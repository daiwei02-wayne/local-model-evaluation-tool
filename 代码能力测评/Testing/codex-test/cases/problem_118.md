# 题目118 杨辉三角

来源：LeetCode 热题 100（https://leetcode.cn/studyplan/top-100-liked/）

```json
{
  "id": 118,
  "title": "杨辉三角",
  "difficulty": "简单",
  "method": "question_118",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          5
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ],
        [
          1,
          3,
          3,
          1
        ],
        [
          1,
          4,
          6,
          4,
          1
        ]
      ]
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          1
        ]
      },
      "expected": [
        [
          1
        ]
      ]
    },
    {
      "name": "case_03_base",
      "input": {
        "args": [
          2
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ]
      ]
    },
    {
      "name": "case_04_edge_three",
      "input": {
        "args": [
          3
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ]
      ]
    },
    {
      "name": "case_05_edge_six",
      "input": {
        "args": [
          6
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ],
        [
          1,
          3,
          3,
          1
        ],
        [
          1,
          4,
          6,
          4,
          1
        ],
        [
          1,
          5,
          10,
          10,
          5,
          1
        ]
      ]
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          5
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ],
        [
          1,
          3,
          3,
          1
        ],
        [
          1,
          4,
          6,
          4,
          1
        ]
      ]
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          1
        ]
      },
      "expected": [
        [
          1
        ]
      ]
    },
    {
      "name": "case_08_base",
      "input": {
        "args": [
          2
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ]
      ]
    },
    {
      "name": "case_09_edge_three",
      "input": {
        "args": [
          3
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ]
      ]
    },
    {
      "name": "case_10_edge_six",
      "input": {
        "args": [
          6
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ],
        [
          1,
          3,
          3,
          1
        ],
        [
          1,
          4,
          6,
          4,
          1
        ],
        [
          1,
          5,
          10,
          10,
          5,
          1
        ]
      ]
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          5
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ],
        [
          1,
          3,
          3,
          1
        ],
        [
          1,
          4,
          6,
          4,
          1
        ]
      ]
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          1
        ]
      },
      "expected": [
        [
          1
        ]
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          2
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ]
      ]
    },
    {
      "name": "case_14_edge_three",
      "input": {
        "args": [
          3
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ]
      ]
    },
    {
      "name": "case_15_edge_six",
      "input": {
        "args": [
          6
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ],
        [
          1,
          3,
          3,
          1
        ],
        [
          1,
          4,
          6,
          4,
          1
        ],
        [
          1,
          5,
          10,
          10,
          5,
          1
        ]
      ]
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          5
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ],
        [
          1,
          3,
          3,
          1
        ],
        [
          1,
          4,
          6,
          4,
          1
        ]
      ]
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          1
        ]
      },
      "expected": [
        [
          1
        ]
      ]
    },
    {
      "name": "case_18_base",
      "input": {
        "args": [
          2
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ]
      ]
    },
    {
      "name": "case_19_edge_three",
      "input": {
        "args": [
          3
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ]
      ]
    },
    {
      "name": "case_20_edge_six",
      "input": {
        "args": [
          6
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ],
        [
          1,
          3,
          3,
          1
        ],
        [
          1,
          4,
          6,
          4,
          1
        ],
        [
          1,
          5,
          10,
          10,
          5,
          1
        ]
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          5
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ],
        [
          1,
          3,
          3,
          1
        ],
        [
          1,
          4,
          6,
          4,
          1
        ]
      ]
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          1
        ]
      },
      "expected": [
        [
          1
        ]
      ]
    },
    {
      "name": "case_23_base",
      "input": {
        "args": [
          2
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ]
      ]
    },
    {
      "name": "case_24_edge_three",
      "input": {
        "args": [
          3
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ]
      ]
    },
    {
      "name": "case_25_edge_six",
      "input": {
        "args": [
          6
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ],
        [
          1,
          3,
          3,
          1
        ],
        [
          1,
          4,
          6,
          4,
          1
        ],
        [
          1,
          5,
          10,
          10,
          5,
          1
        ]
      ]
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          5
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ],
        [
          1,
          3,
          3,
          1
        ],
        [
          1,
          4,
          6,
          4,
          1
        ]
      ]
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          1
        ]
      },
      "expected": [
        [
          1
        ]
      ]
    },
    {
      "name": "case_28_base",
      "input": {
        "args": [
          2
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ]
      ]
    },
    {
      "name": "case_29_edge_three",
      "input": {
        "args": [
          3
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ]
      ]
    },
    {
      "name": "case_30_edge_six",
      "input": {
        "args": [
          6
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ],
        [
          1,
          3,
          3,
          1
        ],
        [
          1,
          4,
          6,
          4,
          1
        ],
        [
          1,
          5,
          10,
          10,
          5,
          1
        ]
      ]
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          5
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ],
        [
          1,
          3,
          3,
          1
        ],
        [
          1,
          4,
          6,
          4,
          1
        ]
      ]
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          1
        ]
      },
      "expected": [
        [
          1
        ]
      ]
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          2
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ]
      ]
    },
    {
      "name": "case_34_edge_three",
      "input": {
        "args": [
          3
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ]
      ]
    },
    {
      "name": "case_35_edge_six",
      "input": {
        "args": [
          6
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ],
        [
          1,
          3,
          3,
          1
        ],
        [
          1,
          4,
          6,
          4,
          1
        ],
        [
          1,
          5,
          10,
          10,
          5,
          1
        ]
      ]
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          5
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ],
        [
          1,
          3,
          3,
          1
        ],
        [
          1,
          4,
          6,
          4,
          1
        ]
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          1
        ]
      },
      "expected": [
        [
          1
        ]
      ]
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          2
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ]
      ]
    },
    {
      "name": "case_39_edge_three",
      "input": {
        "args": [
          3
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ]
      ]
    },
    {
      "name": "case_40_edge_six",
      "input": {
        "args": [
          6
        ]
      },
      "expected": [
        [
          1
        ],
        [
          1,
          1
        ],
        [
          1,
          2,
          1
        ],
        [
          1,
          3,
          3,
          1
        ],
        [
          1,
          4,
          6,
          4,
          1
        ],
        [
          1,
          5,
          10,
          10,
          5,
          1
        ]
      ]
    }
  ]
}
```
