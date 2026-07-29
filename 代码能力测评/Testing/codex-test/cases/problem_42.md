# 题目42 接雨水

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定 `n` 个非负整数表示每个宽度为 `1` 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例 1：
题目配图：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]输出：6解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
示例 2：
输入：height = [4,2,0,3,2,5]输出：9
提示：
`n == height.length`
1 <= n <= 2 * 10<sup>4</sup>
0 <= height[i] <= 10<sup>5</sup>

```json
{
  "id": 42,
  "title": "接雨水",
  "difficulty": "困难",
  "method": "question_42",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            0,
            1,
            0,
            2,
            1,
            0,
            1,
            3,
            2,
            1,
            2,
            1
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            4,
            2,
            0,
            3,
            2,
            5
          ]
        ]
      },
      "expected": 9
    },
    {
      "name": "case_03_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
    },
    {
      "name": "case_04_edge_monotonic",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_05_edge_right_wall_low",
      "input": {
        "args": [
          [
            5,
            4,
            1,
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            0,
            1,
            0,
            2,
            1,
            0,
            1,
            3,
            2,
            1,
            2,
            1
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            4,
            2,
            0,
            3,
            2,
            5
          ]
        ]
      },
      "expected": 9
    },
    {
      "name": "case_08_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
    },
    {
      "name": "case_09_edge_monotonic",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_10_edge_right_wall_low",
      "input": {
        "args": [
          [
            5,
            4,
            1,
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            0,
            1,
            0,
            2,
            1,
            0,
            1,
            3,
            2,
            1,
            2,
            1
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          [
            4,
            2,
            0,
            3,
            2,
            5
          ]
        ]
      },
      "expected": 9
    },
    {
      "name": "case_13_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
    },
    {
      "name": "case_14_edge_monotonic",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_15_edge_right_wall_low",
      "input": {
        "args": [
          [
            5,
            4,
            1,
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            0,
            1,
            0,
            2,
            1,
            0,
            1,
            3,
            2,
            1,
            2,
            1
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
            4,
            2,
            0,
            3,
            2,
            5
          ]
        ]
      },
      "expected": 9
    },
    {
      "name": "case_18_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
    },
    {
      "name": "case_19_edge_monotonic",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_20_edge_right_wall_low",
      "input": {
        "args": [
          [
            5,
            4,
            1,
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            0,
            1,
            0,
            2,
            1,
            0,
            1,
            3,
            2,
            1,
            2,
            1
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            4,
            2,
            0,
            3,
            2,
            5
          ]
        ]
      },
      "expected": 9
    },
    {
      "name": "case_23_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
    },
    {
      "name": "case_24_edge_monotonic",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_25_edge_right_wall_low",
      "input": {
        "args": [
          [
            5,
            4,
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
            0,
            1,
            0,
            2,
            1,
            0,
            1,
            3,
            2,
            1,
            2,
            1
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          [
            4,
            2,
            0,
            3,
            2,
            5
          ]
        ]
      },
      "expected": 9
    },
    {
      "name": "case_28_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
    },
    {
      "name": "case_29_edge_monotonic",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_30_edge_right_wall_low",
      "input": {
        "args": [
          [
            5,
            4,
            1,
            2
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
            0,
            1,
            0,
            2,
            1,
            0,
            1,
            3,
            2,
            1,
            2,
            1
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          [
            4,
            2,
            0,
            3,
            2,
            5
          ]
        ]
      },
      "expected": 9
    },
    {
      "name": "case_33_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
    },
    {
      "name": "case_34_edge_monotonic",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_35_edge_right_wall_low",
      "input": {
        "args": [
          [
            5,
            4,
            1,
            2
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
            0,
            1,
            0,
            2,
            1,
            0,
            1,
            3,
            2,
            1,
            2,
            1
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
            4,
            2,
            0,
            3,
            2,
            5
          ]
        ]
      },
      "expected": 9
    },
    {
      "name": "case_38_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
    },
    {
      "name": "case_39_edge_monotonic",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_40_edge_right_wall_low",
      "input": {
        "args": [
          [
            5,
            4,
            1,
            2
          ]
        ]
      },
      "expected": 1
    }
  ]
}
```
