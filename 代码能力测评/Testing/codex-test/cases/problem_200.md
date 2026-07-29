# 题目200 岛屿数量

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个由 `'1'`（陆地）和 `'0'`（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
示例 1：
输入：grid = [  ["1","1","1","1","0"],  ["1","1","0","1","0"],  ["1","1","0","0","0"],  ["0","0","0","0","0"]]输出：1
示例 2：
输入：grid = [  ["1","1","0","0","0"],  ["1","1","0","0","0"],  ["0","0","1","0","0"],  ["0","0","0","1","1"]]输出：3
提示：
`m == grid.length`
`n == grid[i].length`
`1 <= m, n <= 300`
`grid[i][j]` 的值为 `'0'` 或 `'1'`

```json
{
  "id": 200,
  "title": "岛屿数量",
  "difficulty": "中等",
  "method": "question_200",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            [
              "1",
              "1",
              "1",
              "1",
              "0"
            ],
            [
              "1",
              "1",
              "0",
              "1",
              "0"
            ],
            [
              "1",
              "1",
              "0",
              "0",
              "0"
            ],
            [
              "0",
              "0",
              "0",
              "0",
              "0"
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_02_edge_water_only",
      "input": {
        "args": [
          [
            [
              "0"
            ]
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_03_edge_one_island",
      "input": {
        "args": [
          [
            [
              "1"
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_04_edge_two_islands_row",
      "input": {
        "args": [
          [
            [
              "1",
              "0",
              "1"
            ]
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          [
            [
              "1",
              "1",
              "1",
              "1",
              "0"
            ],
            [
              "1",
              "1",
              "0",
              "1",
              "0"
            ],
            [
              "1",
              "1",
              "0",
              "0",
              "0"
            ],
            [
              "0",
              "0",
              "0",
              "0",
              "0"
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_06_edge_water_only",
      "input": {
        "args": [
          [
            [
              "0"
            ]
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_07_edge_one_island",
      "input": {
        "args": [
          [
            [
              "1"
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_08_edge_two_islands_row",
      "input": {
        "args": [
          [
            [
              "1",
              "0",
              "1"
            ]
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          [
            [
              "1",
              "1",
              "1",
              "1",
              "0"
            ],
            [
              "1",
              "1",
              "0",
              "1",
              "0"
            ],
            [
              "1",
              "1",
              "0",
              "0",
              "0"
            ],
            [
              "0",
              "0",
              "0",
              "0",
              "0"
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_10_edge_water_only",
      "input": {
        "args": [
          [
            [
              "0"
            ]
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_11_edge_one_island",
      "input": {
        "args": [
          [
            [
              "1"
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_12_edge_two_islands_row",
      "input": {
        "args": [
          [
            [
              "1",
              "0",
              "1"
            ]
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [
            [
              "1",
              "1",
              "1",
              "1",
              "0"
            ],
            [
              "1",
              "1",
              "0",
              "1",
              "0"
            ],
            [
              "1",
              "1",
              "0",
              "0",
              "0"
            ],
            [
              "0",
              "0",
              "0",
              "0",
              "0"
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_14_edge_water_only",
      "input": {
        "args": [
          [
            [
              "0"
            ]
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_15_edge_one_island",
      "input": {
        "args": [
          [
            [
              "1"
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_16_edge_two_islands_row",
      "input": {
        "args": [
          [
            [
              "1",
              "0",
              "1"
            ]
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            [
              "1",
              "1",
              "1",
              "1",
              "0"
            ],
            [
              "1",
              "1",
              "0",
              "1",
              "0"
            ],
            [
              "1",
              "1",
              "0",
              "0",
              "0"
            ],
            [
              "0",
              "0",
              "0",
              "0",
              "0"
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_18_edge_water_only",
      "input": {
        "args": [
          [
            [
              "0"
            ]
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_19_edge_one_island",
      "input": {
        "args": [
          [
            [
              "1"
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_20_edge_two_islands_row",
      "input": {
        "args": [
          [
            [
              "1",
              "0",
              "1"
            ]
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            [
              "1",
              "1",
              "1",
              "1",
              "0"
            ],
            [
              "1",
              "1",
              "0",
              "1",
              "0"
            ],
            [
              "1",
              "1",
              "0",
              "0",
              "0"
            ],
            [
              "0",
              "0",
              "0",
              "0",
              "0"
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_22_edge_water_only",
      "input": {
        "args": [
          [
            [
              "0"
            ]
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_23_edge_one_island",
      "input": {
        "args": [
          [
            [
              "1"
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_24_edge_two_islands_row",
      "input": {
        "args": [
          [
            [
              "1",
              "0",
              "1"
            ]
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            [
              "1",
              "1",
              "1",
              "1",
              "0"
            ],
            [
              "1",
              "1",
              "0",
              "1",
              "0"
            ],
            [
              "1",
              "1",
              "0",
              "0",
              "0"
            ],
            [
              "0",
              "0",
              "0",
              "0",
              "0"
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_26_edge_water_only",
      "input": {
        "args": [
          [
            [
              "0"
            ]
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_27_edge_one_island",
      "input": {
        "args": [
          [
            [
              "1"
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_28_edge_two_islands_row",
      "input": {
        "args": [
          [
            [
              "1",
              "0",
              "1"
            ]
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          [
            [
              "1",
              "1",
              "1",
              "1",
              "0"
            ],
            [
              "1",
              "1",
              "0",
              "1",
              "0"
            ],
            [
              "1",
              "1",
              "0",
              "0",
              "0"
            ],
            [
              "0",
              "0",
              "0",
              "0",
              "0"
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_30_edge_water_only",
      "input": {
        "args": [
          [
            [
              "0"
            ]
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_31_edge_one_island",
      "input": {
        "args": [
          [
            [
              "1"
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_32_edge_two_islands_row",
      "input": {
        "args": [
          [
            [
              "1",
              "0",
              "1"
            ]
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          [
            [
              "1",
              "1",
              "1",
              "1",
              "0"
            ],
            [
              "1",
              "1",
              "0",
              "1",
              "0"
            ],
            [
              "1",
              "1",
              "0",
              "0",
              "0"
            ],
            [
              "0",
              "0",
              "0",
              "0",
              "0"
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_34_edge_water_only",
      "input": {
        "args": [
          [
            [
              "0"
            ]
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_35_edge_one_island",
      "input": {
        "args": [
          [
            [
              "1"
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_36_edge_two_islands_row",
      "input": {
        "args": [
          [
            [
              "1",
              "0",
              "1"
            ]
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            [
              "1",
              "1",
              "1",
              "1",
              "0"
            ],
            [
              "1",
              "1",
              "0",
              "1",
              "0"
            ],
            [
              "1",
              "1",
              "0",
              "0",
              "0"
            ],
            [
              "0",
              "0",
              "0",
              "0",
              "0"
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_38_edge_water_only",
      "input": {
        "args": [
          [
            [
              "0"
            ]
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_39_edge_one_island",
      "input": {
        "args": [
          [
            [
              "1"
            ]
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_40_edge_two_islands_row",
      "input": {
        "args": [
          [
            [
              "1",
              "0",
              "1"
            ]
          ]
        ]
      },
      "expected": 2
    }
  ]
}
```
