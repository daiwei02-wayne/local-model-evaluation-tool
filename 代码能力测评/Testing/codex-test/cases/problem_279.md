# 题目279 完全平方数

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个整数 `n` ，返回 _和为 `n` 的完全平方数的最少数量_ 。
完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，`1`、`4`、`9` 和 `16` 都是完全平方数，而 `3` 和 `11` 不是。
示例 1：
输入：n = 12输出：3解释：12 = 4 + 4 + 4
示例 2：
输入：n = 13输出：2解释：13 = 4 + 9
提示：
1 <= n <= 10<sup>4</sup>

```json
{
  "id": 279,
  "title": "完全平方数",
  "difficulty": "中等",
  "method": "question_279",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          12
        ]
      },
      "expected": 3
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          13
        ]
      },
      "expected": 2
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
      "name": "case_04_edge_two",
      "input": {
        "args": [
          2
        ]
      },
      "expected": 2
    },
    {
      "name": "case_05_edge_large_prime_like",
      "input": {
        "args": [
          43
        ]
      },
      "expected": 3
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          12
        ]
      },
      "expected": 3
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          13
        ]
      },
      "expected": 2
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
      "name": "case_09_edge_two",
      "input": {
        "args": [
          2
        ]
      },
      "expected": 2
    },
    {
      "name": "case_10_edge_large_prime_like",
      "input": {
        "args": [
          43
        ]
      },
      "expected": 3
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          12
        ]
      },
      "expected": 3
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          13
        ]
      },
      "expected": 2
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
      "name": "case_14_edge_two",
      "input": {
        "args": [
          2
        ]
      },
      "expected": 2
    },
    {
      "name": "case_15_edge_large_prime_like",
      "input": {
        "args": [
          43
        ]
      },
      "expected": 3
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          12
        ]
      },
      "expected": 3
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          13
        ]
      },
      "expected": 2
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
      "name": "case_19_edge_two",
      "input": {
        "args": [
          2
        ]
      },
      "expected": 2
    },
    {
      "name": "case_20_edge_large_prime_like",
      "input": {
        "args": [
          43
        ]
      },
      "expected": 3
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          12
        ]
      },
      "expected": 3
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          13
        ]
      },
      "expected": 2
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
      "name": "case_24_edge_two",
      "input": {
        "args": [
          2
        ]
      },
      "expected": 2
    },
    {
      "name": "case_25_edge_large_prime_like",
      "input": {
        "args": [
          43
        ]
      },
      "expected": 3
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          12
        ]
      },
      "expected": 3
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          13
        ]
      },
      "expected": 2
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
      "name": "case_29_edge_two",
      "input": {
        "args": [
          2
        ]
      },
      "expected": 2
    },
    {
      "name": "case_30_edge_large_prime_like",
      "input": {
        "args": [
          43
        ]
      },
      "expected": 3
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          12
        ]
      },
      "expected": 3
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          13
        ]
      },
      "expected": 2
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
      "name": "case_34_edge_two",
      "input": {
        "args": [
          2
        ]
      },
      "expected": 2
    },
    {
      "name": "case_35_edge_large_prime_like",
      "input": {
        "args": [
          43
        ]
      },
      "expected": 3
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          12
        ]
      },
      "expected": 3
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          13
        ]
      },
      "expected": 2
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
      "name": "case_39_edge_two",
      "input": {
        "args": [
          2
        ]
      },
      "expected": 2
    },
    {
      "name": "case_40_edge_large_prime_like",
      "input": {
        "args": [
          43
        ]
      },
      "expected": 3
    }
  ]
}
```
