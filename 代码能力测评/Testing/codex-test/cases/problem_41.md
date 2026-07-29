# 题目41 缺失的第一个正数

来源：LeetCode 热题 100（https://leetcode.cn/studyplan/top-100-liked/）

```json
{
  "id": 41,
  "title": "缺失的第一个正数",
  "difficulty": "困难",
  "method": "question_41",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            1,
            2,
            0
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            3,
            4,
            -1,
            1
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_03_base",
      "input": {
        "args": [
          [
            7,
            8,
            9,
            11,
            12
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_04_base",
      "input": {
        "args": [
          [
            1
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
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_06_edge_duplicates",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_07_edge_all_negative",
      "input": {
        "args": [
          [
            -1,
            -2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_08_edge_one_two",
      "input": {
        "args": [
          [
            2,
            1
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          [
            1,
            2,
            0
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_10_base",
      "input": {
        "args": [
          [
            3,
            4,
            -1,
            1
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            7,
            8,
            9,
            11,
            12
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          [
            1
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
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_14_edge_duplicates",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_15_edge_all_negative",
      "input": {
        "args": [
          [
            -1,
            -2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_16_edge_one_two",
      "input": {
        "args": [
          [
            2,
            1
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            1,
            2,
            0
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_18_base",
      "input": {
        "args": [
          [
            3,
            4,
            -1,
            1
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_19_base",
      "input": {
        "args": [
          [
            7,
            8,
            9,
            11,
            12
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_20_base",
      "input": {
        "args": [
          [
            1
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
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_22_edge_duplicates",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_23_edge_all_negative",
      "input": {
        "args": [
          [
            -1,
            -2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_24_edge_one_two",
      "input": {
        "args": [
          [
            2,
            1
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            1,
            2,
            0
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            3,
            4,
            -1,
            1
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          [
            7,
            8,
            9,
            11,
            12
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_28_base",
      "input": {
        "args": [
          [
            1
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
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_30_edge_duplicates",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_31_edge_all_negative",
      "input": {
        "args": [
          [
            -1,
            -2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_32_edge_one_two",
      "input": {
        "args": [
          [
            2,
            1
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          [
            1,
            2,
            0
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_34_base",
      "input": {
        "args": [
          [
            3,
            4,
            -1,
            1
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_35_base",
      "input": {
        "args": [
          [
            7,
            8,
            9,
            11,
            12
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          [
            1
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
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_38_edge_duplicates",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_39_edge_all_negative",
      "input": {
        "args": [
          [
            -1,
            -2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_40_edge_one_two",
      "input": {
        "args": [
          [
            2,
            1
          ]
        ]
      },
      "expected": 3
    }
  ]
}
```
