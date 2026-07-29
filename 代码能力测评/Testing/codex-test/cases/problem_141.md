# 题目141 环形链表

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个链表的头节点 `head` ，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：`pos` 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
_如果链表中存在环_ ，则返回 `true` 。 否则，返回 `false` 。
示例 1：
题目配图：
输入：head = [3,2,0,-4], pos = 1输出：true解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：
题目配图：
输入：head = [1,2], pos = 0输出：true解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：
题目配图：
输入：head = [1], pos = -1输出：false解释：链表中没有环。
提示：
链表中节点的数目范围是 [0, 10<sup>4</sup>]
-10<sup>5</sup> <= Node.val <= 10<sup>5</sup>
`pos` 为 `-1` 或者链表中的一个 有效索引 。
进阶：你能用 `O(1)`（即，常量）内存解决此问题吗？

```json
{
  "id": 141,
  "title": "环形链表",
  "difficulty": "简单",
  "method": "question_141",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              3,
              2,
              0,
              -4
            ],
            "pos": 1
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1
            ],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_03_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_04_edge_self_cycle",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1
            ],
            "pos": 0
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_05_edge_no_cycle",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1,
              2
            ],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              3,
              2,
              0,
              -4
            ],
            "pos": 1
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1
            ],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_08_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_09_edge_self_cycle",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1
            ],
            "pos": 0
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_10_edge_no_cycle",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1,
              2
            ],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              3,
              2,
              0,
              -4
            ],
            "pos": 1
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1
            ],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_13_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_14_edge_self_cycle",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1
            ],
            "pos": 0
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_15_edge_no_cycle",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1,
              2
            ],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              3,
              2,
              0,
              -4
            ],
            "pos": 1
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1
            ],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_18_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_19_edge_self_cycle",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1
            ],
            "pos": 0
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_20_edge_no_cycle",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1,
              2
            ],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              3,
              2,
              0,
              -4
            ],
            "pos": 1
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1
            ],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_23_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_24_edge_self_cycle",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1
            ],
            "pos": 0
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_25_edge_no_cycle",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1,
              2
            ],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              3,
              2,
              0,
              -4
            ],
            "pos": 1
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1
            ],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_28_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_29_edge_self_cycle",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1
            ],
            "pos": 0
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_30_edge_no_cycle",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1,
              2
            ],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              3,
              2,
              0,
              -4
            ],
            "pos": 1
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1
            ],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_33_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_34_edge_self_cycle",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1
            ],
            "pos": 0
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_35_edge_no_cycle",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1,
              2
            ],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              3,
              2,
              0,
              -4
            ],
            "pos": 1
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1
            ],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_38_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [],
            "pos": -1
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_39_edge_self_cycle",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1
            ],
            "pos": 0
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_40_edge_no_cycle",
      "input": {
        "args": [
          {
            "__type__": "CycleListNode",
            "value": [
              1,
              2
            ],
            "pos": -1
          }
        ]
      },
      "expected": false
    }
  ]
}
```
