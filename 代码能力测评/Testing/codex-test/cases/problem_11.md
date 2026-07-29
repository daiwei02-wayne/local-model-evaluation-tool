# 题目11 盛最多水的容器

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一个长度为 `n` 的整数数组 `height` 。有 `n` 条垂线，第 `i` 条线的两个端点是 `(i, 0)` 和 `(i, height[i])` 。
找出其中的两条线，使得它们与 `x` 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。
示例 1：
题目配图：
输入：[1,8,6,2,5,4,8,3,7]输出：49解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：
输入：height = [1,1]输出：1
提示：
`n == height.length`
2 <= n <= 10<sup>5</sup>
0 <= height[i] <= 10<sup>4</sup>

```json
{
  "id": 11,
  "title": "盛最多水的容器",
  "difficulty": "中等",
  "method": "question_11",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            1,
            8,
            6,
            2,
            5,
            4,
            8,
            3,
            7
          ]
        ]
      },
      "expected": 49
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_03_edge_symmetric_tall",
      "input": {
        "args": [
          [
            4,
            3,
            2,
            1,
            4
          ]
        ]
      },
      "expected": 16
    },
    {
      "name": "case_04_edge_peak_middle",
      "input": {
        "args": [
          [
            1,
            2,
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
            1,
            8,
            6,
            2,
            5,
            4,
            8,
            3,
            7
          ]
        ]
      },
      "expected": 49
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_07_edge_symmetric_tall",
      "input": {
        "args": [
          [
            4,
            3,
            2,
            1,
            4
          ]
        ]
      },
      "expected": 16
    },
    {
      "name": "case_08_edge_peak_middle",
      "input": {
        "args": [
          [
            1,
            2,
            1
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
            1,
            8,
            6,
            2,
            5,
            4,
            8,
            3,
            7
          ]
        ]
      },
      "expected": 49
    },
    {
      "name": "case_10_base",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_11_edge_symmetric_tall",
      "input": {
        "args": [
          [
            4,
            3,
            2,
            1,
            4
          ]
        ]
      },
      "expected": 16
    },
    {
      "name": "case_12_edge_peak_middle",
      "input": {
        "args": [
          [
            1,
            2,
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
            1,
            8,
            6,
            2,
            5,
            4,
            8,
            3,
            7
          ]
        ]
      },
      "expected": 49
    },
    {
      "name": "case_14_base",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_15_edge_symmetric_tall",
      "input": {
        "args": [
          [
            4,
            3,
            2,
            1,
            4
          ]
        ]
      },
      "expected": 16
    },
    {
      "name": "case_16_edge_peak_middle",
      "input": {
        "args": [
          [
            1,
            2,
            1
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
            1,
            8,
            6,
            2,
            5,
            4,
            8,
            3,
            7
          ]
        ]
      },
      "expected": 49
    },
    {
      "name": "case_18_base",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_19_edge_symmetric_tall",
      "input": {
        "args": [
          [
            4,
            3,
            2,
            1,
            4
          ]
        ]
      },
      "expected": 16
    },
    {
      "name": "case_20_edge_peak_middle",
      "input": {
        "args": [
          [
            1,
            2,
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
            1,
            8,
            6,
            2,
            5,
            4,
            8,
            3,
            7
          ]
        ]
      },
      "expected": 49
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_23_edge_symmetric_tall",
      "input": {
        "args": [
          [
            4,
            3,
            2,
            1,
            4
          ]
        ]
      },
      "expected": 16
    },
    {
      "name": "case_24_edge_peak_middle",
      "input": {
        "args": [
          [
            1,
            2,
            1
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
            1,
            8,
            6,
            2,
            5,
            4,
            8,
            3,
            7
          ]
        ]
      },
      "expected": 49
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_27_edge_symmetric_tall",
      "input": {
        "args": [
          [
            4,
            3,
            2,
            1,
            4
          ]
        ]
      },
      "expected": 16
    },
    {
      "name": "case_28_edge_peak_middle",
      "input": {
        "args": [
          [
            1,
            2,
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
            1,
            8,
            6,
            2,
            5,
            4,
            8,
            3,
            7
          ]
        ]
      },
      "expected": 49
    },
    {
      "name": "case_30_base",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_31_edge_symmetric_tall",
      "input": {
        "args": [
          [
            4,
            3,
            2,
            1,
            4
          ]
        ]
      },
      "expected": 16
    },
    {
      "name": "case_32_edge_peak_middle",
      "input": {
        "args": [
          [
            1,
            2,
            1
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
            1,
            8,
            6,
            2,
            5,
            4,
            8,
            3,
            7
          ]
        ]
      },
      "expected": 49
    },
    {
      "name": "case_34_base",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_35_edge_symmetric_tall",
      "input": {
        "args": [
          [
            4,
            3,
            2,
            1,
            4
          ]
        ]
      },
      "expected": 16
    },
    {
      "name": "case_36_edge_peak_middle",
      "input": {
        "args": [
          [
            1,
            2,
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
            1,
            8,
            6,
            2,
            5,
            4,
            8,
            3,
            7
          ]
        ]
      },
      "expected": 49
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_39_edge_symmetric_tall",
      "input": {
        "args": [
          [
            4,
            3,
            2,
            1,
            4
          ]
        ]
      },
      "expected": 16
    },
    {
      "name": "case_40_edge_peak_middle",
      "input": {
        "args": [
          [
            1,
            2,
            1
          ]
        ]
      },
      "expected": 2
    }
  ]
}
```
