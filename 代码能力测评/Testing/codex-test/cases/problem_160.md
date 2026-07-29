# 题目160 相交链表

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你两个单链表的头节点 `headA` 和 `headB` ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 `null` 。
图示两个链表在节点 `c1` 开始相交：
题目数据 保证 整个链式结构中不存在环。
注意，函数返回结果后，链表必须 保持其原始结构 。
自定义评测：
评测系统 的输入如下（你设计的程序 不适用 此输入）：
`intersectVal` - 相交的起始节点的值。如果不存在相交节点，这一值为 `0`
`listA` - 第一个链表
`listB` - 第二个链表
`skipA` - 在 `listA` 中（从头节点开始）跳到交叉节点的节点数
`skipB` - 在 `listB` 中（从头节点开始）跳到交叉节点的节点数
评测系统将根据这些输入创建链式数据结构，并将两个头节点 `headA` 和 `headB` 传递给你的程序。如果程序能够正确返回相交节点，那么你的解决方案将被 视作正确答案 。
示例 1：
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3输出：Intersected at '8'解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,6,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。— 请注意相交节点的值不为 1，因为在链表 A 和链表 B 之中值为 1 的节点 (A 中第二个节点和 B 中第三个节点) 是不同的节点。换句话说，它们在内存中指向两个不同的位置，而链表 A 和链表 B 中值为 8 的节点 (A 中第三个节点，B 中第四个节点) 在内存中指向相同的位置。
示例 2：
输入：intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1输出：Intersected at '2'解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [1,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
示例 3：
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2输出：null解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。这两个链表不相交，因此返回 null 。
提示：
`listA` 中节点数目为 `m`
`listB` 中节点数目为 `n`
1 <= m, n <= 3 * 10<sup>4</sup>
1 <= Node.val <= 10<sup>5</sup>
`0 <= skipA <= m`
`0 <= skipB <= n`
如果 `listA` 和 `listB` 没有交点，`intersectVal` 为 `0`
如果 `listA` 和 `listB` 有交点，`intersectVal == listA[skipA] == listB[skipB]`
进阶：你能否设计一个时间复杂度 `O(m + n)` 、仅用 `O(1)` 内存的解决方案？

```json
{
  "id": 160,
  "title": "相交链表",
  "difficulty": "简单",
  "method": "question_160",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              4,
              1,
              8,
              4,
              5
            ],
            "listB": [
              5,
              6,
              1,
              8,
              4,
              5
            ],
            "skipA": 2,
            "skipB": 3
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          8,
          4,
          5
        ]
      }
    },
    {
      "name": "case_02_edge_no_intersection",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1
            ],
            "listB": [
              2
            ],
            "skipA": 1,
            "skipB": 1
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_03_edge_intersection_middle",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1,
              9,
              1,
              2,
              4
            ],
            "listB": [
              3,
              2,
              4
            ],
            "skipA": 3,
            "skipB": 1
          }
        ]
      },
      "expected": [
        2,
        4
      ]
    },
    {
      "name": "case_04_base",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              4,
              1,
              8,
              4,
              5
            ],
            "listB": [
              5,
              6,
              1,
              8,
              4,
              5
            ],
            "skipA": 2,
            "skipB": 3
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          8,
          4,
          5
        ]
      }
    },
    {
      "name": "case_05_edge_no_intersection",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1
            ],
            "listB": [
              2
            ],
            "skipA": 1,
            "skipB": 1
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_06_edge_intersection_middle",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1,
              9,
              1,
              2,
              4
            ],
            "listB": [
              3,
              2,
              4
            ],
            "skipA": 3,
            "skipB": 1
          }
        ]
      },
      "expected": [
        2,
        4
      ]
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              4,
              1,
              8,
              4,
              5
            ],
            "listB": [
              5,
              6,
              1,
              8,
              4,
              5
            ],
            "skipA": 2,
            "skipB": 3
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          8,
          4,
          5
        ]
      }
    },
    {
      "name": "case_08_edge_no_intersection",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1
            ],
            "listB": [
              2
            ],
            "skipA": 1,
            "skipB": 1
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_09_edge_intersection_middle",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1,
              9,
              1,
              2,
              4
            ],
            "listB": [
              3,
              2,
              4
            ],
            "skipA": 3,
            "skipB": 1
          }
        ]
      },
      "expected": [
        2,
        4
      ]
    },
    {
      "name": "case_10_base",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              4,
              1,
              8,
              4,
              5
            ],
            "listB": [
              5,
              6,
              1,
              8,
              4,
              5
            ],
            "skipA": 2,
            "skipB": 3
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          8,
          4,
          5
        ]
      }
    },
    {
      "name": "case_11_edge_no_intersection",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1
            ],
            "listB": [
              2
            ],
            "skipA": 1,
            "skipB": 1
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_12_edge_intersection_middle",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1,
              9,
              1,
              2,
              4
            ],
            "listB": [
              3,
              2,
              4
            ],
            "skipA": 3,
            "skipB": 1
          }
        ]
      },
      "expected": [
        2,
        4
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              4,
              1,
              8,
              4,
              5
            ],
            "listB": [
              5,
              6,
              1,
              8,
              4,
              5
            ],
            "skipA": 2,
            "skipB": 3
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          8,
          4,
          5
        ]
      }
    },
    {
      "name": "case_14_edge_no_intersection",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1
            ],
            "listB": [
              2
            ],
            "skipA": 1,
            "skipB": 1
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_15_edge_intersection_middle",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1,
              9,
              1,
              2,
              4
            ],
            "listB": [
              3,
              2,
              4
            ],
            "skipA": 3,
            "skipB": 1
          }
        ]
      },
      "expected": [
        2,
        4
      ]
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              4,
              1,
              8,
              4,
              5
            ],
            "listB": [
              5,
              6,
              1,
              8,
              4,
              5
            ],
            "skipA": 2,
            "skipB": 3
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          8,
          4,
          5
        ]
      }
    },
    {
      "name": "case_17_edge_no_intersection",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1
            ],
            "listB": [
              2
            ],
            "skipA": 1,
            "skipB": 1
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_18_edge_intersection_middle",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1,
              9,
              1,
              2,
              4
            ],
            "listB": [
              3,
              2,
              4
            ],
            "skipA": 3,
            "skipB": 1
          }
        ]
      },
      "expected": [
        2,
        4
      ]
    },
    {
      "name": "case_19_base",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              4,
              1,
              8,
              4,
              5
            ],
            "listB": [
              5,
              6,
              1,
              8,
              4,
              5
            ],
            "skipA": 2,
            "skipB": 3
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          8,
          4,
          5
        ]
      }
    },
    {
      "name": "case_20_edge_no_intersection",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1
            ],
            "listB": [
              2
            ],
            "skipA": 1,
            "skipB": 1
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_21_edge_intersection_middle",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1,
              9,
              1,
              2,
              4
            ],
            "listB": [
              3,
              2,
              4
            ],
            "skipA": 3,
            "skipB": 1
          }
        ]
      },
      "expected": [
        2,
        4
      ]
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              4,
              1,
              8,
              4,
              5
            ],
            "listB": [
              5,
              6,
              1,
              8,
              4,
              5
            ],
            "skipA": 2,
            "skipB": 3
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          8,
          4,
          5
        ]
      }
    },
    {
      "name": "case_23_edge_no_intersection",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1
            ],
            "listB": [
              2
            ],
            "skipA": 1,
            "skipB": 1
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_24_edge_intersection_middle",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1,
              9,
              1,
              2,
              4
            ],
            "listB": [
              3,
              2,
              4
            ],
            "skipA": 3,
            "skipB": 1
          }
        ]
      },
      "expected": [
        2,
        4
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              4,
              1,
              8,
              4,
              5
            ],
            "listB": [
              5,
              6,
              1,
              8,
              4,
              5
            ],
            "skipA": 2,
            "skipB": 3
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          8,
          4,
          5
        ]
      }
    },
    {
      "name": "case_26_edge_no_intersection",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1
            ],
            "listB": [
              2
            ],
            "skipA": 1,
            "skipB": 1
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_27_edge_intersection_middle",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1,
              9,
              1,
              2,
              4
            ],
            "listB": [
              3,
              2,
              4
            ],
            "skipA": 3,
            "skipB": 1
          }
        ]
      },
      "expected": [
        2,
        4
      ]
    },
    {
      "name": "case_28_base",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              4,
              1,
              8,
              4,
              5
            ],
            "listB": [
              5,
              6,
              1,
              8,
              4,
              5
            ],
            "skipA": 2,
            "skipB": 3
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          8,
          4,
          5
        ]
      }
    },
    {
      "name": "case_29_edge_no_intersection",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1
            ],
            "listB": [
              2
            ],
            "skipA": 1,
            "skipB": 1
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_30_edge_intersection_middle",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1,
              9,
              1,
              2,
              4
            ],
            "listB": [
              3,
              2,
              4
            ],
            "skipA": 3,
            "skipB": 1
          }
        ]
      },
      "expected": [
        2,
        4
      ]
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              4,
              1,
              8,
              4,
              5
            ],
            "listB": [
              5,
              6,
              1,
              8,
              4,
              5
            ],
            "skipA": 2,
            "skipB": 3
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          8,
          4,
          5
        ]
      }
    },
    {
      "name": "case_32_edge_no_intersection",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1
            ],
            "listB": [
              2
            ],
            "skipA": 1,
            "skipB": 1
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_33_edge_intersection_middle",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1,
              9,
              1,
              2,
              4
            ],
            "listB": [
              3,
              2,
              4
            ],
            "skipA": 3,
            "skipB": 1
          }
        ]
      },
      "expected": [
        2,
        4
      ]
    },
    {
      "name": "case_34_base",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              4,
              1,
              8,
              4,
              5
            ],
            "listB": [
              5,
              6,
              1,
              8,
              4,
              5
            ],
            "skipA": 2,
            "skipB": 3
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          8,
          4,
          5
        ]
      }
    },
    {
      "name": "case_35_edge_no_intersection",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1
            ],
            "listB": [
              2
            ],
            "skipA": 1,
            "skipB": 1
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_36_edge_intersection_middle",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1,
              9,
              1,
              2,
              4
            ],
            "listB": [
              3,
              2,
              4
            ],
            "skipA": 3,
            "skipB": 1
          }
        ]
      },
      "expected": [
        2,
        4
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              4,
              1,
              8,
              4,
              5
            ],
            "listB": [
              5,
              6,
              1,
              8,
              4,
              5
            ],
            "skipA": 2,
            "skipB": 3
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          8,
          4,
          5
        ]
      }
    },
    {
      "name": "case_38_edge_no_intersection",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1
            ],
            "listB": [
              2
            ],
            "skipA": 1,
            "skipB": 1
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_39_edge_intersection_middle",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              1,
              9,
              1,
              2,
              4
            ],
            "listB": [
              3,
              2,
              4
            ],
            "skipA": 3,
            "skipB": 1
          }
        ]
      },
      "expected": [
        2,
        4
      ]
    },
    {
      "name": "case_40_base",
      "input": {
        "args": [
          {
            "__type__": "IntersectListNodePair",
            "listA": [
              4,
              1,
              8,
              4,
              5
            ],
            "listB": [
              5,
              6,
              1,
              8,
              4,
              5
            ],
            "skipA": 2,
            "skipB": 3
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          8,
          4,
          5
        ]
      }
    }
  ]
}
```
