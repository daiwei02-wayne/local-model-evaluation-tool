# 题目240 搜索二维矩阵 II

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

编写一个高效的算法来搜索 `_m_ x _n_` 矩阵 `matrix` 中的一个目标值 `target` 。该矩阵具有以下特性：
每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例 1：
题目配图：
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5输出：true
示例 2：
题目配图：
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20输出：false
提示：
`m == matrix.length`
`n == matrix[i].length`
`1 <= n, m <= 300`
-10<sup>9</sup> <= matrix[i][j] <= 10<sup>9</sup>
每行的所有元素从左到右升序排列
每列的所有元素从上到下升序排列
-10<sup>9</sup> <= target <= 10<sup>9</sup>

```json
{
  "id": 240,
  "title": "搜索二维矩阵 II",
  "difficulty": "中等",
  "method": "question_240",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            [
              1,
              4,
              7,
              11,
              15
            ],
            [
              2,
              5,
              8,
              12,
              19
            ],
            [
              3,
              6,
              9,
              16,
              22
            ],
            [
              10,
              13,
              14,
              17,
              24
            ],
            [
              18,
              21,
              23,
              26,
              30
            ]
          ],
          5
        ]
      },
      "expected": true
    },
    {
      "name": "case_02_edge_empty_row",
      "input": {
        "args": [
          [
            []
          ],
          1
        ]
      },
      "expected": false
    },
    {
      "name": "case_03_edge_single_hit",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          1
        ]
      },
      "expected": true
    },
    {
      "name": "case_04_edge_single_miss",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          0
        ]
      },
      "expected": false
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          [
            [
              1,
              4,
              7,
              11,
              15
            ],
            [
              2,
              5,
              8,
              12,
              19
            ],
            [
              3,
              6,
              9,
              16,
              22
            ],
            [
              10,
              13,
              14,
              17,
              24
            ],
            [
              18,
              21,
              23,
              26,
              30
            ]
          ],
          5
        ]
      },
      "expected": true
    },
    {
      "name": "case_06_edge_empty_row",
      "input": {
        "args": [
          [
            []
          ],
          1
        ]
      },
      "expected": false
    },
    {
      "name": "case_07_edge_single_hit",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          1
        ]
      },
      "expected": true
    },
    {
      "name": "case_08_edge_single_miss",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          0
        ]
      },
      "expected": false
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          [
            [
              1,
              4,
              7,
              11,
              15
            ],
            [
              2,
              5,
              8,
              12,
              19
            ],
            [
              3,
              6,
              9,
              16,
              22
            ],
            [
              10,
              13,
              14,
              17,
              24
            ],
            [
              18,
              21,
              23,
              26,
              30
            ]
          ],
          5
        ]
      },
      "expected": true
    },
    {
      "name": "case_10_edge_empty_row",
      "input": {
        "args": [
          [
            []
          ],
          1
        ]
      },
      "expected": false
    },
    {
      "name": "case_11_edge_single_hit",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          1
        ]
      },
      "expected": true
    },
    {
      "name": "case_12_edge_single_miss",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          0
        ]
      },
      "expected": false
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [
            [
              1,
              4,
              7,
              11,
              15
            ],
            [
              2,
              5,
              8,
              12,
              19
            ],
            [
              3,
              6,
              9,
              16,
              22
            ],
            [
              10,
              13,
              14,
              17,
              24
            ],
            [
              18,
              21,
              23,
              26,
              30
            ]
          ],
          5
        ]
      },
      "expected": true
    },
    {
      "name": "case_14_edge_empty_row",
      "input": {
        "args": [
          [
            []
          ],
          1
        ]
      },
      "expected": false
    },
    {
      "name": "case_15_edge_single_hit",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          1
        ]
      },
      "expected": true
    },
    {
      "name": "case_16_edge_single_miss",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          0
        ]
      },
      "expected": false
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            [
              1,
              4,
              7,
              11,
              15
            ],
            [
              2,
              5,
              8,
              12,
              19
            ],
            [
              3,
              6,
              9,
              16,
              22
            ],
            [
              10,
              13,
              14,
              17,
              24
            ],
            [
              18,
              21,
              23,
              26,
              30
            ]
          ],
          5
        ]
      },
      "expected": true
    },
    {
      "name": "case_18_edge_empty_row",
      "input": {
        "args": [
          [
            []
          ],
          1
        ]
      },
      "expected": false
    },
    {
      "name": "case_19_edge_single_hit",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          1
        ]
      },
      "expected": true
    },
    {
      "name": "case_20_edge_single_miss",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          0
        ]
      },
      "expected": false
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            [
              1,
              4,
              7,
              11,
              15
            ],
            [
              2,
              5,
              8,
              12,
              19
            ],
            [
              3,
              6,
              9,
              16,
              22
            ],
            [
              10,
              13,
              14,
              17,
              24
            ],
            [
              18,
              21,
              23,
              26,
              30
            ]
          ],
          5
        ]
      },
      "expected": true
    },
    {
      "name": "case_22_edge_empty_row",
      "input": {
        "args": [
          [
            []
          ],
          1
        ]
      },
      "expected": false
    },
    {
      "name": "case_23_edge_single_hit",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          1
        ]
      },
      "expected": true
    },
    {
      "name": "case_24_edge_single_miss",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          0
        ]
      },
      "expected": false
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            [
              1,
              4,
              7,
              11,
              15
            ],
            [
              2,
              5,
              8,
              12,
              19
            ],
            [
              3,
              6,
              9,
              16,
              22
            ],
            [
              10,
              13,
              14,
              17,
              24
            ],
            [
              18,
              21,
              23,
              26,
              30
            ]
          ],
          5
        ]
      },
      "expected": true
    },
    {
      "name": "case_26_edge_empty_row",
      "input": {
        "args": [
          [
            []
          ],
          1
        ]
      },
      "expected": false
    },
    {
      "name": "case_27_edge_single_hit",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          1
        ]
      },
      "expected": true
    },
    {
      "name": "case_28_edge_single_miss",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          0
        ]
      },
      "expected": false
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          [
            [
              1,
              4,
              7,
              11,
              15
            ],
            [
              2,
              5,
              8,
              12,
              19
            ],
            [
              3,
              6,
              9,
              16,
              22
            ],
            [
              10,
              13,
              14,
              17,
              24
            ],
            [
              18,
              21,
              23,
              26,
              30
            ]
          ],
          5
        ]
      },
      "expected": true
    },
    {
      "name": "case_30_edge_empty_row",
      "input": {
        "args": [
          [
            []
          ],
          1
        ]
      },
      "expected": false
    },
    {
      "name": "case_31_edge_single_hit",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          1
        ]
      },
      "expected": true
    },
    {
      "name": "case_32_edge_single_miss",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          0
        ]
      },
      "expected": false
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          [
            [
              1,
              4,
              7,
              11,
              15
            ],
            [
              2,
              5,
              8,
              12,
              19
            ],
            [
              3,
              6,
              9,
              16,
              22
            ],
            [
              10,
              13,
              14,
              17,
              24
            ],
            [
              18,
              21,
              23,
              26,
              30
            ]
          ],
          5
        ]
      },
      "expected": true
    },
    {
      "name": "case_34_edge_empty_row",
      "input": {
        "args": [
          [
            []
          ],
          1
        ]
      },
      "expected": false
    },
    {
      "name": "case_35_edge_single_hit",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          1
        ]
      },
      "expected": true
    },
    {
      "name": "case_36_edge_single_miss",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          0
        ]
      },
      "expected": false
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            [
              1,
              4,
              7,
              11,
              15
            ],
            [
              2,
              5,
              8,
              12,
              19
            ],
            [
              3,
              6,
              9,
              16,
              22
            ],
            [
              10,
              13,
              14,
              17,
              24
            ],
            [
              18,
              21,
              23,
              26,
              30
            ]
          ],
          5
        ]
      },
      "expected": true
    },
    {
      "name": "case_38_edge_empty_row",
      "input": {
        "args": [
          [
            []
          ],
          1
        ]
      },
      "expected": false
    },
    {
      "name": "case_39_edge_single_hit",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          1
        ]
      },
      "expected": true
    },
    {
      "name": "case_40_edge_single_miss",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          0
        ]
      },
      "expected": false
    }
  ]
}
```
