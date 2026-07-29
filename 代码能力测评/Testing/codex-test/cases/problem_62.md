# 题目62 不同路径

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

一个机器人位于一个 `m x n`网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
示例 1：
题目配图：
输入：m = 3, n = 7输出：28
示例 2：
输入：m = 3, n = 2输出：3解释：从左上角开始，总共有 3 条路径可以到达右下角。1\. 向右 -> 向下 -> 向下2\. 向下 -> 向下 -> 向右3\. 向下 -> 向右 -> 向下
示例 3：
输入：m = 7, n = 3输出：28
示例 4：
输入：m = 3, n = 3输出：6
提示：
`1 <= m, n <= 100`
题目数据保证答案小于等于 2 * 10<sup>9</sup>

```json
{
  "id": 62,
  "title": "不同路径",
  "difficulty": "中等",
  "method": "question_62",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          3,
          7
        ]
      },
      "expected": 28
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          3,
          2
        ]
      },
      "expected": 3
    },
    {
      "name": "case_03_edge_one_cell",
      "input": {
        "args": [
          1,
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_04_edge_one_row",
      "input": {
        "args": [
          1,
          10
        ]
      },
      "expected": 1
    },
    {
      "name": "case_05_edge_one_col",
      "input": {
        "args": [
          10,
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          3,
          7
        ]
      },
      "expected": 28
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          3,
          2
        ]
      },
      "expected": 3
    },
    {
      "name": "case_08_edge_one_cell",
      "input": {
        "args": [
          1,
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_09_edge_one_row",
      "input": {
        "args": [
          1,
          10
        ]
      },
      "expected": 1
    },
    {
      "name": "case_10_edge_one_col",
      "input": {
        "args": [
          10,
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          3,
          7
        ]
      },
      "expected": 28
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          3,
          2
        ]
      },
      "expected": 3
    },
    {
      "name": "case_13_edge_one_cell",
      "input": {
        "args": [
          1,
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_14_edge_one_row",
      "input": {
        "args": [
          1,
          10
        ]
      },
      "expected": 1
    },
    {
      "name": "case_15_edge_one_col",
      "input": {
        "args": [
          10,
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          3,
          7
        ]
      },
      "expected": 28
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          3,
          2
        ]
      },
      "expected": 3
    },
    {
      "name": "case_18_edge_one_cell",
      "input": {
        "args": [
          1,
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_19_edge_one_row",
      "input": {
        "args": [
          1,
          10
        ]
      },
      "expected": 1
    },
    {
      "name": "case_20_edge_one_col",
      "input": {
        "args": [
          10,
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          3,
          7
        ]
      },
      "expected": 28
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          3,
          2
        ]
      },
      "expected": 3
    },
    {
      "name": "case_23_edge_one_cell",
      "input": {
        "args": [
          1,
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_24_edge_one_row",
      "input": {
        "args": [
          1,
          10
        ]
      },
      "expected": 1
    },
    {
      "name": "case_25_edge_one_col",
      "input": {
        "args": [
          10,
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          3,
          7
        ]
      },
      "expected": 28
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          3,
          2
        ]
      },
      "expected": 3
    },
    {
      "name": "case_28_edge_one_cell",
      "input": {
        "args": [
          1,
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_29_edge_one_row",
      "input": {
        "args": [
          1,
          10
        ]
      },
      "expected": 1
    },
    {
      "name": "case_30_edge_one_col",
      "input": {
        "args": [
          10,
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          3,
          7
        ]
      },
      "expected": 28
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          3,
          2
        ]
      },
      "expected": 3
    },
    {
      "name": "case_33_edge_one_cell",
      "input": {
        "args": [
          1,
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_34_edge_one_row",
      "input": {
        "args": [
          1,
          10
        ]
      },
      "expected": 1
    },
    {
      "name": "case_35_edge_one_col",
      "input": {
        "args": [
          10,
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          3,
          7
        ]
      },
      "expected": 28
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          3,
          2
        ]
      },
      "expected": 3
    },
    {
      "name": "case_38_edge_one_cell",
      "input": {
        "args": [
          1,
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_39_edge_one_row",
      "input": {
        "args": [
          1,
          10
        ]
      },
      "expected": 1
    },
    {
      "name": "case_40_edge_one_col",
      "input": {
        "args": [
          10,
          1
        ]
      },
      "expected": 1
    }
  ]
}
```
