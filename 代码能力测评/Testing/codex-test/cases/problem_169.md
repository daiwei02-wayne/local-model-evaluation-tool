# 题目169 多数元素

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一个大小为 `n`的数组 `nums` ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 `⌊ n/2 ⌋` 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例 1：
输入：nums = [3,2,3]输出：3
示例 2：
输入：nums = [2,2,1,1,1,2,2]输出：2
提示：
`n == nums.length`
1 <= n <= 5 * 10<sup>4</sup>
-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>
进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。

```json
{
  "id": 169,
  "title": "多数元素",
  "difficulty": "简单",
  "method": "question_169",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            3,
            2,
            3
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            2,
            2,
            1,
            1,
            1,
            2,
            2
          ]
        ]
      },
      "expected": 2
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
      "name": "case_04_edge_majority_suffix",
      "input": {
        "args": [
          [
            6,
            5,
            5
          ]
        ]
      },
      "expected": 5
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          [
            3,
            2,
            3
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            2,
            2,
            1,
            1,
            1,
            2,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_07_edge_single",
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
      "name": "case_08_edge_majority_suffix",
      "input": {
        "args": [
          [
            6,
            5,
            5
          ]
        ]
      },
      "expected": 5
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          [
            3,
            2,
            3
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_10_base",
      "input": {
        "args": [
          [
            2,
            2,
            1,
            1,
            1,
            2,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_11_edge_single",
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
      "name": "case_12_edge_majority_suffix",
      "input": {
        "args": [
          [
            6,
            5,
            5
          ]
        ]
      },
      "expected": 5
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [
            3,
            2,
            3
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_14_base",
      "input": {
        "args": [
          [
            2,
            2,
            1,
            1,
            1,
            2,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_15_edge_single",
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
      "name": "case_16_edge_majority_suffix",
      "input": {
        "args": [
          [
            6,
            5,
            5
          ]
        ]
      },
      "expected": 5
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            3,
            2,
            3
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_18_base",
      "input": {
        "args": [
          [
            2,
            2,
            1,
            1,
            1,
            2,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_19_edge_single",
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
      "name": "case_20_edge_majority_suffix",
      "input": {
        "args": [
          [
            6,
            5,
            5
          ]
        ]
      },
      "expected": 5
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            3,
            2,
            3
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            2,
            2,
            1,
            1,
            1,
            2,
            2
          ]
        ]
      },
      "expected": 2
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
      "name": "case_24_edge_majority_suffix",
      "input": {
        "args": [
          [
            6,
            5,
            5
          ]
        ]
      },
      "expected": 5
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            3,
            2,
            3
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            2,
            2,
            1,
            1,
            1,
            2,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_27_edge_single",
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
      "name": "case_28_edge_majority_suffix",
      "input": {
        "args": [
          [
            6,
            5,
            5
          ]
        ]
      },
      "expected": 5
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          [
            3,
            2,
            3
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_30_base",
      "input": {
        "args": [
          [
            2,
            2,
            1,
            1,
            1,
            2,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_31_edge_single",
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
      "name": "case_32_edge_majority_suffix",
      "input": {
        "args": [
          [
            6,
            5,
            5
          ]
        ]
      },
      "expected": 5
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          [
            3,
            2,
            3
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_34_base",
      "input": {
        "args": [
          [
            2,
            2,
            1,
            1,
            1,
            2,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_35_edge_single",
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
      "name": "case_36_edge_majority_suffix",
      "input": {
        "args": [
          [
            6,
            5,
            5
          ]
        ]
      },
      "expected": 5
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            3,
            2,
            3
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          [
            2,
            2,
            1,
            1,
            1,
            2,
            2
          ]
        ]
      },
      "expected": 2
    },
    {
      "name": "case_39_edge_single",
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
      "name": "case_40_edge_majority_suffix",
      "input": {
        "args": [
          [
            6,
            5,
            5
          ]
        ]
      },
      "expected": 5
    }
  ]
}
```
