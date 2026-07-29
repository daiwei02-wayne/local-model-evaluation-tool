# 题目994 腐烂的橘子

在给定的 m x n 网格中，每个单元格可以有以下三个值之一：0 表示空单元格，1 表示新鲜橘子，2 表示腐烂橘子。每分钟腐烂橘子会让上下左右相邻的新鲜橘子腐烂。返回直到没有新鲜橘子所需的最小分钟数；如果不可能，返回 -1。

```json
{
  "id": 994,
  "title": "腐烂的橘子",
  "difficulty": "中等",
  "method": "question_994",
  "cases": [
    {
      "name": "case_01_official_four_minutes",
      "input": {
        "args": [
          [
            [
              2,
              1,
              1
            ],
            [
              1,
              1,
              0
            ],
            [
              0,
              1,
              1
            ]
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_02_unreachable",
      "input": {
        "args": [
          [
            [
              2,
              1,
              1
            ],
            [
              0,
              1,
              1
            ],
            [
              1,
              0,
              1
            ]
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_03_no_fresh",
      "input": {
        "args": [
          [
            [
              0,
              2
            ]
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_04_single_fresh_no_rotten",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_05_single_rotten",
      "input": {
        "args": [
          [
            [
              2
            ]
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_06_all_empty",
      "input": {
        "args": [
          [
            [
              0,
              0
            ],
            [
              0,
              0
            ]
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_07_one_row_spread",
      "input": {
        "args": [
          [
            [
              2,
              1,
              1,
              1,
              1
            ]
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_08_one_col_spread",
      "input": {
        "args": [
          [
            [
              2
            ],
            [
              1
            ],
            [
              1
            ],
            [
              1
            ]
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_09_multi_source",
      "input": {
        "args": [
          [
            [
              2,
              1,
              1
            ],
            [
              1,
              1,
              1
            ],
            [
              1,
              1,
              2
            ]
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_10_blocked_by_empty",
      "input": {
        "args": [
          [
            [
              2,
              0,
              1
            ],
            [
              0,
              1,
              0
            ],
            [
              1,
              0,
              2
            ]
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_11_edge_line",
      "input": {
        "args": [
          [
            [
              2,
              1,
              1,
              1
            ]
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_12_official_four_minutes",
      "input": {
        "args": [
          [
            [
              2,
              1,
              1
            ],
            [
              1,
              1,
              0
            ],
            [
              0,
              1,
              1
            ]
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_13_unreachable",
      "input": {
        "args": [
          [
            [
              2,
              1,
              1
            ],
            [
              0,
              1,
              1
            ],
            [
              1,
              0,
              1
            ]
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_14_no_fresh",
      "input": {
        "args": [
          [
            [
              0,
              2
            ]
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_15_single_fresh_no_rotten",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_16_single_rotten",
      "input": {
        "args": [
          [
            [
              2
            ]
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_17_all_empty",
      "input": {
        "args": [
          [
            [
              0,
              0
            ],
            [
              0,
              0
            ]
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_18_one_row_spread",
      "input": {
        "args": [
          [
            [
              2,
              1,
              1,
              1,
              1
            ]
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_19_one_col_spread",
      "input": {
        "args": [
          [
            [
              2
            ],
            [
              1
            ],
            [
              1
            ],
            [
              1
            ]
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_20_multi_source",
      "input": {
        "args": [
          [
            [
              2,
              1,
              1
            ],
            [
              1,
              1,
              1
            ],
            [
              1,
              1,
              2
            ]
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_21_blocked_by_empty",
      "input": {
        "args": [
          [
            [
              2,
              0,
              1
            ],
            [
              0,
              1,
              0
            ],
            [
              1,
              0,
              2
            ]
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_22_edge_line",
      "input": {
        "args": [
          [
            [
              2,
              1,
              1,
              1
            ]
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_23_official_four_minutes",
      "input": {
        "args": [
          [
            [
              2,
              1,
              1
            ],
            [
              1,
              1,
              0
            ],
            [
              0,
              1,
              1
            ]
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_24_unreachable",
      "input": {
        "args": [
          [
            [
              2,
              1,
              1
            ],
            [
              0,
              1,
              1
            ],
            [
              1,
              0,
              1
            ]
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_25_no_fresh",
      "input": {
        "args": [
          [
            [
              0,
              2
            ]
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_26_single_fresh_no_rotten",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_27_single_rotten",
      "input": {
        "args": [
          [
            [
              2
            ]
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_28_all_empty",
      "input": {
        "args": [
          [
            [
              0,
              0
            ],
            [
              0,
              0
            ]
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_29_one_row_spread",
      "input": {
        "args": [
          [
            [
              2,
              1,
              1,
              1,
              1
            ]
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_30_one_col_spread",
      "input": {
        "args": [
          [
            [
              2
            ],
            [
              1
            ],
            [
              1
            ],
            [
              1
            ]
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_31_multi_source",
      "input": {
        "args": [
          [
            [
              2,
              1,
              1
            ],
            [
              1,
              1,
              1
            ],
            [
              1,
              1,
              2
            ]
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_32_blocked_by_empty",
      "input": {
        "args": [
          [
            [
              2,
              0,
              1
            ],
            [
              0,
              1,
              0
            ],
            [
              1,
              0,
              2
            ]
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_33_edge_line",
      "input": {
        "args": [
          [
            [
              2,
              1,
              1,
              1
            ]
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_34_official_four_minutes",
      "input": {
        "args": [
          [
            [
              2,
              1,
              1
            ],
            [
              1,
              1,
              0
            ],
            [
              0,
              1,
              1
            ]
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_35_unreachable",
      "input": {
        "args": [
          [
            [
              2,
              1,
              1
            ],
            [
              0,
              1,
              1
            ],
            [
              1,
              0,
              1
            ]
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_36_no_fresh",
      "input": {
        "args": [
          [
            [
              0,
              2
            ]
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_37_single_fresh_no_rotten",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_38_single_rotten",
      "input": {
        "args": [
          [
            [
              2
            ]
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_39_all_empty",
      "input": {
        "args": [
          [
            [
              0,
              0
            ],
            [
              0,
              0
            ]
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_40_one_row_spread",
      "input": {
        "args": [
          [
            [
              2,
              1,
              1,
              1,
              1
            ]
          ]
        ]
      },
      "expected": 4
    }
  ]
}
```
