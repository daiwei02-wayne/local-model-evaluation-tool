# 题目21 合并两个有序链表

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
示例 1：
题目配图：
输入：l1 = [1,2,4], l2 = [1,3,4]输出：[1,1,2,3,4,4]
示例 2：
输入：l1 = [], l2 = []输出：[]
示例 3：
输入：l1 = [], l2 = [0]输出：[0]
提示：
两个链表的节点数目范围是 `[0, 50]`
`-100 <= Node.val <= 100`
`l1` 和 `l2` 均按 非递减顺序 排列

```json
{
  "id": 21,
  "title": "合并两个有序链表",
  "difficulty": "简单",
  "method": "question_21",
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
              4
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              1,
              3,
              4
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          1,
          2,
          3,
          4,
          4
        ]
      }
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": []
      }
    },
    {
      "name": "case_03_edge_one_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          }
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_04_edge_negatives",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              -10,
              -1,
              3
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              -2,
              0,
              4
            ]
          }
        ]
      },
      "expected": [
        -10,
        -2,
        -1,
        0,
        3,
        4
      ]
    },
    {
      "name": "case_05_edge_both_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": null
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
              4
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              1,
              3,
              4
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          1,
          2,
          3,
          4,
          4
        ]
      }
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": []
      }
    },
    {
      "name": "case_08_edge_one_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          }
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_09_edge_negatives",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              -10,
              -1,
              3
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              -2,
              0,
              4
            ]
          }
        ]
      },
      "expected": [
        -10,
        -2,
        -1,
        0,
        3,
        4
      ]
    },
    {
      "name": "case_10_edge_both_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": null
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
              4
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              1,
              3,
              4
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          1,
          2,
          3,
          4,
          4
        ]
      }
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": []
      }
    },
    {
      "name": "case_13_edge_one_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          }
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_14_edge_negatives",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              -10,
              -1,
              3
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              -2,
              0,
              4
            ]
          }
        ]
      },
      "expected": [
        -10,
        -2,
        -1,
        0,
        3,
        4
      ]
    },
    {
      "name": "case_15_edge_both_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": null
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
              4
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              1,
              3,
              4
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          1,
          2,
          3,
          4,
          4
        ]
      }
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": []
      }
    },
    {
      "name": "case_18_edge_one_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          }
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_19_edge_negatives",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              -10,
              -1,
              3
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              -2,
              0,
              4
            ]
          }
        ]
      },
      "expected": [
        -10,
        -2,
        -1,
        0,
        3,
        4
      ]
    },
    {
      "name": "case_20_edge_both_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": null
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
              4
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              1,
              3,
              4
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          1,
          2,
          3,
          4,
          4
        ]
      }
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": []
      }
    },
    {
      "name": "case_23_edge_one_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          }
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_24_edge_negatives",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              -10,
              -1,
              3
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              -2,
              0,
              4
            ]
          }
        ]
      },
      "expected": [
        -10,
        -2,
        -1,
        0,
        3,
        4
      ]
    },
    {
      "name": "case_25_edge_both_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": null
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
              4
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              1,
              3,
              4
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          1,
          2,
          3,
          4,
          4
        ]
      }
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": []
      }
    },
    {
      "name": "case_28_edge_one_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          }
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_29_edge_negatives",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              -10,
              -1,
              3
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              -2,
              0,
              4
            ]
          }
        ]
      },
      "expected": [
        -10,
        -2,
        -1,
        0,
        3,
        4
      ]
    },
    {
      "name": "case_30_edge_both_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": null
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
              4
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              1,
              3,
              4
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          1,
          2,
          3,
          4,
          4
        ]
      }
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": []
      }
    },
    {
      "name": "case_33_edge_one_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          }
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_34_edge_negatives",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              -10,
              -1,
              3
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              -2,
              0,
              4
            ]
          }
        ]
      },
      "expected": [
        -10,
        -2,
        -1,
        0,
        3,
        4
      ]
    },
    {
      "name": "case_35_edge_both_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": null
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
              4
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              1,
              3,
              4
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          1,
          2,
          3,
          4,
          4
        ]
      }
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": []
      }
    },
    {
      "name": "case_38_edge_one_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          }
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_39_edge_negatives",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              -10,
              -1,
              3
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              -2,
              0,
              4
            ]
          }
        ]
      },
      "expected": [
        -10,
        -2,
        -1,
        0,
        3,
        4
      ]
    },
    {
      "name": "case_40_edge_both_empty",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": []
          },
          {
            "__type__": "ListNode",
            "value": []
          }
        ]
      },
      "expected": null
    }
  ]
}
```
