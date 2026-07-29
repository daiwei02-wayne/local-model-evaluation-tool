# 题目25 K 个一组翻转链表

来源：LeetCode 热题 100（https://leetcode.cn/studyplan/top-100-liked/）

```json
{
  "id": 25,
  "title": "K 个一组翻转链表",
  "difficulty": "困难",
  "method": "question_25",
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
          2,
          1,
          4,
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
              1,
              2,
              3,
              4,
              5
            ]
          },
          3
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          3,
          2,
          1,
          4,
          5
        ]
      }
    },
    {
      "name": "case_03_base",
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
        "value": [
          1
        ]
      }
    },
    {
      "name": "case_04_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          },
          3
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2
        ]
      }
    },
    {
      "name": "case_05_edge_exact_groups",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              4,
              5,
              6
            ]
          },
          3
        ]
      },
      "expected": [
        3,
        2,
        1,
        6,
        5,
        4
      ]
    },
    {
      "name": "case_06_edge_k_one",
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
          1
        ]
      },
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_07_edge_k_gt_len",
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
          4
        ]
      },
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_08_base",
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
          2,
          1,
          4,
          3,
          5
        ]
      }
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
          },
          3
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          3,
          2,
          1,
          4,
          5
        ]
      }
    },
    {
      "name": "case_10_base",
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
        "value": [
          1
        ]
      }
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          },
          3
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2
        ]
      }
    },
    {
      "name": "case_12_edge_exact_groups",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              4,
              5,
              6
            ]
          },
          3
        ]
      },
      "expected": [
        3,
        2,
        1,
        6,
        5,
        4
      ]
    },
    {
      "name": "case_13_edge_k_one",
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
          1
        ]
      },
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_14_edge_k_gt_len",
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
          4
        ]
      },
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_15_base",
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
          2,
          1,
          4,
          3,
          5
        ]
      }
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
          3
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          3,
          2,
          1,
          4,
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
        "value": [
          1
        ]
      }
    },
    {
      "name": "case_18_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          },
          3
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2
        ]
      }
    },
    {
      "name": "case_19_edge_exact_groups",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              4,
              5,
              6
            ]
          },
          3
        ]
      },
      "expected": [
        3,
        2,
        1,
        6,
        5,
        4
      ]
    },
    {
      "name": "case_20_edge_k_one",
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
          1
        ]
      },
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_21_edge_k_gt_len",
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
          4
        ]
      },
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_22_base",
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
          2,
          1,
          4,
          3,
          5
        ]
      }
    },
    {
      "name": "case_23_base",
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
          3
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          3,
          2,
          1,
          4,
          5
        ]
      }
    },
    {
      "name": "case_24_base",
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
        "value": [
          1
        ]
      }
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          },
          3
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2
        ]
      }
    },
    {
      "name": "case_26_edge_exact_groups",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              4,
              5,
              6
            ]
          },
          3
        ]
      },
      "expected": [
        3,
        2,
        1,
        6,
        5,
        4
      ]
    },
    {
      "name": "case_27_edge_k_one",
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
          1
        ]
      },
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_28_edge_k_gt_len",
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
          4
        ]
      },
      "expected": [
        1,
        2,
        3
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
          },
          2
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          2,
          1,
          4,
          3,
          5
        ]
      }
    },
    {
      "name": "case_30_base",
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
          3
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          3,
          2,
          1,
          4,
          5
        ]
      }
    },
    {
      "name": "case_31_base",
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
        "value": [
          1
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
              1,
              2
            ]
          },
          3
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2
        ]
      }
    },
    {
      "name": "case_33_edge_exact_groups",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              4,
              5,
              6
            ]
          },
          3
        ]
      },
      "expected": [
        3,
        2,
        1,
        6,
        5,
        4
      ]
    },
    {
      "name": "case_34_edge_k_one",
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
          1
        ]
      },
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_35_edge_k_gt_len",
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
          4
        ]
      },
      "expected": [
        1,
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
          2,
          1,
          4,
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
              1,
              2,
              3,
              4,
              5
            ]
          },
          3
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          3,
          2,
          1,
          4,
          5
        ]
      }
    },
    {
      "name": "case_38_base",
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
        "value": [
          1
        ]
      }
    },
    {
      "name": "case_39_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2
            ]
          },
          3
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          1,
          2
        ]
      }
    },
    {
      "name": "case_40_edge_exact_groups",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              4,
              5,
              6
            ]
          },
          3
        ]
      },
      "expected": [
        3,
        2,
        1,
        6,
        5,
        4
      ]
    }
  ]
}
```
