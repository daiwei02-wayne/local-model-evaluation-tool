# 题目70 爬楼梯

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

假设你正在爬楼梯。需要 `n` 阶你才能到达楼顶。
每次你可以爬 `1` 或 `2` 个台阶。你有多少种不同的方法可以爬到楼顶呢？
示例 1：
输入：n = 2输出：2解释：有两种方法可以爬到楼顶。1\. 1 阶 + 1 阶2\. 2 阶
示例 2：
输入：n = 3输出：3解释：有三种方法可以爬到楼顶。1\. 1 阶 + 1 阶 + 1 阶2\. 1 阶 + 2 阶3\. 2 阶 + 1 阶
提示：
`1 <= n <= 45`

```json
{
  "id": 70,
  "title": "爬楼梯",
  "difficulty": "简单",
  "method": "question_70",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          2
        ]
      },
      "expected": 2
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          3
        ]
      },
      "expected": 3
    },
    {
      "name": "case_03_edge_one",
      "input": {
        "args": [
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_04_edge_four",
      "input": {
        "args": [
          4
        ]
      },
      "expected": 5
    },
    {
      "name": "case_05_edge_five",
      "input": {
        "args": [
          5
        ]
      },
      "expected": 8
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          2
        ]
      },
      "expected": 2
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          3
        ]
      },
      "expected": 3
    },
    {
      "name": "case_08_edge_one",
      "input": {
        "args": [
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_09_edge_four",
      "input": {
        "args": [
          4
        ]
      },
      "expected": 5
    },
    {
      "name": "case_10_edge_five",
      "input": {
        "args": [
          5
        ]
      },
      "expected": 8
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          2
        ]
      },
      "expected": 2
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          3
        ]
      },
      "expected": 3
    },
    {
      "name": "case_13_edge_one",
      "input": {
        "args": [
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_14_edge_four",
      "input": {
        "args": [
          4
        ]
      },
      "expected": 5
    },
    {
      "name": "case_15_edge_five",
      "input": {
        "args": [
          5
        ]
      },
      "expected": 8
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          2
        ]
      },
      "expected": 2
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          3
        ]
      },
      "expected": 3
    },
    {
      "name": "case_18_edge_one",
      "input": {
        "args": [
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_19_edge_four",
      "input": {
        "args": [
          4
        ]
      },
      "expected": 5
    },
    {
      "name": "case_20_edge_five",
      "input": {
        "args": [
          5
        ]
      },
      "expected": 8
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          2
        ]
      },
      "expected": 2
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          3
        ]
      },
      "expected": 3
    },
    {
      "name": "case_23_edge_one",
      "input": {
        "args": [
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_24_edge_four",
      "input": {
        "args": [
          4
        ]
      },
      "expected": 5
    },
    {
      "name": "case_25_edge_five",
      "input": {
        "args": [
          5
        ]
      },
      "expected": 8
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          2
        ]
      },
      "expected": 2
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          3
        ]
      },
      "expected": 3
    },
    {
      "name": "case_28_edge_one",
      "input": {
        "args": [
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_29_edge_four",
      "input": {
        "args": [
          4
        ]
      },
      "expected": 5
    },
    {
      "name": "case_30_edge_five",
      "input": {
        "args": [
          5
        ]
      },
      "expected": 8
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          2
        ]
      },
      "expected": 2
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          3
        ]
      },
      "expected": 3
    },
    {
      "name": "case_33_edge_one",
      "input": {
        "args": [
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_34_edge_four",
      "input": {
        "args": [
          4
        ]
      },
      "expected": 5
    },
    {
      "name": "case_35_edge_five",
      "input": {
        "args": [
          5
        ]
      },
      "expected": 8
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          2
        ]
      },
      "expected": 2
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          3
        ]
      },
      "expected": 3
    },
    {
      "name": "case_38_edge_one",
      "input": {
        "args": [
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_39_edge_four",
      "input": {
        "args": [
          4
        ]
      },
      "expected": 5
    },
    {
      "name": "case_40_edge_five",
      "input": {
        "args": [
          5
        ]
      },
      "expected": 8
    }
  ]
}
```
