# 题目287 寻找重复数

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一个包含 `n + 1` 个整数的数组 `nums` ，其数字都在 `[1, n]` 范围内（包括 `1` 和 `n`），可知至少存在一个重复的整数。
假设 `nums` 只有 一个重复的整数 ，返回 这个重复的数 。
你设计的解决方案必须 不修改 数组 `nums` 且只用常量级 `O(1)` 的额外空间。
示例 1：
输入：nums = [1,3,4,2,2]输出：2
示例 2：
输入：nums = [3,1,3,4,2]输出：3
提示：
1 <= n <= 10<sup>5</sup>
`nums.length == n + 1`
`1 <= nums[i] <= n`
`nums` 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次
进阶：
如何证明 `nums` 中至少存在一个重复的数字?
你可以设计一个线性级时间复杂度 `O(n)` 的解决方案吗？

```json
{
  "id": 287,
  "title": "寻找重复数",
  "difficulty": "中等",
  "method": "question_287",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            1,
            3,
            4,
            2,
            2
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
            3,
            1,
            3,
            4,
            2
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_03_edge_min",
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
      "name": "case_04_edge_all_duplicate",
      "input": {
        "args": [
          [
            2,
            2,
            2,
            2,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_05_edge_duplicate_many",
      "input": {
        "args": [
          [
            1,
            4,
            4,
            2,
            4
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            1,
            3,
            4,
            2,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            3,
            1,
            3,
            4,
            2
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_08_edge_min",
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
      "name": "case_09_edge_all_duplicate",
      "input": {
        "args": [
          [
            2,
            2,
            2,
            2,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_10_edge_duplicate_many",
      "input": {
        "args": [
          [
            1,
            4,
            4,
            2,
            4
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            1,
            3,
            4,
            2,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          [
            3,
            1,
            3,
            4,
            2
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_13_edge_min",
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
      "name": "case_14_edge_all_duplicate",
      "input": {
        "args": [
          [
            2,
            2,
            2,
            2,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_15_edge_duplicate_many",
      "input": {
        "args": [
          [
            1,
            4,
            4,
            2,
            4
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            1,
            3,
            4,
            2,
            2
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
            3,
            1,
            3,
            4,
            2
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_18_edge_min",
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
      "name": "case_19_edge_all_duplicate",
      "input": {
        "args": [
          [
            2,
            2,
            2,
            2,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_20_edge_duplicate_many",
      "input": {
        "args": [
          [
            1,
            4,
            4,
            2,
            4
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            1,
            3,
            4,
            2,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            3,
            1,
            3,
            4,
            2
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_23_edge_min",
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
      "name": "case_24_edge_all_duplicate",
      "input": {
        "args": [
          [
            2,
            2,
            2,
            2,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_25_edge_duplicate_many",
      "input": {
        "args": [
          [
            1,
            4,
            4,
            2,
            4
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            1,
            3,
            4,
            2,
            2
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
            3,
            1,
            3,
            4,
            2
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_28_edge_min",
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
      "name": "case_29_edge_all_duplicate",
      "input": {
        "args": [
          [
            2,
            2,
            2,
            2,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_30_edge_duplicate_many",
      "input": {
        "args": [
          [
            1,
            4,
            4,
            2,
            4
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            1,
            3,
            4,
            2,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          [
            3,
            1,
            3,
            4,
            2
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_33_edge_min",
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
      "name": "case_34_edge_all_duplicate",
      "input": {
        "args": [
          [
            2,
            2,
            2,
            2,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_35_edge_duplicate_many",
      "input": {
        "args": [
          [
            1,
            4,
            4,
            2,
            4
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          [
            1,
            3,
            4,
            2,
            2
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
            3,
            1,
            3,
            4,
            2
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_38_edge_min",
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
      "name": "case_39_edge_all_duplicate",
      "input": {
        "args": [
          [
            2,
            2,
            2,
            2,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_40_edge_duplicate_many",
      "input": {
        "args": [
          [
            1,
            4,
            4,
            2,
            4
          ]
        ]
      },
      "expected": 4
    }
  ]
}
```
