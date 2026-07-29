# 题目84 柱状图中最大的矩形

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定 _n_ 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
示例 1:
题目配图：
输入：heights = [2,1,5,6,2,3]输出：10解释：最大的矩形为图中红色区域，面积为 10
示例 2：
题目配图：
输入： heights = [2,4]输出： 4
提示：
1 <= heights.length <=10<sup>5</sup>
0 <= heights[i] <= 10<sup>4</sup>

```json
{
  "id": 84,
  "title": "柱状图中最大的矩形",
  "difficulty": "困难",
  "method": "question_84",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            2,
            1,
            5,
            6,
            2,
            3
          ]
        ]
      },
      "expected": 10
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            2,
            4
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_03_edge_single",
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
      "name": "case_04_edge_valley",
      "input": {
        "args": [
          [
            2,
            1,
            2
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_05_edge_increasing",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            2,
            1,
            5,
            6,
            2,
            3
          ]
        ]
      },
      "expected": 10
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            2,
            4
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_08_edge_single",
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
      "name": "case_09_edge_valley",
      "input": {
        "args": [
          [
            2,
            1,
            2
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_10_edge_increasing",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            2,
            1,
            5,
            6,
            2,
            3
          ]
        ]
      },
      "expected": 10
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          [
            2,
            4
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_13_edge_single",
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
      "name": "case_14_edge_valley",
      "input": {
        "args": [
          [
            2,
            1,
            2
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_15_edge_increasing",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            2,
            1,
            5,
            6,
            2,
            3
          ]
        ]
      },
      "expected": 10
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            2,
            4
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_18_edge_single",
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
      "name": "case_19_edge_valley",
      "input": {
        "args": [
          [
            2,
            1,
            2
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_20_edge_increasing",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            2,
            1,
            5,
            6,
            2,
            3
          ]
        ]
      },
      "expected": 10
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            2,
            4
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_23_edge_single",
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
      "name": "case_24_edge_valley",
      "input": {
        "args": [
          [
            2,
            1,
            2
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_25_edge_increasing",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            2,
            1,
            5,
            6,
            2,
            3
          ]
        ]
      },
      "expected": 10
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          [
            2,
            4
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_28_edge_single",
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
      "name": "case_29_edge_valley",
      "input": {
        "args": [
          [
            2,
            1,
            2
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_30_edge_increasing",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            2,
            1,
            5,
            6,
            2,
            3
          ]
        ]
      },
      "expected": 10
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          [
            2,
            4
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_33_edge_single",
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
      "name": "case_34_edge_valley",
      "input": {
        "args": [
          [
            2,
            1,
            2
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_35_edge_increasing",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ]
      },
      "expected": 6
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          [
            2,
            1,
            5,
            6,
            2,
            3
          ]
        ]
      },
      "expected": 10
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            2,
            4
          ]
        ]
      },
      "expected": 4
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
      "expected": 1
    },
    {
      "name": "case_39_edge_valley",
      "input": {
        "args": [
          [
            2,
            1,
            2
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_40_edge_increasing",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ]
      },
      "expected": 6
    }
  ]
}
```
