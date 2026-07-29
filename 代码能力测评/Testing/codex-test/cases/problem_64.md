# 题目64 最小路径和

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一个包含非负整数的 `_m_ x _n_` 网格 `grid` ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
示例 1：
题目配图：
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]输出：7解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：
输入：grid = [[1,2,3],[4,5,6]]输出：12
提示：
`m == grid.length`
`n == grid[i].length`
`1 <= m, n <= 200`
`0 <= grid[i][j] <= 100`

```json
{
  "id": 64,
  "title": "最小路径和",
  "difficulty": "中等",
  "method": "question_64",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            [
              1,
              3,
              1
            ],
            [
              1,
              5,
              1
            ],
            [
              4,
              2,
              1
            ]
          ]
        ]
      },
      "expected": 7
    },
    {
      "name": "case_02_edge_one_cell",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_03_edge_one_row",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ]
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_04_edge_one_col",
      "input": {
        "args": [
          [
            [
              1
            ],
            [
              2
            ],
            [
              3
            ]
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          [
            [
              1,
              3,
              1
            ],
            [
              1,
              5,
              1
            ],
            [
              4,
              2,
              1
            ]
          ]
        ]
      },
      "expected": 7
    },
    {
      "name": "case_06_edge_one_cell",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_07_edge_one_row",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ]
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_08_edge_one_col",
      "input": {
        "args": [
          [
            [
              1
            ],
            [
              2
            ],
            [
              3
            ]
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          [
            [
              1,
              3,
              1
            ],
            [
              1,
              5,
              1
            ],
            [
              4,
              2,
              1
            ]
          ]
        ]
      },
      "expected": 7
    },
    {
      "name": "case_10_edge_one_cell",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_11_edge_one_row",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ]
          ]
        ]
      },
      "expected": 6
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
              2
            ],
            [
              3
            ]
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [
            [
              1,
              3,
              1
            ],
            [
              1,
              5,
              1
            ],
            [
              4,
              2,
              1
            ]
          ]
        ]
      },
      "expected": 7
    },
    {
      "name": "case_14_edge_one_cell",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_15_edge_one_row",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ]
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_16_edge_one_col",
      "input": {
        "args": [
          [
            [
              1
            ],
            [
              2
            ],
            [
              3
            ]
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            [
              1,
              3,
              1
            ],
            [
              1,
              5,
              1
            ],
            [
              4,
              2,
              1
            ]
          ]
        ]
      },
      "expected": 7
    },
    {
      "name": "case_18_edge_one_cell",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_19_edge_one_row",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ]
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_20_edge_one_col",
      "input": {
        "args": [
          [
            [
              1
            ],
            [
              2
            ],
            [
              3
            ]
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            [
              1,
              3,
              1
            ],
            [
              1,
              5,
              1
            ],
            [
              4,
              2,
              1
            ]
          ]
        ]
      },
      "expected": 7
    },
    {
      "name": "case_22_edge_one_cell",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_23_edge_one_row",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ]
          ]
        ]
      },
      "expected": 6
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
              2
            ],
            [
              3
            ]
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            [
              1,
              3,
              1
            ],
            [
              1,
              5,
              1
            ],
            [
              4,
              2,
              1
            ]
          ]
        ]
      },
      "expected": 7
    },
    {
      "name": "case_26_edge_one_cell",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_27_edge_one_row",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ]
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_28_edge_one_col",
      "input": {
        "args": [
          [
            [
              1
            ],
            [
              2
            ],
            [
              3
            ]
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          [
            [
              1,
              3,
              1
            ],
            [
              1,
              5,
              1
            ],
            [
              4,
              2,
              1
            ]
          ]
        ]
      },
      "expected": 7
    },
    {
      "name": "case_30_edge_one_cell",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_31_edge_one_row",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ]
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_32_edge_one_col",
      "input": {
        "args": [
          [
            [
              1
            ],
            [
              2
            ],
            [
              3
            ]
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          [
            [
              1,
              3,
              1
            ],
            [
              1,
              5,
              1
            ],
            [
              4,
              2,
              1
            ]
          ]
        ]
      },
      "expected": 7
    },
    {
      "name": "case_34_edge_one_cell",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_35_edge_one_row",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ]
          ]
        ]
      },
      "expected": 6
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
              2
            ],
            [
              3
            ]
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            [
              1,
              3,
              1
            ],
            [
              1,
              5,
              1
            ],
            [
              4,
              2,
              1
            ]
          ]
        ]
      },
      "expected": 7
    },
    {
      "name": "case_38_edge_one_cell",
      "input": {
        "args": [
          [
            [
              1
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_39_edge_one_row",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ]
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_40_edge_one_col",
      "input": {
        "args": [
          [
            [
              1
            ],
            [
              2
            ],
            [
              3
            ]
          ]
        ]
      },
      "expected": 6
    }
  ]
}
```
