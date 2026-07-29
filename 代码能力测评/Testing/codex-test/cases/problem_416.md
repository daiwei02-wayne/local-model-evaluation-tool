# 题目416 分割等和子集

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个 只包含正整数 的 非空 数组 `nums` 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
示例 1：
输入：nums = [1,5,11,5]输出：true解释：数组可以分割成 [1, 5, 5] 和 [11] 。
示例 2：
输入：nums = [1,2,3,5]输出：false解释：数组不能分割成两个元素和相等的子集。
提示：
`1 <= nums.length <= 200`
`1 <= nums[i] <= 100`

```json
{
  "id": 416,
  "title": "分割等和子集",
  "difficulty": "中等",
  "method": "question_416",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            1,
            5,
            11,
            5
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            5
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_03_edge_single_false",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_04_edge_two_true",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_05_edge_false_even_sum",
      "input": {
        "args": [
          [
            2,
            2,
            3,
            5
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            1,
            5,
            11,
            5
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            5
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_08_edge_single_false",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_09_edge_two_true",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_10_edge_false_even_sum",
      "input": {
        "args": [
          [
            2,
            2,
            3,
            5
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            1,
            5,
            11,
            5
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            5
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_13_edge_single_false",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_14_edge_two_true",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_15_edge_false_even_sum",
      "input": {
        "args": [
          [
            2,
            2,
            3,
            5
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            1,
            5,
            11,
            5
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            5
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_18_edge_single_false",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_19_edge_two_true",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_20_edge_false_even_sum",
      "input": {
        "args": [
          [
            2,
            2,
            3,
            5
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            1,
            5,
            11,
            5
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            5
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_23_edge_single_false",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_24_edge_two_true",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_25_edge_false_even_sum",
      "input": {
        "args": [
          [
            2,
            2,
            3,
            5
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            1,
            5,
            11,
            5
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            5
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_28_edge_single_false",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_29_edge_two_true",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_30_edge_false_even_sum",
      "input": {
        "args": [
          [
            2,
            2,
            3,
            5
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            1,
            5,
            11,
            5
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            5
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_33_edge_single_false",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_34_edge_two_true",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_35_edge_false_even_sum",
      "input": {
        "args": [
          [
            2,
            2,
            3,
            5
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          [
            1,
            5,
            11,
            5
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            5
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_38_edge_single_false",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_39_edge_two_true",
      "input": {
        "args": [
          [
            1,
            1
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_40_edge_false_even_sum",
      "input": {
        "args": [
          [
            2,
            2,
            3,
            5
          ]
        ]
      },
      "expected": false
    }
  ]
}
```
