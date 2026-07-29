# 题目23 合并K个升序链表

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。
示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]输出：[1,1,2,3,4,4,5,6]解释：链表数组如下：[  1->4->5,  1->3->4,  2->6]将它们合并到一个有序链表中得到。1->1->2->3->4->4->5->6
示例 2：
输入：lists = []输出：[]
示例 3：
输入：lists = [[]]输出：[]
提示：
`k == lists.length`
`0 <= k <= 10^4`
`0 <= lists[i].length <= 500`
`-10^4 <= lists[i][j] <= 10^4`
`lists[i]` 按 升序 排列
`lists[i].length` 的总和不超过 `10^4`

```json
{
  "id": 23,
  "title": "合并K个升序链表",
  "difficulty": "困难",
  "method": "question_23",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
            "value": [
              [
                1,
                4,
                5
              ],
              [
                1,
                3,
                4
              ],
              [
                2,
                6
              ]
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
          4,
          5,
          6
        ]
      }
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
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
      "name": "case_03_edge_empty_lists",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
            "value": [
              [],
              [
                1
              ]
            ]
          }
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_04_edge_single_nodes",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
            "value": [
              [
                1
              ],
              [
                0
              ]
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
      "name": "case_05_edge_no_lists",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
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
            "__type__": "ListNodeArray",
            "value": [
              [
                1,
                4,
                5
              ],
              [
                1,
                3,
                4
              ],
              [
                2,
                6
              ]
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
          4,
          5,
          6
        ]
      }
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
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
      "name": "case_08_edge_empty_lists",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
            "value": [
              [],
              [
                1
              ]
            ]
          }
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_09_edge_single_nodes",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
            "value": [
              [
                1
              ],
              [
                0
              ]
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
      "name": "case_10_edge_no_lists",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
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
            "__type__": "ListNodeArray",
            "value": [
              [
                1,
                4,
                5
              ],
              [
                1,
                3,
                4
              ],
              [
                2,
                6
              ]
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
          4,
          5,
          6
        ]
      }
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
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
      "name": "case_13_edge_empty_lists",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
            "value": [
              [],
              [
                1
              ]
            ]
          }
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_14_edge_single_nodes",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
            "value": [
              [
                1
              ],
              [
                0
              ]
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
      "name": "case_15_edge_no_lists",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
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
            "__type__": "ListNodeArray",
            "value": [
              [
                1,
                4,
                5
              ],
              [
                1,
                3,
                4
              ],
              [
                2,
                6
              ]
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
          4,
          5,
          6
        ]
      }
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
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
      "name": "case_18_edge_empty_lists",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
            "value": [
              [],
              [
                1
              ]
            ]
          }
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_19_edge_single_nodes",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
            "value": [
              [
                1
              ],
              [
                0
              ]
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
      "name": "case_20_edge_no_lists",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
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
            "__type__": "ListNodeArray",
            "value": [
              [
                1,
                4,
                5
              ],
              [
                1,
                3,
                4
              ],
              [
                2,
                6
              ]
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
          4,
          5,
          6
        ]
      }
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
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
      "name": "case_23_edge_empty_lists",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
            "value": [
              [],
              [
                1
              ]
            ]
          }
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_24_edge_single_nodes",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
            "value": [
              [
                1
              ],
              [
                0
              ]
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
      "name": "case_25_edge_no_lists",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
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
            "__type__": "ListNodeArray",
            "value": [
              [
                1,
                4,
                5
              ],
              [
                1,
                3,
                4
              ],
              [
                2,
                6
              ]
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
          4,
          5,
          6
        ]
      }
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
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
      "name": "case_28_edge_empty_lists",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
            "value": [
              [],
              [
                1
              ]
            ]
          }
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_29_edge_single_nodes",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
            "value": [
              [
                1
              ],
              [
                0
              ]
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
      "name": "case_30_edge_no_lists",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
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
            "__type__": "ListNodeArray",
            "value": [
              [
                1,
                4,
                5
              ],
              [
                1,
                3,
                4
              ],
              [
                2,
                6
              ]
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
          4,
          5,
          6
        ]
      }
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
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
      "name": "case_33_edge_empty_lists",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
            "value": [
              [],
              [
                1
              ]
            ]
          }
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_34_edge_single_nodes",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
            "value": [
              [
                1
              ],
              [
                0
              ]
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
      "name": "case_35_edge_no_lists",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
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
            "__type__": "ListNodeArray",
            "value": [
              [
                1,
                4,
                5
              ],
              [
                1,
                3,
                4
              ],
              [
                2,
                6
              ]
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
          4,
          5,
          6
        ]
      }
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
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
      "name": "case_38_edge_empty_lists",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
            "value": [
              [],
              [
                1
              ]
            ]
          }
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_39_edge_single_nodes",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
            "value": [
              [
                1
              ],
              [
                0
              ]
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
      "name": "case_40_edge_no_lists",
      "input": {
        "args": [
          {
            "__type__": "ListNodeArray",
            "value": []
          }
        ]
      },
      "expected": null
    }
  ]
}
```
