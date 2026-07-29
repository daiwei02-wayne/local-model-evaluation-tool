# 题目2 两数相加

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例 1：
题目配图：
输入：l1 = [2,4,3], l2 = [5,6,4]输出：[7,0,8]解释：342 + 465 = 807.
示例 2：
输入：l1 = [0], l2 = [0]输出：[0]
示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]输出：[8,9,9,9,0,0,0,1]
提示：
每个链表中的节点数在范围 `[1, 100]` 内
`0 <= Node.val <= 9`
题目数据保证列表表示的数字不含前导零

```json
{
  "id": 2,
  "title": "两数相加",
  "difficulty": "中等",
  "method": "question_2",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              2,
              4,
              3
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              5,
              6,
              4
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          7,
          0,
          8
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
              0
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          0
        ]
      }
    },
    {
      "name": "case_03_edge_long_carry",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              9,
              9,
              9,
              9
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": [
        0,
        0,
        0,
        0,
        1
      ]
    },
    {
      "name": "case_04_edge_single_carry",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              5
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              5
            ]
          }
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_05_edge_uneven",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              9,
              9
            ]
          }
        ]
      },
      "expected": [
        9,
        9
      ]
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              2,
              4,
              3
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              5,
              6,
              4
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          7,
          0,
          8
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
              0
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          0
        ]
      }
    },
    {
      "name": "case_08_edge_long_carry",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              9,
              9,
              9,
              9
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": [
        0,
        0,
        0,
        0,
        1
      ]
    },
    {
      "name": "case_09_edge_single_carry",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              5
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              5
            ]
          }
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_10_edge_uneven",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              9,
              9
            ]
          }
        ]
      },
      "expected": [
        9,
        9
      ]
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              2,
              4,
              3
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              5,
              6,
              4
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          7,
          0,
          8
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
              0
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          0
        ]
      }
    },
    {
      "name": "case_13_edge_long_carry",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              9,
              9,
              9,
              9
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": [
        0,
        0,
        0,
        0,
        1
      ]
    },
    {
      "name": "case_14_edge_single_carry",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              5
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              5
            ]
          }
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_15_edge_uneven",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              9,
              9
            ]
          }
        ]
      },
      "expected": [
        9,
        9
      ]
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              2,
              4,
              3
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              5,
              6,
              4
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          7,
          0,
          8
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
              0
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          0
        ]
      }
    },
    {
      "name": "case_18_edge_long_carry",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              9,
              9,
              9,
              9
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": [
        0,
        0,
        0,
        0,
        1
      ]
    },
    {
      "name": "case_19_edge_single_carry",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              5
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              5
            ]
          }
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_20_edge_uneven",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              9,
              9
            ]
          }
        ]
      },
      "expected": [
        9,
        9
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              2,
              4,
              3
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              5,
              6,
              4
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          7,
          0,
          8
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
              0
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          0
        ]
      }
    },
    {
      "name": "case_23_edge_long_carry",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              9,
              9,
              9,
              9
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": [
        0,
        0,
        0,
        0,
        1
      ]
    },
    {
      "name": "case_24_edge_single_carry",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              5
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              5
            ]
          }
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_25_edge_uneven",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              9,
              9
            ]
          }
        ]
      },
      "expected": [
        9,
        9
      ]
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              2,
              4,
              3
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              5,
              6,
              4
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          7,
          0,
          8
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
              0
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          0
        ]
      }
    },
    {
      "name": "case_28_edge_long_carry",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              9,
              9,
              9,
              9
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": [
        0,
        0,
        0,
        0,
        1
      ]
    },
    {
      "name": "case_29_edge_single_carry",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              5
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              5
            ]
          }
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_30_edge_uneven",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              9,
              9
            ]
          }
        ]
      },
      "expected": [
        9,
        9
      ]
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              2,
              4,
              3
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              5,
              6,
              4
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          7,
          0,
          8
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
              0
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          0
        ]
      }
    },
    {
      "name": "case_33_edge_long_carry",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              9,
              9,
              9,
              9
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": [
        0,
        0,
        0,
        0,
        1
      ]
    },
    {
      "name": "case_34_edge_single_carry",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              5
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              5
            ]
          }
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_35_edge_uneven",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              9,
              9
            ]
          }
        ]
      },
      "expected": [
        9,
        9
      ]
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              2,
              4,
              3
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              5,
              6,
              4
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          7,
          0,
          8
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
              0
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          }
        ]
      },
      "expected": {
        "__type__": "ListNode",
        "value": [
          0
        ]
      }
    },
    {
      "name": "case_38_edge_long_carry",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              9,
              9,
              9,
              9
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": [
        0,
        0,
        0,
        0,
        1
      ]
    },
    {
      "name": "case_39_edge_single_carry",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              5
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              5
            ]
          }
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_40_edge_uneven",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              0
            ]
          },
          {
            "__type__": "ListNode",
            "value": [
              9,
              9
            ]
          }
        ]
      },
      "expected": [
        9,
        9
      ]
    }
  ]
}
```
