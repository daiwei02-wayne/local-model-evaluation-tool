# 题目55 跳跃游戏

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一个非负整数数组 `nums` ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。
示例 1：
输入：nums = [2,3,1,1,4]输出：true解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2：
输入：nums = [3,2,1,0,4]输出：false解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
提示：
1 <= nums.length <= 3 * 10<sup>4</sup>
0 <= nums[i] <= 10<sup>5</sup>

```json
{
  "id": 55,
  "title": "跳跃游戏",
  "difficulty": "中等",
  "method": "question_55",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            2,
            3,
            1,
            1,
            4
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
            3,
            2,
            1,
            0,
            4
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_03_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_04_edge_blocked",
      "input": {
        "args": [
          [
            1,
            0,
            1
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_05_edge_exact_jump",
      "input": {
        "args": [
          [
            2,
            0,
            0
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            2,
            3,
            1,
            1,
            4
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
            3,
            2,
            1,
            0,
            4
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_08_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_09_edge_blocked",
      "input": {
        "args": [
          [
            1,
            0,
            1
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_10_edge_exact_jump",
      "input": {
        "args": [
          [
            2,
            0,
            0
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            2,
            3,
            1,
            1,
            4
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
            3,
            2,
            1,
            0,
            4
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_13_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_14_edge_blocked",
      "input": {
        "args": [
          [
            1,
            0,
            1
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_15_edge_exact_jump",
      "input": {
        "args": [
          [
            2,
            0,
            0
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            2,
            3,
            1,
            1,
            4
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
            3,
            2,
            1,
            0,
            4
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_18_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_19_edge_blocked",
      "input": {
        "args": [
          [
            1,
            0,
            1
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_20_edge_exact_jump",
      "input": {
        "args": [
          [
            2,
            0,
            0
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            2,
            3,
            1,
            1,
            4
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
            3,
            2,
            1,
            0,
            4
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_23_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_24_edge_blocked",
      "input": {
        "args": [
          [
            1,
            0,
            1
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_25_edge_exact_jump",
      "input": {
        "args": [
          [
            2,
            0,
            0
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            2,
            3,
            1,
            1,
            4
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
            3,
            2,
            1,
            0,
            4
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_28_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_29_edge_blocked",
      "input": {
        "args": [
          [
            1,
            0,
            1
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_30_edge_exact_jump",
      "input": {
        "args": [
          [
            2,
            0,
            0
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            2,
            3,
            1,
            1,
            4
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
            3,
            2,
            1,
            0,
            4
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_33_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_34_edge_blocked",
      "input": {
        "args": [
          [
            1,
            0,
            1
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_35_edge_exact_jump",
      "input": {
        "args": [
          [
            2,
            0,
            0
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          [
            2,
            3,
            1,
            1,
            4
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
            3,
            2,
            1,
            0,
            4
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_38_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_39_edge_blocked",
      "input": {
        "args": [
          [
            1,
            0,
            1
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_40_edge_exact_jump",
      "input": {
        "args": [
          [
            2,
            0,
            0
          ]
        ]
      },
      "expected": true
    }
  ]
}
```
