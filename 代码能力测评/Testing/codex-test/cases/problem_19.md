# 题目19 删除链表的倒数第 N 个结点

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个链表，删除链表的倒数第 `n`个结点，并且返回链表的头结点。
示例 1：
题目配图：
输入：head = [1,2,3,4,5], n = 2输出：[1,2,3,5]
示例 2：
输入：head = [1], n = 1输出：[]
示例 3：
输入：head = [1,2], n = 1输出：[1]
提示：
链表中结点的数目为 `sz`
`1 <= sz <= 30`
`0 <= Node.val <= 100`
`1 <= n <= sz`
进阶：你能尝试使用一趟扫描实现吗？

```json
{
  "id": 19,
  "title": "删除链表的倒数第 N 个结点",
  "difficulty": "中等",
  "method": "question_19",
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
          },
          2
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2,
          3,
          5
        ]
      }
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          },
          1
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": []
      }
    },
    {
      "name": "case_03_edge_remove_tail",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          },
          1
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_04_edge_remove_head",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          },
          2
        ]
      },
      "expected": [
        2
      ]
    },
    {
      "name": "case_05_edge_remove_first",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3
            ]
          },
          3
        ]
      },
      "expected": [
        2,
        3
      ]
    },
    {
      "name": "case_06_base",
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
          },
          2
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2,
          3,
          5
        ]
      }
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          },
          1
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": []
      }
    },
    {
      "name": "case_08_edge_remove_tail",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          },
          1
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_09_edge_remove_head",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          },
          2
        ]
      },
      "expected": [
        2
      ]
    },
    {
      "name": "case_10_edge_remove_first",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3
            ]
          },
          3
        ]
      },
      "expected": [
        2,
        3
      ]
    },
    {
      "name": "case_11_base",
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
          },
          2
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2,
          3,
          5
        ]
      }
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          },
          1
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": []
      }
    },
    {
      "name": "case_13_edge_remove_tail",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          },
          1
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_14_edge_remove_head",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          },
          2
        ]
      },
      "expected": [
        2
      ]
    },
    {
      "name": "case_15_edge_remove_first",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3
            ]
          },
          3
        ]
      },
      "expected": [
        2,
        3
      ]
    },
    {
      "name": "case_16_base",
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
          },
          2
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2,
          3,
          5
        ]
      }
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          },
          1
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": []
      }
    },
    {
      "name": "case_18_edge_remove_tail",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          },
          1
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_19_edge_remove_head",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          },
          2
        ]
      },
      "expected": [
        2
      ]
    },
    {
      "name": "case_20_edge_remove_first",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3
            ]
          },
          3
        ]
      },
      "expected": [
        2,
        3
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
          },
          2
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2,
          3,
          5
        ]
      }
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          },
          1
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": []
      }
    },
    {
      "name": "case_23_edge_remove_tail",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          },
          1
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_24_edge_remove_head",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          },
          2
        ]
      },
      "expected": [
        2
      ]
    },
    {
      "name": "case_25_edge_remove_first",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3
            ]
          },
          3
        ]
      },
      "expected": [
        2,
        3
      ]
    },
    {
      "name": "case_26_base",
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
          },
          2
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2,
          3,
          5
        ]
      }
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          },
          1
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": []
      }
    },
    {
      "name": "case_28_edge_remove_tail",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          },
          1
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_29_edge_remove_head",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          },
          2
        ]
      },
      "expected": [
        2
      ]
    },
    {
      "name": "case_30_edge_remove_first",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3
            ]
          },
          3
        ]
      },
      "expected": [
        2,
        3
      ]
    },
    {
      "name": "case_31_base",
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
          },
          2
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2,
          3,
          5
        ]
      }
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          },
          1
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": []
      }
    },
    {
      "name": "case_33_edge_remove_tail",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          },
          1
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_34_edge_remove_head",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          },
          2
        ]
      },
      "expected": [
        2
      ]
    },
    {
      "name": "case_35_edge_remove_first",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3
            ]
          },
          3
        ]
      },
      "expected": [
        2,
        3
      ]
    },
    {
      "name": "case_36_base",
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
          },
          2
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2,
          3,
          5
        ]
      }
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          },
          1
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": []
      }
    },
    {
      "name": "case_38_edge_remove_tail",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          },
          1
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_39_edge_remove_head",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          },
          2
        ]
      },
      "expected": [
        2
      ]
    },
    {
      "name": "case_40_edge_remove_first",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3
            ]
          },
          3
        ]
      },
      "expected": [
        2,
        3
      ]
    }
  ]
}
```
