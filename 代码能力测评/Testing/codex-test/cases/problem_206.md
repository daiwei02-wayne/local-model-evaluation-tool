# 题目206 反转链表

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你单链表的头节点 `head` ，请你反转链表，并返回反转后的链表。
示例 1：
题目配图：
输入：head = [1,2,3,4,5]输出：[5,4,3,2,1]
示例 2：
题目配图：
输入：head = [1,2]输出：[2,1]
示例 3：
输入：head = []输出：[]
提示：
链表中节点的数目范围是 `[0, 5000]`
`-5000 <= Node.val <= 5000`
进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？

```json
{
  "id": 206,
  "title": "反转链表",
  "difficulty": "简单",
  "method": "question_206",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              4,
              5
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          5,
          4,
          3,
          2,
          1
        ]
      }
    },
    {
      "name": "case_02_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_03_edge_single",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_04_edge_two",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          }
        ]
      },
      "expected": [
        2,
        1
      ]
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              4,
              5
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          5,
          4,
          3,
          2,
          1
        ]
      }
    },
    {
      "name": "case_06_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_07_edge_single",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_08_edge_two",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          }
        ]
      },
      "expected": [
        2,
        1
      ]
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              4,
              5
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          5,
          4,
          3,
          2,
          1
        ]
      }
    },
    {
      "name": "case_10_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_11_edge_single",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_12_edge_two",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          }
        ]
      },
      "expected": [
        2,
        1
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              4,
              5
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          5,
          4,
          3,
          2,
          1
        ]
      }
    },
    {
      "name": "case_14_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_15_edge_single",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_16_edge_two",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          }
        ]
      },
      "expected": [
        2,
        1
      ]
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              4,
              5
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          5,
          4,
          3,
          2,
          1
        ]
      }
    },
    {
      "name": "case_18_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_19_edge_single",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_20_edge_two",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          }
        ]
      },
      "expected": [
        2,
        1
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              4,
              5
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          5,
          4,
          3,
          2,
          1
        ]
      }
    },
    {
      "name": "case_22_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_23_edge_single",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_24_edge_two",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          }
        ]
      },
      "expected": [
        2,
        1
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              4,
              5
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          5,
          4,
          3,
          2,
          1
        ]
      }
    },
    {
      "name": "case_26_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_27_edge_single",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_28_edge_two",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          }
        ]
      },
      "expected": [
        2,
        1
      ]
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              4,
              5
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          5,
          4,
          3,
          2,
          1
        ]
      }
    },
    {
      "name": "case_30_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_31_edge_single",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_32_edge_two",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          }
        ]
      },
      "expected": [
        2,
        1
      ]
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              4,
              5
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          5,
          4,
          3,
          2,
          1
        ]
      }
    },
    {
      "name": "case_34_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_35_edge_single",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_36_edge_two",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          }
        ]
      },
      "expected": [
        2,
        1
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              4,
              5
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          5,
          4,
          3,
          2,
          1
        ]
      }
    },
    {
      "name": "case_38_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_39_edge_single",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_40_edge_two",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          }
        ]
      },
      "expected": [
        2,
        1
      ]
    }
  ]
}
```
