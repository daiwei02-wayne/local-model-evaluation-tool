# 题目152 乘积最大子数组

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个整数数组 `nums` ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
测试用例的答案是一个 32-位 整数。
子数组 是数组的连续子序列。
示例 1:
输入: nums = [2,3,-2,4]输出: 6解释: 子数组 [2,3] 有最大乘积 6。
示例 2:
输入: nums = [-2,0,-1]输出: 0解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
提示:
1 <= nums.length <= 2 * 10<sup>4</sup>
`-10 <= nums[i] <= 10`
`nums` 的任何前缀或后缀的乘积都 保证 是一个 32-位 整数

```json
{
  "id": 152,
  "title": "乘积最大子数组",
  "difficulty": "中等",
  "method": "question_152",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            2,
            3,
            -2,
            4
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
            -2,
            0,
            -1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_03_edge_single_negative",
      "input": {
        "args": [
          [
            -2
          ]
        ]
      },
      "expected": -2
    },
    {
      "name": "case_04_edge_zero_prefix",
      "input": {
        "args": [
          [
            0,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_05_edge_two_negatives",
      "input": {
        "args": [
          [
            -2,
            3,
            -4
          ]
        ]
      },
      "expected": 24
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            2,
            3,
            -2,
            4
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
            -2,
            0,
            -1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_08_edge_single_negative",
      "input": {
        "args": [
          [
            -2
          ]
        ]
      },
      "expected": -2
    },
    {
      "name": "case_09_edge_zero_prefix",
      "input": {
        "args": [
          [
            0,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_10_edge_two_negatives",
      "input": {
        "args": [
          [
            -2,
            3,
            -4
          ]
        ]
      },
      "expected": 24
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            2,
            3,
            -2,
            4
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
            -2,
            0,
            -1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_13_edge_single_negative",
      "input": {
        "args": [
          [
            -2
          ]
        ]
      },
      "expected": -2
    },
    {
      "name": "case_14_edge_zero_prefix",
      "input": {
        "args": [
          [
            0,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_15_edge_two_negatives",
      "input": {
        "args": [
          [
            -2,
            3,
            -4
          ]
        ]
      },
      "expected": 24
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            2,
            3,
            -2,
            4
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
            -2,
            0,
            -1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_18_edge_single_negative",
      "input": {
        "args": [
          [
            -2
          ]
        ]
      },
      "expected": -2
    },
    {
      "name": "case_19_edge_zero_prefix",
      "input": {
        "args": [
          [
            0,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_20_edge_two_negatives",
      "input": {
        "args": [
          [
            -2,
            3,
            -4
          ]
        ]
      },
      "expected": 24
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            2,
            3,
            -2,
            4
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
            -2,
            0,
            -1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_23_edge_single_negative",
      "input": {
        "args": [
          [
            -2
          ]
        ]
      },
      "expected": -2
    },
    {
      "name": "case_24_edge_zero_prefix",
      "input": {
        "args": [
          [
            0,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_25_edge_two_negatives",
      "input": {
        "args": [
          [
            -2,
            3,
            -4
          ]
        ]
      },
      "expected": 24
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            2,
            3,
            -2,
            4
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
            -2,
            0,
            -1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_28_edge_single_negative",
      "input": {
        "args": [
          [
            -2
          ]
        ]
      },
      "expected": -2
    },
    {
      "name": "case_29_edge_zero_prefix",
      "input": {
        "args": [
          [
            0,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_30_edge_two_negatives",
      "input": {
        "args": [
          [
            -2,
            3,
            -4
          ]
        ]
      },
      "expected": 24
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            2,
            3,
            -2,
            4
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
            -2,
            0,
            -1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_33_edge_single_negative",
      "input": {
        "args": [
          [
            -2
          ]
        ]
      },
      "expected": -2
    },
    {
      "name": "case_34_edge_zero_prefix",
      "input": {
        "args": [
          [
            0,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_35_edge_two_negatives",
      "input": {
        "args": [
          [
            -2,
            3,
            -4
          ]
        ]
      },
      "expected": 24
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          [
            2,
            3,
            -2,
            4
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
            -2,
            0,
            -1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_38_edge_single_negative",
      "input": {
        "args": [
          [
            -2
          ]
        ]
      },
      "expected": -2
    },
    {
      "name": "case_39_edge_zero_prefix",
      "input": {
        "args": [
          [
            0,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_40_edge_two_negatives",
      "input": {
        "args": [
          [
            -2,
            3,
            -4
          ]
        ]
      },
      "expected": 24
    }
  ]
}
```
