# 题目73 矩阵置零

来源：LeetCode 热题 100（https://leetcode.cn/studyplan/top-100-liked/）

```json
{
  "id": 73,
  "title": "矩阵置零",
  "difficulty": "中等",
  "method": "question_73",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            [
              1,
              1,
              1
            ],
            [
              1,
              0,
              1
            ],
            [
              1,
              1,
              1
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          0,
          1
        ],
        [
          0,
          0,
          0
        ],
        [
          1,
          0,
          1
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            [
              0,
              1,
              2,
              0
            ],
            [
              3,
              4,
              5,
              2
            ],
            [
              1,
              3,
              1,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          0,
          0,
          0,
          0
        ],
        [
          0,
          4,
          5,
          0
        ],
        [
          0,
          3,
          1,
          0
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_03_base",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expected": [
        [
          1
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_04_edge_single_zero",
      "input": {
        "args": [
          [
            [
              0
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
          0
        ]
      ]
    },
    {
      "name": "case_05_edge_one_row",
      "input": {
        "args": [
          [
            [
              1,
              0
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
          0,
          0
        ]
      ]
    },
    {
      "name": "case_06_edge_one_col",
      "input": {
        "args": [
          [
            [
              1
            ],
            [
              0
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
          0
        ],
        [
          0
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
              1,
              1
            ],
            [
              1,
              0,
              1
            ],
            [
              1,
              1,
              1
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          0,
          1
        ],
        [
          0,
          0,
          0
        ],
        [
          1,
          0,
          1
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_08_base",
      "input": {
        "args": [
          [
            [
              0,
              1,
              2,
              0
            ],
            [
              3,
              4,
              5,
              2
            ],
            [
              1,
              3,
              1,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          0,
          0,
          0,
          0
        ],
        [
          0,
          4,
          5,
          0
        ],
        [
          0,
          3,
          1,
          0
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expected": [
        [
          1
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_10_edge_single_zero",
      "input": {
        "args": [
          [
            [
              0
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
          0
        ]
      ]
    },
    {
      "name": "case_11_edge_one_row",
      "input": {
        "args": [
          [
            [
              1,
              0
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
          0,
          0
        ]
      ]
    },
    {
      "name": "case_12_edge_one_col",
      "input": {
        "args": [
          [
            [
              1
            ],
            [
              0
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
          0
        ],
        [
          0
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
              1,
              1
            ],
            [
              1,
              0,
              1
            ],
            [
              1,
              1,
              1
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          0,
          1
        ],
        [
          0,
          0,
          0
        ],
        [
          1,
          0,
          1
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_14_base",
      "input": {
        "args": [
          [
            [
              0,
              1,
              2,
              0
            ],
            [
              3,
              4,
              5,
              2
            ],
            [
              1,
              3,
              1,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          0,
          0,
          0,
          0
        ],
        [
          0,
          4,
          5,
          0
        ],
        [
          0,
          3,
          1,
          0
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_15_base",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expected": [
        [
          1
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_16_edge_single_zero",
      "input": {
        "args": [
          [
            [
              0
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
          0
        ]
      ]
    },
    {
      "name": "case_17_edge_one_row",
      "input": {
        "args": [
          [
            [
              1,
              0
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
          0,
          0
        ]
      ]
    },
    {
      "name": "case_18_edge_one_col",
      "input": {
        "args": [
          [
            [
              1
            ],
            [
              0
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
          0
        ],
        [
          0
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
              1,
              1
            ],
            [
              1,
              0,
              1
            ],
            [
              1,
              1,
              1
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          0,
          1
        ],
        [
          0,
          0,
          0
        ],
        [
          1,
          0,
          1
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_20_base",
      "input": {
        "args": [
          [
            [
              0,
              1,
              2,
              0
            ],
            [
              3,
              4,
              5,
              2
            ],
            [
              1,
              3,
              1,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          0,
          0,
          0,
          0
        ],
        [
          0,
          4,
          5,
          0
        ],
        [
          0,
          3,
          1,
          0
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expected": [
        [
          1
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_22_edge_single_zero",
      "input": {
        "args": [
          [
            [
              0
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
          0
        ]
      ]
    },
    {
      "name": "case_23_edge_one_row",
      "input": {
        "args": [
          [
            [
              1,
              0
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
          0,
          0
        ]
      ]
    },
    {
      "name": "case_24_edge_one_col",
      "input": {
        "args": [
          [
            [
              1
            ],
            [
              0
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
          0
        ],
        [
          0
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
              1,
              1
            ],
            [
              1,
              0,
              1
            ],
            [
              1,
              1,
              1
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          0,
          1
        ],
        [
          0,
          0,
          0
        ],
        [
          1,
          0,
          1
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            [
              0,
              1,
              2,
              0
            ],
            [
              3,
              4,
              5,
              2
            ],
            [
              1,
              3,
              1,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          0,
          0,
          0,
          0
        ],
        [
          0,
          4,
          5,
          0
        ],
        [
          0,
          3,
          1,
          0
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expected": [
        [
          1
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_28_edge_single_zero",
      "input": {
        "args": [
          [
            [
              0
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
          0
        ]
      ]
    },
    {
      "name": "case_29_edge_one_row",
      "input": {
        "args": [
          [
            [
              1,
              0
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
          0,
          0
        ]
      ]
    },
    {
      "name": "case_30_edge_one_col",
      "input": {
        "args": [
          [
            [
              1
            ],
            [
              0
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
          0
        ],
        [
          0
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
              1,
              1
            ],
            [
              1,
              0,
              1
            ],
            [
              1,
              1,
              1
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          0,
          1
        ],
        [
          0,
          0,
          0
        ],
        [
          1,
          0,
          1
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          [
            [
              0,
              1,
              2,
              0
            ],
            [
              3,
              4,
              5,
              2
            ],
            [
              1,
              3,
              1,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          0,
          0,
          0,
          0
        ],
        [
          0,
          4,
          5,
          0
        ],
        [
          0,
          3,
          1,
          0
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expected": [
        [
          1
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_34_edge_single_zero",
      "input": {
        "args": [
          [
            [
              0
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
          0
        ]
      ]
    },
    {
      "name": "case_35_edge_one_row",
      "input": {
        "args": [
          [
            [
              1,
              0
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
          0,
          0
        ]
      ]
    },
    {
      "name": "case_36_edge_one_col",
      "input": {
        "args": [
          [
            [
              1
            ],
            [
              0
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
          0
        ],
        [
          0
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
              1,
              1
            ],
            [
              1,
              0,
              1
            ],
            [
              1,
              1,
              1
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          0,
          1
        ],
        [
          0,
          0,
          0
        ],
        [
          1,
          0,
          1
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          [
            [
              0,
              1,
              2,
              0
            ],
            [
              3,
              4,
              5,
              2
            ],
            [
              1,
              3,
              1,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          0,
          0,
          0,
          0
        ],
        [
          0,
          4,
          5,
          0
        ],
        [
          0,
          3,
          1,
          0
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_39_base",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expected": [
        [
          1
        ]
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_40_edge_single_zero",
      "input": {
        "args": [
          [
            [
              0
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
          0
        ]
      ]
    }
  ]
}
```
