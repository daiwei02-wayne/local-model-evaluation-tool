from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Any


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class RandomNode:
    def __init__(
        self,
        x: int,
        next: "RandomNode | None" = None,
        random: "RandomNode | None" = None,
    ):
        self.val = int(x)
        self.next = next
        self.random = random


@dataclass
class SpreadArgs:
    values: list[Any]


def decode_args(args: list[Any], kwargs: dict[str, Any]) -> tuple[list[Any], dict[str, Any], dict[str, Any]]:
    context: dict[str, Any] = {"list_nodes": {}, "tree_nodes": {}}
    decoded_args: list[Any] = []
    for i, value in enumerate(args):
        decoded = _decode_value(value, context, arg_index=i)
        if isinstance(decoded, SpreadArgs):
            decoded_args.extend(decoded.values)
        else:
            decoded_args.append(decoded)
    decoded_kwargs = {key: _decode_value(value, context) for key, value in kwargs.items()}
    return decoded_args, decoded_kwargs, context


def encode_value(value: Any, context: dict[str, Any] | None = None) -> Any:
    if isinstance(value, ListNode):
        return _listnode_to_list(value)
    if isinstance(value, TreeNode):
        return _treenode_to_level_list(value)
    if isinstance(value, RandomNode) or _looks_like_random_node(value):
        return _randomnode_to_list(value)
    if isinstance(value, list):
        return [encode_value(item, context) for item in value]
    if isinstance(value, tuple):
        return [encode_value(item, context) for item in value]
    if isinstance(value, dict):
        return {key: encode_value(item, context) for key, item in value.items()}
    return value


def value_for_expectation(
    returned: Any,
    args: list[Any],
    expectation: dict[str, Any],
    context: dict[str, Any],
) -> Any:
    source = expectation.get("source", "return")
    if source == "return":
        return encode_value(returned, context)
    if source == "return_node_value":
        return None if returned is None else getattr(returned, "val", returned)
    if source == "arg":
        return encode_value(args[int(expectation["index"])], context)
    if source == "linked_cycle_entry_index":
        node = returned
        mapping = context["list_nodes"].get(int(expectation.get("arg_index", 0)), {})
        return mapping.get(id(node), -1) if node is not None else -1
    raise ValueError(f"未知 expectation.source: {source}")


def normalize_expected(value: Any) -> Any:
    if isinstance(value, dict) and "__type__" in value:
        kind = value["__type__"]
        if kind in {"ListNode", "TreeNode", "ListNodeArray", "RandomNode"}:
            return value.get("value")
        return value.get("value")
    if isinstance(value, list):
        return [normalize_expected(item) for item in value]
    if isinstance(value, dict):
        return {key: normalize_expected(item) for key, item in value.items()}
    return value


def _decode_value(value: Any, context: dict[str, Any], arg_index: int | None = None) -> Any:
    if isinstance(value, dict) and "__type__" in value:
        kind = value["__type__"]
        if kind == "ListNode":
            head, mapping = _list_to_listnode(value.get("value", []))
            if arg_index is not None:
                context["list_nodes"][arg_index] = mapping
            return head
        if kind == "CycleListNode":
            head, mapping = _list_to_cycle_listnode(value.get("value", []), value.get("pos", -1))
            if arg_index is not None:
                context["list_nodes"][arg_index] = mapping
            return head
        if kind == "ListNodeArray":
            return [_list_to_listnode(item)[0] for item in value.get("value", [])]
        if kind == "IntersectListNodePair":
            return SpreadArgs(_intersect_list_pair(value))
        if kind == "TreeNode":
            root, mapping = _level_list_to_treenode(value.get("value", []))
            if arg_index is not None:
                context["tree_nodes"][arg_index] = mapping
            return root
        if kind == "RandomNode":
            return _list_to_randomnode(value.get("value", []))
        if kind == "TreeNodeRef":
            tree_arg = int(value["tree_arg"])
            return context["tree_nodes"][tree_arg][value["value"]]
        raise ValueError(f"未知数据类型: {kind}")
    if isinstance(value, list):
        return [_decode_value(item, context) for item in value]
    if isinstance(value, dict):
        return {key: _decode_value(item, context) for key, item in value.items()}
    return value


def _list_to_listnode(values: list[Any]) -> tuple[ListNode | None, dict[int, int]]:
    dummy = ListNode()
    current = dummy
    mapping: dict[int, int] = {}
    for index, value in enumerate(values):
        current.next = ListNode(value)
        current = current.next
        mapping[id(current)] = index
    return dummy.next, mapping


def _list_to_cycle_listnode(values: list[Any], pos: int) -> tuple[ListNode | None, dict[int, int]]:
    head, mapping = _list_to_listnode(values)
    if head is None or pos < 0:
        return head, mapping
    nodes: list[ListNode] = []
    current = head
    while current:
        nodes.append(current)
        if current.next is None:
            break
        current = current.next
    if 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]
    return head, mapping


def _intersect_list_pair(value: dict[str, Any]) -> list[ListNode | None]:
    list_a = value.get("listA", [])
    list_b = value.get("listB", [])
    skip_a = int(value.get("skipA", len(list_a)))
    skip_b = int(value.get("skipB", len(list_b)))
    shared, _ = _list_to_listnode(list_a[skip_a:])
    head_a = _prefix_to_shared(list_a[:skip_a], shared)
    head_b = _prefix_to_shared(list_b[:skip_b], shared)
    return [head_a, head_b]


def _prefix_to_shared(prefix: list[Any], shared: ListNode | None) -> ListNode | None:
    dummy = ListNode()
    current = dummy
    for item in prefix:
        current.next = ListNode(item)
        current = current.next
    current.next = shared
    return dummy.next


def _listnode_to_list(head: ListNode | None, limit: int = 10000) -> list[Any]:
    values: list[Any] = []
    seen: set[int] = set()
    current = head
    while current is not None and id(current) not in seen and len(values) < limit:
        seen.add(id(current))
        values.append(current.val)
        current = current.next
    return values


def _level_list_to_treenode(values: list[Any]) -> tuple[TreeNode | None, dict[Any, TreeNode]]:
    if not values or values[0] is None:
        return None, {}
    root = TreeNode(values[0])
    by_value: dict[Any, TreeNode] = {values[0]: root}
    queue: deque[TreeNode] = deque([root])
    index = 1
    while queue and index < len(values):
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            by_value.setdefault(values[index], node.left)
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            by_value.setdefault(values[index], node.right)
            queue.append(node.right)
        index += 1
    return root, by_value


def _treenode_to_level_list(root: TreeNode | None) -> list[Any]:
    if root is None:
        return []
    result: list[Any] = []
    queue: deque[TreeNode | None] = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


def _list_to_randomnode(values: list[Any]) -> RandomNode | None:
    if not values:
        return None
    nodes = [RandomNode(item[0]) for item in values]
    for index, item in enumerate(values):
        if index + 1 < len(nodes):
            nodes[index].next = nodes[index + 1]
        random_index = item[1]
        if random_index is not None and random_index >= 0:
            nodes[index].random = nodes[random_index]
    return nodes[0]


def _randomnode_to_list(head: Any) -> list[list[Any]]:
    nodes: list[Any] = []
    index_by_id: dict[int, int] = {}
    current = head
    while current is not None and id(current) not in index_by_id:
        index_by_id[id(current)] = len(nodes)
        nodes.append(current)
        current = current.next
    result: list[list[Any]] = []
    for node in nodes:
        random_index = None if node.random is None else index_by_id.get(id(node.random))
        result.append([node.val, random_index])
    return result


def _looks_like_random_node(value: Any) -> bool:
    return (
        value is not None
        and hasattr(value, "val")
        and hasattr(value, "next")
        and hasattr(value, "random")
    )
