# 题目48 旋转图像

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一个 _n _× _n_ 的二维矩阵 `matrix` 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
示例 1：
题目配图：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]输出：[[7,4,1],[8,5,2],[9,6,3]]
示例 2：
题目配图：
输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
提示：
`n == matrix.length == matrix[i].length`
`1 <= n <= 20`
`-1000 <= matrix[i][j] <= 1000`

```json
{
  "id": 48,
  "title": "旋转图像",
  "difficulty": "中等",
  "method": "question_48",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              4,
              5,
              6
            ],
            [
              7,
              8,
              9
            ]
          ]
        ]
      },
      "expected": [
        [
          7,
          4,
          1
        ],
        [
          8,
          5,
          2
        ],
        [
          9,
          6,
          3
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_02_edge_one_by_one",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          1
        ]
      ]
    },
    {
      "name": "case_03_edge_two_by_two",
      "input": {
        "args": [
          [
            [
              1,
              2
            ],
            [
              3,
              4
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          3,
          1
        ],
        [
          4,
          2
        ]
      ]
    },
    {
      "name": "case_04_base",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              4,
              5,
              6
            ],
            [
              7,
              8,
              9
            ]
          ]
        ]
      },
      "expected": [
        [
          7,
          4,
          1
        ],
        [
          8,
          5,
          2
        ],
        [
          9,
          6,
          3
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_05_edge_one_by_one",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          1
        ]
      ]
    },
    {
      "name": "case_06_edge_two_by_two",
      "input": {
        "args": [
          [
            [
              1,
              2
            ],
            [
              3,
              4
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          3,
          1
        ],
        [
          4,
          2
        ]
      ]
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              4,
              5,
              6
            ],
            [
              7,
              8,
              9
            ]
          ]
        ]
      },
      "expected": [
        [
          7,
          4,
          1
        ],
        [
          8,
          5,
          2
        ],
        [
          9,
          6,
          3
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_08_edge_one_by_one",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          1
        ]
      ]
    },
    {
      "name": "case_09_edge_two_by_two",
      "input": {
        "args": [
          [
            [
              1,
              2
            ],
            [
              3,
              4
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          3,
          1
        ],
        [
          4,
          2
        ]
      ]
    },
    {
      "name": "case_10_base",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              4,
              5,
              6
            ],
            [
              7,
              8,
              9
            ]
          ]
        ]
      },
      "expected": [
        [
          7,
          4,
          1
        ],
        [
          8,
          5,
          2
        ],
        [
          9,
          6,
          3
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_11_edge_one_by_one",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          1
        ]
      ]
    },
    {
      "name": "case_12_edge_two_by_two",
      "input": {
        "args": [
          [
            [
              1,
              2
            ],
            [
              3,
              4
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          3,
          1
        ],
        [
          4,
          2
        ]
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              4,
              5,
              6
            ],
            [
              7,
              8,
              9
            ]
          ]
        ]
      },
      "expected": [
        [
          7,
          4,
          1
        ],
        [
          8,
          5,
          2
        ],
        [
          9,
          6,
          3
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_14_edge_one_by_one",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          1
        ]
      ]
    },
    {
      "name": "case_15_edge_two_by_two",
      "input": {
        "args": [
          [
            [
              1,
              2
            ],
            [
              3,
              4
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          3,
          1
        ],
        [
          4,
          2
        ]
      ]
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              4,
              5,
              6
            ],
            [
              7,
              8,
              9
            ]
          ]
        ]
      },
      "expected": [
        [
          7,
          4,
          1
        ],
        [
          8,
          5,
          2
        ],
        [
          9,
          6,
          3
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_17_edge_one_by_one",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          1
        ]
      ]
    },
    {
      "name": "case_18_edge_two_by_two",
      "input": {
        "args": [
          [
            [
              1,
              2
            ],
            [
              3,
              4
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          3,
          1
        ],
        [
          4,
          2
        ]
      ]
    },
    {
      "name": "case_19_base",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              4,
              5,
              6
            ],
            [
              7,
              8,
              9
            ]
          ]
        ]
      },
      "expected": [
        [
          7,
          4,
          1
        ],
        [
          8,
          5,
          2
        ],
        [
          9,
          6,
          3
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_20_edge_one_by_one",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          1
        ]
      ]
    },
    {
      "name": "case_21_edge_two_by_two",
      "input": {
        "args": [
          [
            [
              1,
              2
            ],
            [
              3,
              4
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          3,
          1
        ],
        [
          4,
          2
        ]
      ]
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              4,
              5,
              6
            ],
            [
              7,
              8,
              9
            ]
          ]
        ]
      },
      "expected": [
        [
          7,
          4,
          1
        ],
        [
          8,
          5,
          2
        ],
        [
          9,
          6,
          3
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_23_edge_one_by_one",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          1
        ]
      ]
    },
    {
      "name": "case_24_edge_two_by_two",
      "input": {
        "args": [
          [
            [
              1,
              2
            ],
            [
              3,
              4
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          3,
          1
        ],
        [
          4,
          2
        ]
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              4,
              5,
              6
            ],
            [
              7,
              8,
              9
            ]
          ]
        ]
      },
      "expected": [
        [
          7,
          4,
          1
        ],
        [
          8,
          5,
          2
        ],
        [
          9,
          6,
          3
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_26_edge_one_by_one",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          1
        ]
      ]
    },
    {
      "name": "case_27_edge_two_by_two",
      "input": {
        "args": [
          [
            [
              1,
              2
            ],
            [
              3,
              4
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          3,
          1
        ],
        [
          4,
          2
        ]
      ]
    },
    {
      "name": "case_28_base",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              4,
              5,
              6
            ],
            [
              7,
              8,
              9
            ]
          ]
        ]
      },
      "expected": [
        [
          7,
          4,
          1
        ],
        [
          8,
          5,
          2
        ],
        [
          9,
          6,
          3
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_29_edge_one_by_one",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          1
        ]
      ]
    },
    {
      "name": "case_30_edge_two_by_two",
      "input": {
        "args": [
          [
            [
              1,
              2
            ],
            [
              3,
              4
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          3,
          1
        ],
        [
          4,
          2
        ]
      ]
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              4,
              5,
              6
            ],
            [
              7,
              8,
              9
            ]
          ]
        ]
      },
      "expected": [
        [
          7,
          4,
          1
        ],
        [
          8,
          5,
          2
        ],
        [
          9,
          6,
          3
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_32_edge_one_by_one",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          1
        ]
      ]
    },
    {
      "name": "case_33_edge_two_by_two",
      "input": {
        "args": [
          [
            [
              1,
              2
            ],
            [
              3,
              4
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          3,
          1
        ],
        [
          4,
          2
        ]
      ]
    },
    {
      "name": "case_34_base",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              4,
              5,
              6
            ],
            [
              7,
              8,
              9
            ]
          ]
        ]
      },
      "expected": [
        [
          7,
          4,
          1
        ],
        [
          8,
          5,
          2
        ],
        [
          9,
          6,
          3
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_35_edge_one_by_one",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          1
        ]
      ]
    },
    {
      "name": "case_36_edge_two_by_two",
      "input": {
        "args": [
          [
            [
              1,
              2
            ],
            [
              3,
              4
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          3,
          1
        ],
        [
          4,
          2
        ]
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              4,
              5,
              6
            ],
            [
              7,
              8,
              9
            ]
          ]
        ]
      },
      "expected": [
        [
          7,
          4,
          1
        ],
        [
          8,
          5,
          2
        ],
        [
          9,
          6,
          3
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_38_edge_one_by_one",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          1
        ]
      ]
    },
    {
      "name": "case_39_edge_two_by_two",
      "input": {
        "args": [
          [
            [
              1,
              2
            ],
            [
              3,
              4
            ]
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        [
          3,
          1
        ],
        [
          4,
          2
        ]
      ]
    },
    {
      "name": "case_40_base",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              4,
              5,
              6
            ],
            [
              7,
              8,
              9
            ]
          ]
        ]
      },
      "expected": [
        [
          7,
          4,
          1
        ],
        [
          8,
          5,
          2
        ],
        [
          9,
          6,
          3
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    }
  ]
}
```
