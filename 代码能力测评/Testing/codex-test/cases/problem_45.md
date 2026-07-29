# 题目45 跳跃游戏 II

来源：LeetCode 热题 100（https://leetcode.cn/studyplan/top-100-liked/）

```json
{
  "id": 45,
  "title": "跳跃游戏 II",
  "difficulty": "中等",
  "method": "question_45",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            2,
            3,
            1,
            1,
            4
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            2,
            3,
            0,
            1,
            4
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
            0
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_04_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
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
            1,
            1,
            1,
            1
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_06_edge_single",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_07_edge_all_one",
      "input": {
        "args": [
          [
            1,
            1,
            1,
            1,
            1
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_08_edge_jump_to_end",
      "input": {
        "args": [
          [
            5,
            0,
            0,
            0
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          [
            2,
            3,
            1,
            1,
            4
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_10_base",
      "input": {
        "args": [
          [
            2,
            3,
            0,
            1,
            4
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
            0
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
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
            1,
            1,
            1,
            1
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_14_edge_single",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_15_edge_all_one",
      "input": {
        "args": [
          [
            1,
            1,
            1,
            1,
            1
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_16_edge_jump_to_end",
      "input": {
        "args": [
          [
            5,
            0,
            0,
            0
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            2,
            3,
            1,
            1,
            4
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_18_base",
      "input": {
        "args": [
          [
            2,
            3,
            0,
            1,
            4
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
            0
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_20_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
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
            1,
            1,
            1,
            1
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_22_edge_single",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_23_edge_all_one",
      "input": {
        "args": [
          [
            1,
            1,
            1,
            1,
            1
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_24_edge_jump_to_end",
      "input": {
        "args": [
          [
            5,
            0,
            0,
            0
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
            2,
            3,
            1,
            1,
            4
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            2,
            3,
            0,
            1,
            4
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
            0
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_28_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
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
            1,
            1,
            1,
            1
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_30_edge_single",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_31_edge_all_one",
      "input": {
        "args": [
          [
            1,
            1,
            1,
            1,
            1
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_32_edge_jump_to_end",
      "input": {
        "args": [
          [
            5,
            0,
            0,
            0
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          [
            2,
            3,
            1,
            1,
            4
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_34_base",
      "input": {
        "args": [
          [
            2,
            3,
            0,
            1,
            4
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
            0
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
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
            1,
            1,
            1,
            1
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_38_edge_single",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_39_edge_all_one",
      "input": {
        "args": [
          [
            1,
            1,
            1,
            1,
            1
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_40_edge_jump_to_end",
      "input": {
        "args": [
          [
            5,
            0,
            0,
            0
          ]
        ]
      },
      "expected": 1
    }
  ]
}
```
