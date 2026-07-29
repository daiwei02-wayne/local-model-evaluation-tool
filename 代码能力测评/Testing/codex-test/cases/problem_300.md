# 题目300 最长递增子序列

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个整数数组 `nums` ，找到其中最长严格递增子序列的长度。
子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，`[3,6,2,7]` 是数组 `[0,3,1,6,2,2,7]` 的子序列。
示例 1：
输入：nums = [10,9,2,5,3,7,101,18]输出：4解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：
输入：nums = [0,1,0,3,2,3]输出：4
示例 3：
输入：nums = [7,7,7,7,7,7,7]输出：1
提示：
`1 <= nums.length <= 2500`
-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>
进阶：
你能将算法的时间复杂度降低到 `O(n log(n))` 吗?

```json
{
  "id": 300,
  "title": "最长递增子序列",
  "difficulty": "中等",
  "method": "question_300",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            10,
            9,
            2,
            5,
            3,
            7,
            101,
            18
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_02_edge_single",
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
      "name": "case_03_edge_decreasing",
      "input": {
        "args": [
          [
            5,
            4,
            3,
            2,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_04_edge_duplicates",
      "input": {
        "args": [
          [
            2,
            2,
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          [
            10,
            9,
            2,
            5,
            3,
            7,
            101,
            18
          ]
        ]
      },
      "expected": 4
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
      "expected": 1
    },
    {
      "name": "case_07_edge_decreasing",
      "input": {
        "args": [
          [
            5,
            4,
            3,
            2,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_08_edge_duplicates",
      "input": {
        "args": [
          [
            2,
            2,
            2
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
            10,
            9,
            2,
            5,
            3,
            7,
            101,
            18
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_10_edge_single",
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
      "name": "case_11_edge_decreasing",
      "input": {
        "args": [
          [
            5,
            4,
            3,
            2,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_12_edge_duplicates",
      "input": {
        "args": [
          [
            2,
            2,
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [
            10,
            9,
            2,
            5,
            3,
            7,
            101,
            18
          ]
        ]
      },
      "expected": 4
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
      "expected": 1
    },
    {
      "name": "case_15_edge_decreasing",
      "input": {
        "args": [
          [
            5,
            4,
            3,
            2,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_16_edge_duplicates",
      "input": {
        "args": [
          [
            2,
            2,
            2
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
            10,
            9,
            2,
            5,
            3,
            7,
            101,
            18
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
      "name": "case_19_edge_decreasing",
      "input": {
        "args": [
          [
            5,
            4,
            3,
            2,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_20_edge_duplicates",
      "input": {
        "args": [
          [
            2,
            2,
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
            10,
            9,
            2,
            5,
            3,
            7,
            101,
            18
          ]
        ]
      },
      "expected": 4
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
      "expected": 1
    },
    {
      "name": "case_23_edge_decreasing",
      "input": {
        "args": [
          [
            5,
            4,
            3,
            2,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_24_edge_duplicates",
      "input": {
        "args": [
          [
            2,
            2,
            2
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
            10,
            9,
            2,
            5,
            3,
            7,
            101,
            18
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_26_edge_single",
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
      "name": "case_27_edge_decreasing",
      "input": {
        "args": [
          [
            5,
            4,
            3,
            2,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_28_edge_duplicates",
      "input": {
        "args": [
          [
            2,
            2,
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          [
            10,
            9,
            2,
            5,
            3,
            7,
            101,
            18
          ]
        ]
      },
      "expected": 4
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
      "expected": 1
    },
    {
      "name": "case_31_edge_decreasing",
      "input": {
        "args": [
          [
            5,
            4,
            3,
            2,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_32_edge_duplicates",
      "input": {
        "args": [
          [
            2,
            2,
            2
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
            10,
            9,
            2,
            5,
            3,
            7,
            101,
            18
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_34_edge_single",
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
      "name": "case_35_edge_decreasing",
      "input": {
        "args": [
          [
            5,
            4,
            3,
            2,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_36_edge_duplicates",
      "input": {
        "args": [
          [
            2,
            2,
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            10,
            9,
            2,
            5,
            3,
            7,
            101,
            18
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
      "name": "case_39_edge_decreasing",
      "input": {
        "args": [
          [
            5,
            4,
            3,
            2,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_40_edge_duplicates",
      "input": {
        "args": [
          [
            2,
            2,
            2
          ]
        ]
      },
      "expected": 1
    }
  ]
}
```
