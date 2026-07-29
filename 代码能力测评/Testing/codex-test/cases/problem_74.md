# 题目74 搜索二维矩阵

来源：LeetCode 热题 100（https://leetcode.cn/studyplan/top-100-liked/）

```json
{
  "id": 74,
  "title": "搜索二维矩阵",
  "difficulty": "中等",
  "method": "question_74",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            [
              1,
              3,
              5,
              7
            ],
            [
              10,
              11,
              16,
              20
            ],
            [
              23,
              30,
              34,
              60
            ]
          ],
          3
        ]
      },
      "expected": true
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            [
              1,
              3,
              5,
              7
            ],
            [
              10,
              11,
              16,
              20
            ],
            [
              23,
              30,
              34,
              60
            ]
          ],
          13
        ]
      },
      "expected": false
    },
    {
      "name": "case_03_base",
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
      "name": "case_04_base",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          2
        ]
      },
      "expected": false
    },
    {
      "name": "case_05_edge_one_row_hit",
      "input": {
        "args": [
          [
            [
              1,
              3
            ]
          ],
          3
        ]
      },
      "expected": true
    },
    {
      "name": "case_06_edge_one_col_missing",
      "input": {
        "args": [
          [
            [
              1
            ],
            [
              3
            ]
          ],
          2
        ]
      },
      "expected": false
    },
    {
      "name": "case_07_edge_before_first",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ]
          ],
          0
        ]
      },
      "expected": false
    },
    {
      "name": "case_08_base",
      "input": {
        "args": [
          [
            [
              1,
              3,
              5,
              7
            ],
            [
              10,
              11,
              16,
              20
            ],
            [
              23,
              30,
              34,
              60
            ]
          ],
          3
        ]
      },
      "expected": true
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          [
            [
              1,
              3,
              5,
              7
            ],
            [
              10,
              11,
              16,
              20
            ],
            [
              23,
              30,
              34,
              60
            ]
          ],
          13
        ]
      },
      "expected": false
    },
    {
      "name": "case_10_base",
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
      "name": "case_11_base",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          2
        ]
      },
      "expected": false
    },
    {
      "name": "case_12_edge_one_row_hit",
      "input": {
        "args": [
          [
            [
              1,
              3
            ]
          ],
          3
        ]
      },
      "expected": true
    },
    {
      "name": "case_13_edge_one_col_missing",
      "input": {
        "args": [
          [
            [
              1
            ],
            [
              3
            ]
          ],
          2
        ]
      },
      "expected": false
    },
    {
      "name": "case_14_edge_before_first",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ]
          ],
          0
        ]
      },
      "expected": false
    },
    {
      "name": "case_15_base",
      "input": {
        "args": [
          [
            [
              1,
              3,
              5,
              7
            ],
            [
              10,
              11,
              16,
              20
            ],
            [
              23,
              30,
              34,
              60
            ]
          ],
          3
        ]
      },
      "expected": true
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            [
              1,
              3,
              5,
              7
            ],
            [
              10,
              11,
              16,
              20
            ],
            [
              23,
              30,
              34,
              60
            ]
          ],
          13
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
              1
            ]
          ],
          1
        ]
      },
      "expected": true
    },
    {
      "name": "case_18_base",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          2
        ]
      },
      "expected": false
    },
    {
      "name": "case_19_edge_one_row_hit",
      "input": {
        "args": [
          [
            [
              1,
              3
            ]
          ],
          3
        ]
      },
      "expected": true
    },
    {
      "name": "case_20_edge_one_col_missing",
      "input": {
        "args": [
          [
            [
              1
            ],
            [
              3
            ]
          ],
          2
        ]
      },
      "expected": false
    },
    {
      "name": "case_21_edge_before_first",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ]
          ],
          0
        ]
      },
      "expected": false
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            [
              1,
              3,
              5,
              7
            ],
            [
              10,
              11,
              16,
              20
            ],
            [
              23,
              30,
              34,
              60
            ]
          ],
          3
        ]
      },
      "expected": true
    },
    {
      "name": "case_23_base",
      "input": {
        "args": [
          [
            [
              1,
              3,
              5,
              7
            ],
            [
              10,
              11,
              16,
              20
            ],
            [
              23,
              30,
              34,
              60
            ]
          ],
          13
        ]
      },
      "expected": false
    },
    {
      "name": "case_24_base",
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
      "name": "case_25_base",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          2
        ]
      },
      "expected": false
    },
    {
      "name": "case_26_edge_one_row_hit",
      "input": {
        "args": [
          [
            [
              1,
              3
            ]
          ],
          3
        ]
      },
      "expected": true
    },
    {
      "name": "case_27_edge_one_col_missing",
      "input": {
        "args": [
          [
            [
              1
            ],
            [
              3
            ]
          ],
          2
        ]
      },
      "expected": false
    },
    {
      "name": "case_28_edge_before_first",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
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
              3,
              5,
              7
            ],
            [
              10,
              11,
              16,
              20
            ],
            [
              23,
              30,
              34,
              60
            ]
          ],
          3
        ]
      },
      "expected": true
    },
    {
      "name": "case_30_base",
      "input": {
        "args": [
          [
            [
              1,
              3,
              5,
              7
            ],
            [
              10,
              11,
              16,
              20
            ],
            [
              23,
              30,
              34,
              60
            ]
          ],
          13
        ]
      },
      "expected": false
    },
    {
      "name": "case_31_base",
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
      "name": "case_32_base",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          2
        ]
      },
      "expected": false
    },
    {
      "name": "case_33_edge_one_row_hit",
      "input": {
        "args": [
          [
            [
              1,
              3
            ]
          ],
          3
        ]
      },
      "expected": true
    },
    {
      "name": "case_34_edge_one_col_missing",
      "input": {
        "args": [
          [
            [
              1
            ],
            [
              3
            ]
          ],
          2
        ]
      },
      "expected": false
    },
    {
      "name": "case_35_edge_before_first",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3
            ]
          ],
          0
        ]
      },
      "expected": false
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          [
            [
              1,
              3,
              5,
              7
            ],
            [
              10,
              11,
              16,
              20
            ],
            [
              23,
              30,
              34,
              60
            ]
          ],
          3
        ]
      },
      "expected": true
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            [
              1,
              3,
              5,
              7
            ],
            [
              10,
              11,
              16,
              20
            ],
            [
              23,
              30,
              34,
              60
            ]
          ],
          13
        ]
      },
      "expected": false
    },
    {
      "name": "case_38_base",
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
      "name": "case_39_base",
      "input": {
        "args": [
          [
            [
              1
            ]
          ],
          2
        ]
      },
      "expected": false
    },
    {
      "name": "case_40_edge_one_row_hit",
      "input": {
        "args": [
          [
            [
              1,
              3
            ]
          ],
          3
        ]
      },
      "expected": true
    }
  ]
}
```
