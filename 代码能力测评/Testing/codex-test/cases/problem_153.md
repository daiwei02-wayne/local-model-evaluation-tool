# 题目153 寻找旋转排序数组中的最小值

来源：LeetCode 热题 100（https://leetcode.cn/studyplan/top-100-liked/）

```json
{
  "id": 153,
  "title": "寻找旋转排序数组中的最小值",
  "difficulty": "中等",
  "method": "question_153",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            3,
            4,
            5,
            1,
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_03_base",
      "input": {
        "args": [
          [
            11,
            13,
            15,
            17
          ]
        ]
      },
      "expected": 11
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
      "expected": 1
    },
    {
      "name": "case_05_edge_two_rotated",
      "input": {
        "args": [
          [
            2,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_06_edge_not_rotated",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            3,
            4,
            5,
            1,
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_08_base",
      "input": {
        "args": [
          [
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          [
            11,
            13,
            15,
            17
          ]
        ]
      },
      "expected": 11
    },
    {
      "name": "case_10_base",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_11_edge_two_rotated",
      "input": {
        "args": [
          [
            2,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_12_edge_not_rotated",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [
            3,
            4,
            5,
            1,
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_14_base",
      "input": {
        "args": [
          [
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_15_base",
      "input": {
        "args": [
          [
            11,
            13,
            15,
            17
          ]
        ]
      },
      "expected": 11
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_17_edge_two_rotated",
      "input": {
        "args": [
          [
            2,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_18_edge_not_rotated",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_19_base",
      "input": {
        "args": [
          [
            3,
            4,
            5,
            1,
            2
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
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            11,
            13,
            15,
            17
          ]
        ]
      },
      "expected": 11
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_23_edge_two_rotated",
      "input": {
        "args": [
          [
            2,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_24_edge_not_rotated",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            3,
            4,
            5,
            1,
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          [
            11,
            13,
            15,
            17
          ]
        ]
      },
      "expected": 11
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
      "expected": 1
    },
    {
      "name": "case_29_edge_two_rotated",
      "input": {
        "args": [
          [
            2,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_30_edge_not_rotated",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            3,
            4,
            5,
            1,
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          [
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          [
            11,
            13,
            15,
            17
          ]
        ]
      },
      "expected": 11
    },
    {
      "name": "case_34_base",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_35_edge_two_rotated",
      "input": {
        "args": [
          [
            2,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_36_edge_not_rotated",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            3,
            4,
            5,
            1,
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          [
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_39_base",
      "input": {
        "args": [
          [
            11,
            13,
            15,
            17
          ]
        ]
      },
      "expected": 11
    },
    {
      "name": "case_40_base",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 1
    }
  ]
}
```
