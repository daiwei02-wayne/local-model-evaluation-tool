# 题目53 最大子数组和

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个整数数组 `nums` ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组 是数组中的一个连续部分。
示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]输出：6解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：
输入：nums = [1]输出：1
示例 3：
输入：nums = [5,4,-1,7,8]输出：23
提示：
1 <= nums.length <= 10<sup>5</sup>
-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>
进阶：如果你已经实现复杂度为 `O(n)` 的解法，尝试使用更为精妙的 分治法 求解。

```json
{
  "id": 53,
  "title": "最大子数组和",
  "difficulty": "中等",
  "method": "question_53",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            -2,
            1,
            -3,
            4,
            -1,
            2,
            1,
            -5,
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
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_03_edge_single_negative",
      "input": {
        "args": [
          [
            -1
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_04_edge_all_negative",
      "input": {
        "args": [
          [
            -2,
            -1
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_05_edge_all_zero",
      "input": {
        "args": [
          [
            0,
            0,
            0
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            -2,
            1,
            -3,
            4,
            -1,
            2,
            1,
            -5,
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
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_08_edge_single_negative",
      "input": {
        "args": [
          [
            -1
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_09_edge_all_negative",
      "input": {
        "args": [
          [
            -2,
            -1
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_10_edge_all_zero",
      "input": {
        "args": [
          [
            0,
            0,
            0
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            -2,
            1,
            -3,
            4,
            -1,
            2,
            1,
            -5,
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
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_13_edge_single_negative",
      "input": {
        "args": [
          [
            -1
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_14_edge_all_negative",
      "input": {
        "args": [
          [
            -2,
            -1
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_15_edge_all_zero",
      "input": {
        "args": [
          [
            0,
            0,
            0
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            -2,
            1,
            -3,
            4,
            -1,
            2,
            1,
            -5,
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
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_18_edge_single_negative",
      "input": {
        "args": [
          [
            -1
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_19_edge_all_negative",
      "input": {
        "args": [
          [
            -2,
            -1
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_20_edge_all_zero",
      "input": {
        "args": [
          [
            0,
            0,
            0
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
            -2,
            1,
            -3,
            4,
            -1,
            2,
            1,
            -5,
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
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_23_edge_single_negative",
      "input": {
        "args": [
          [
            -1
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_24_edge_all_negative",
      "input": {
        "args": [
          [
            -2,
            -1
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_25_edge_all_zero",
      "input": {
        "args": [
          [
            0,
            0,
            0
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            -2,
            1,
            -3,
            4,
            -1,
            2,
            1,
            -5,
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
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_28_edge_single_negative",
      "input": {
        "args": [
          [
            -1
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_29_edge_all_negative",
      "input": {
        "args": [
          [
            -2,
            -1
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_30_edge_all_zero",
      "input": {
        "args": [
          [
            0,
            0,
            0
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            -2,
            1,
            -3,
            4,
            -1,
            2,
            1,
            -5,
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
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_33_edge_single_negative",
      "input": {
        "args": [
          [
            -1
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_34_edge_all_negative",
      "input": {
        "args": [
          [
            -2,
            -1
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_35_edge_all_zero",
      "input": {
        "args": [
          [
            0,
            0,
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
            -2,
            1,
            -3,
            4,
            -1,
            2,
            1,
            -5,
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
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_38_edge_single_negative",
      "input": {
        "args": [
          [
            -1
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_39_edge_all_negative",
      "input": {
        "args": [
          [
            -2,
            -1
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_40_edge_all_zero",
      "input": {
        "args": [
          [
            0,
            0,
            0
          ]
        ]
      },
      "expected": 0
    }
  ]
}
```
