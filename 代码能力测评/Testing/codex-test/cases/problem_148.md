# 题目148 排序链表

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你链表的头结点 `head` ，请将其按 升序 排列并返回 排序后的链表 。
示例 1：
题目配图：
输入：head = [4,2,1,3]输出：[1,2,3,4]
示例 2：
题目配图：
输入：head = [-1,5,3,4,0]输出：[-1,0,3,4,5]
示例 3：
输入：head = []输出：[]
提示：
链表中节点的数目在范围 [0, 5 * 10<sup>4</sup>] 内
-10<sup>5</sup> <= Node.val <= 10<sup>5</sup>
进阶：你可以在 `O(n log n)` 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

```json
{
  "id": 148,
  "title": "排序链表",
  "difficulty": "中等",
  "method": "question_148",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              4,
              2,
              1,
              3
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2,
          3,
          4
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
      "name": "case_04_edge_negative",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              -1,
              5,
              3,
              4,
              0
            ]
          }
        ]
      },
      "expected": [
        -1,
        0,
        3,
        4,
        5
      ]
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              4,
              2,
              1,
              3
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2,
          3,
          4
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
      "name": "case_08_edge_negative",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              -1,
              5,
              3,
              4,
              0
            ]
          }
        ]
      },
      "expected": [
        -1,
        0,
        3,
        4,
        5
      ]
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              4,
              2,
              1,
              3
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2,
          3,
          4
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
      "name": "case_12_edge_negative",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              -1,
              5,
              3,
              4,
              0
            ]
          }
        ]
      },
      "expected": [
        -1,
        0,
        3,
        4,
        5
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              4,
              2,
              1,
              3
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2,
          3,
          4
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
      "name": "case_16_edge_negative",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              -1,
              5,
              3,
              4,
              0
            ]
          }
        ]
      },
      "expected": [
        -1,
        0,
        3,
        4,
        5
      ]
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              4,
              2,
              1,
              3
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2,
          3,
          4
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
      "name": "case_20_edge_negative",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              -1,
              5,
              3,
              4,
              0
            ]
          }
        ]
      },
      "expected": [
        -1,
        0,
        3,
        4,
        5
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              4,
              2,
              1,
              3
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2,
          3,
          4
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
      "name": "case_24_edge_negative",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              -1,
              5,
              3,
              4,
              0
            ]
          }
        ]
      },
      "expected": [
        -1,
        0,
        3,
        4,
        5
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              4,
              2,
              1,
              3
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2,
          3,
          4
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
      "name": "case_28_edge_negative",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              -1,
              5,
              3,
              4,
              0
            ]
          }
        ]
      },
      "expected": [
        -1,
        0,
        3,
        4,
        5
      ]
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              4,
              2,
              1,
              3
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2,
          3,
          4
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
      "name": "case_32_edge_negative",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              -1,
              5,
              3,
              4,
              0
            ]
          }
        ]
      },
      "expected": [
        -1,
        0,
        3,
        4,
        5
      ]
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              4,
              2,
              1,
              3
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2,
          3,
          4
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
      "name": "case_36_edge_negative",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              -1,
              5,
              3,
              4,
              0
            ]
          }
        ]
      },
      "expected": [
        -1,
        0,
        3,
        4,
        5
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              4,
              2,
              1,
              3
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2,
          3,
          4
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
      "name": "case_40_edge_negative",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              -1,
              5,
              3,
              4,
              0
            ]
          }
        ]
      },
      "expected": [
        -1,
        0,
        3,
        4,
        5
      ]
    }
  ]
}
```
