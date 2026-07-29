# 题目54 螺旋矩阵

来源：LeetCode 热题 100（https://leetcode.cn/studyplan/top-100-liked/）

```json
{
  "id": 54,
  "title": "螺旋矩阵",
  "difficulty": "中等",
  "method": "question_54",
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
        1,
        2,
        3,
        6,
        9,
        8,
        7,
        4,
        5
      ]
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3,
              4
            ],
            [
              5,
              6,
              7,
              8
            ],
            [
              9,
              10,
              11,
              12
            ]
          ]
        ]
      },
      "expected": [
        1,
        2,
        3,
        4,
        8,
        12,
        11,
        10,
        9,
        5,
        6,
        7
      ]
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
        1
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
            ]
          ]
        ]
      },
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_05_edge_one_column",
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
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_06_edge_square_two",
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
      "expected": [
        1,
        2,
        4,
        3
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
        1,
        2,
        3,
        6,
        9,
        8,
        7,
        4,
        5
      ]
    },
    {
      "name": "case_08_base",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3,
              4
            ],
            [
              5,
              6,
              7,
              8
            ],
            [
              9,
              10,
              11,
              12
            ]
          ]
        ]
      },
      "expected": [
        1,
        2,
        3,
        4,
        8,
        12,
        11,
        10,
        9,
        5,
        6,
        7
      ]
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
        1
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
            ]
          ]
        ]
      },
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_11_edge_one_column",
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
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_12_edge_square_two",
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
      "expected": [
        1,
        2,
        4,
        3
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
        1,
        2,
        3,
        6,
        9,
        8,
        7,
        4,
        5
      ]
    },
    {
      "name": "case_14_base",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3,
              4
            ],
            [
              5,
              6,
              7,
              8
            ],
            [
              9,
              10,
              11,
              12
            ]
          ]
        ]
      },
      "expected": [
        1,
        2,
        3,
        4,
        8,
        12,
        11,
        10,
        9,
        5,
        6,
        7
      ]
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
        1
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
            ]
          ]
        ]
      },
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_17_edge_one_column",
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
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_18_edge_square_two",
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
      "expected": [
        1,
        2,
        4,
        3
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
        1,
        2,
        3,
        6,
        9,
        8,
        7,
        4,
        5
      ]
    },
    {
      "name": "case_20_base",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3,
              4
            ],
            [
              5,
              6,
              7,
              8
            ],
            [
              9,
              10,
              11,
              12
            ]
          ]
        ]
      },
      "expected": [
        1,
        2,
        3,
        4,
        8,
        12,
        11,
        10,
        9,
        5,
        6,
        7
      ]
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
        1
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
            ]
          ]
        ]
      },
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_23_edge_one_column",
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
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_24_edge_square_two",
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
      "expected": [
        1,
        2,
        4,
        3
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
        1,
        2,
        3,
        6,
        9,
        8,
        7,
        4,
        5
      ]
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3,
              4
            ],
            [
              5,
              6,
              7,
              8
            ],
            [
              9,
              10,
              11,
              12
            ]
          ]
        ]
      },
      "expected": [
        1,
        2,
        3,
        4,
        8,
        12,
        11,
        10,
        9,
        5,
        6,
        7
      ]
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
        1
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
            ]
          ]
        ]
      },
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_29_edge_one_column",
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
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_30_edge_square_two",
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
      "expected": [
        1,
        2,
        4,
        3
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
        1,
        2,
        3,
        6,
        9,
        8,
        7,
        4,
        5
      ]
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3,
              4
            ],
            [
              5,
              6,
              7,
              8
            ],
            [
              9,
              10,
              11,
              12
            ]
          ]
        ]
      },
      "expected": [
        1,
        2,
        3,
        4,
        8,
        12,
        11,
        10,
        9,
        5,
        6,
        7
      ]
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
        1
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
            ]
          ]
        ]
      },
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_35_edge_one_column",
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
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_36_edge_square_two",
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
      "expected": [
        1,
        2,
        4,
        3
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
        1,
        2,
        3,
        6,
        9,
        8,
        7,
        4,
        5
      ]
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          [
            [
              1,
              2,
              3,
              4
            ],
            [
              5,
              6,
              7,
              8
            ],
            [
              9,
              10,
              11,
              12
            ]
          ]
        ]
      },
      "expected": [
        1,
        2,
        3,
        4,
        8,
        12,
        11,
        10,
        9,
        5,
        6,
        7
      ]
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
        1
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
            ]
          ]
        ]
      },
      "expected": [
        1,
        2,
        3
      ]
    }
  ]
}
```
