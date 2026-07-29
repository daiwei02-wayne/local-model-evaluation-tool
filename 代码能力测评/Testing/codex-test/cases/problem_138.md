# 题目138 复制带随机指针的链表

给你一个长度为 n 的链表，每个节点包含一个额外的随机指针 random，该指针可以指向链表中的任意节点或空节点。请返回该链表的深拷贝。

用例中 `RandomNode` 使用 `[val, random_index]` 表示一个节点，其中 `random_index` 为随机指针指向的节点下标，`null` 表示空指针。

```json
{
  "id": 138,
  "title": "复制带随机指针的链表",
  "difficulty": "中等",
  "method": "question_138",
  "cases": [
    {
      "name": "case_01_official_complex",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                7,
                null
              ],
              [
                13,
                0
              ],
              [
                11,
                4
              ],
              [
                10,
                2
              ],
              [
                1,
                0
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            7,
            null
          ],
          [
            13,
            0
          ],
          [
            11,
            4
          ],
          [
            10,
            2
          ],
          [
            1,
            0
          ]
        ]
      }
    },
    {
      "name": "case_02_two_nodes_cycle_random",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                1,
                1
              ],
              [
                2,
                1
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            1,
            1
          ],
          [
            2,
            1
          ]
        ]
      }
    },
    {
      "name": "case_03_three_nodes_mixed",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                3,
                null
              ],
              [
                3,
                0
              ],
              [
                3,
                null
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            3,
            null
          ],
          [
            3,
            0
          ],
          [
            3,
            null
          ]
        ]
      }
    },
    {
      "name": "case_04_empty",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": []
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": []
      }
    },
    {
      "name": "case_05_single_null_random",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                1,
                null
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            1,
            null
          ]
        ]
      }
    },
    {
      "name": "case_06_single_self_random",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                1,
                0
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            1,
            0
          ]
        ]
      }
    },
    {
      "name": "case_07_forward_randoms",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                1,
                2
              ],
              [
                2,
                3
              ],
              [
                3,
                1
              ],
              [
                4,
                null
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            1,
            2
          ],
          [
            2,
            3
          ],
          [
            3,
            1
          ],
          [
            4,
            null
          ]
        ]
      }
    },
    {
      "name": "case_08_backward_randoms",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                5,
                null
              ],
              [
                6,
                0
              ],
              [
                7,
                1
              ],
              [
                8,
                2
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            5,
            null
          ],
          [
            6,
            0
          ],
          [
            7,
            1
          ],
          [
            8,
            2
          ]
        ]
      }
    },
    {
      "name": "case_09_all_to_head",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                9,
                0
              ],
              [
                8,
                0
              ],
              [
                7,
                0
              ],
              [
                6,
                0
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            9,
            0
          ],
          [
            8,
            0
          ],
          [
            7,
            0
          ],
          [
            6,
            0
          ]
        ]
      }
    },
    {
      "name": "case_10_all_to_tail",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                1,
                3
              ],
              [
                2,
                3
              ],
              [
                3,
                3
              ],
              [
                4,
                3
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            1,
            3
          ],
          [
            2,
            3
          ],
          [
            3,
            3
          ],
          [
            4,
            3
          ]
        ]
      }
    },
    {
      "name": "case_11_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": []
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_12_edge_self_random",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                1,
                0
              ]
            ]
          }
        ]
      },
      "expected": [
        [
          1,
          0
        ]
      ]
    },
    {
      "name": "case_13_edge_backward_random",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                1,
                null
              ],
              [
                2,
                0
              ]
            ]
          }
        ]
      },
      "expected": [
        [
          1,
          null
        ],
        [
          2,
          0
        ]
      ]
    },
    {
      "name": "case_14_official_complex",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                7,
                null
              ],
              [
                13,
                0
              ],
              [
                11,
                4
              ],
              [
                10,
                2
              ],
              [
                1,
                0
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            7,
            null
          ],
          [
            13,
            0
          ],
          [
            11,
            4
          ],
          [
            10,
            2
          ],
          [
            1,
            0
          ]
        ]
      }
    },
    {
      "name": "case_15_two_nodes_cycle_random",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                1,
                1
              ],
              [
                2,
                1
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            1,
            1
          ],
          [
            2,
            1
          ]
        ]
      }
    },
    {
      "name": "case_16_three_nodes_mixed",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                3,
                null
              ],
              [
                3,
                0
              ],
              [
                3,
                null
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            3,
            null
          ],
          [
            3,
            0
          ],
          [
            3,
            null
          ]
        ]
      }
    },
    {
      "name": "case_17_empty",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": []
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": []
      }
    },
    {
      "name": "case_18_single_null_random",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                1,
                null
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            1,
            null
          ]
        ]
      }
    },
    {
      "name": "case_19_single_self_random",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                1,
                0
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            1,
            0
          ]
        ]
      }
    },
    {
      "name": "case_20_forward_randoms",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                1,
                2
              ],
              [
                2,
                3
              ],
              [
                3,
                1
              ],
              [
                4,
                null
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            1,
            2
          ],
          [
            2,
            3
          ],
          [
            3,
            1
          ],
          [
            4,
            null
          ]
        ]
      }
    },
    {
      "name": "case_21_backward_randoms",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                5,
                null
              ],
              [
                6,
                0
              ],
              [
                7,
                1
              ],
              [
                8,
                2
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            5,
            null
          ],
          [
            6,
            0
          ],
          [
            7,
            1
          ],
          [
            8,
            2
          ]
        ]
      }
    },
    {
      "name": "case_22_all_to_head",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                9,
                0
              ],
              [
                8,
                0
              ],
              [
                7,
                0
              ],
              [
                6,
                0
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            9,
            0
          ],
          [
            8,
            0
          ],
          [
            7,
            0
          ],
          [
            6,
            0
          ]
        ]
      }
    },
    {
      "name": "case_23_all_to_tail",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                1,
                3
              ],
              [
                2,
                3
              ],
              [
                3,
                3
              ],
              [
                4,
                3
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            1,
            3
          ],
          [
            2,
            3
          ],
          [
            3,
            3
          ],
          [
            4,
            3
          ]
        ]
      }
    },
    {
      "name": "case_24_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": []
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_25_edge_self_random",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                1,
                0
              ]
            ]
          }
        ]
      },
      "expected": [
        [
          1,
          0
        ]
      ]
    },
    {
      "name": "case_26_edge_backward_random",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                1,
                null
              ],
              [
                2,
                0
              ]
            ]
          }
        ]
      },
      "expected": [
        [
          1,
          null
        ],
        [
          2,
          0
        ]
      ]
    },
    {
      "name": "case_27_official_complex",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                7,
                null
              ],
              [
                13,
                0
              ],
              [
                11,
                4
              ],
              [
                10,
                2
              ],
              [
                1,
                0
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            7,
            null
          ],
          [
            13,
            0
          ],
          [
            11,
            4
          ],
          [
            10,
            2
          ],
          [
            1,
            0
          ]
        ]
      }
    },
    {
      "name": "case_28_two_nodes_cycle_random",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                1,
                1
              ],
              [
                2,
                1
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            1,
            1
          ],
          [
            2,
            1
          ]
        ]
      }
    },
    {
      "name": "case_29_three_nodes_mixed",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                3,
                null
              ],
              [
                3,
                0
              ],
              [
                3,
                null
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            3,
            null
          ],
          [
            3,
            0
          ],
          [
            3,
            null
          ]
        ]
      }
    },
    {
      "name": "case_30_empty",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": []
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": []
      }
    },
    {
      "name": "case_31_single_null_random",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                1,
                null
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            1,
            null
          ]
        ]
      }
    },
    {
      "name": "case_32_single_self_random",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                1,
                0
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            1,
            0
          ]
        ]
      }
    },
    {
      "name": "case_33_forward_randoms",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                1,
                2
              ],
              [
                2,
                3
              ],
              [
                3,
                1
              ],
              [
                4,
                null
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            1,
            2
          ],
          [
            2,
            3
          ],
          [
            3,
            1
          ],
          [
            4,
            null
          ]
        ]
      }
    },
    {
      "name": "case_34_backward_randoms",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                5,
                null
              ],
              [
                6,
                0
              ],
              [
                7,
                1
              ],
              [
                8,
                2
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            5,
            null
          ],
          [
            6,
            0
          ],
          [
            7,
            1
          ],
          [
            8,
            2
          ]
        ]
      }
    },
    {
      "name": "case_35_all_to_head",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                9,
                0
              ],
              [
                8,
                0
              ],
              [
                7,
                0
              ],
              [
                6,
                0
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            9,
            0
          ],
          [
            8,
            0
          ],
          [
            7,
            0
          ],
          [
            6,
            0
          ]
        ]
      }
    },
    {
      "name": "case_36_all_to_tail",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                1,
                3
              ],
              [
                2,
                3
              ],
              [
                3,
                3
              ],
              [
                4,
                3
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            1,
            3
          ],
          [
            2,
            3
          ],
          [
            3,
            3
          ],
          [
            4,
            3
          ]
        ]
      }
    },
    {
      "name": "case_37_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": []
          }
        ]
      },
      "expected": null
    },
    {
      "name": "case_38_edge_self_random",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                1,
                0
              ]
            ]
          }
        ]
      },
      "expected": [
        [
          1,
          0
        ]
      ]
    },
    {
      "name": "case_39_edge_backward_random",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                1,
                null
              ],
              [
                2,
                0
              ]
            ]
          }
        ]
      },
      "expected": [
        [
          1,
          null
        ],
        [
          2,
          0
        ]
      ]
    },
    {
      "name": "case_40_official_complex",
      "input": {
        "args": [
          {
            "__type__": "RandomNode",
            "value": [
              [
                7,
                null
              ],
              [
                13,
                0
              ],
              [
                11,
                4
              ],
              [
                10,
                2
              ],
              [
                1,
                0
              ]
            ]
          }
        ]
      },
      "expected": {
        "__type__": "RandomNode",
        "value": [
          [
            7,
            null
          ],
          [
            13,
            0
          ],
          [
            11,
            4
          ],
          [
            10,
            2
          ],
          [
            1,
            0
          ]
        ]
      }
    }
  ]
}
```
