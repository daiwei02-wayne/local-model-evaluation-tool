# 题目238 除自身以外数组的乘积

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个整数数组 `nums`，返回 _数组 `answer` ，其中 `answer[i]` 等于 `nums` 中除 `nums[i]` 之外其余各元素的乘积_ 。
题目数据 保证 数组 `nums`之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
请不要使用除法，且在 `O(_n_)` 时间复杂度内完成此题。
示例 1:
输入: nums = [1,2,3,4]输出: [24,12,8,6]
示例 2:
输入: nums = [-1,1,0,-3,3]输出: [0,0,9,0,0]
提示：
2 <= nums.length <= 10<sup>5</sup>
`-30 <= nums[i] <= 30`
保证 数组 `nums`之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内
进阶：你可以在 `O(1)` 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

```json
{
  "id": 238,
  "title": "除自身以外数组的乘积",
  "difficulty": "中等",
  "method": "question_238",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ]
      },
      "expected": [
        24,
        12,
        8,
        6
      ]
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            -1,
            1,
            0,
            -3,
            3
          ]
        ]
      },
      "expected": [
        0,
        0,
        9,
        0,
        0
      ]
    },
    {
      "name": "case_03_edge_two",
      "input": {
        "args": [
          [
            1,
            2
          ]
        ]
      },
      "expected": [
        2,
        1
      ]
    },
    {
      "name": "case_04_edge_two_zeroes",
      "input": {
        "args": [
          [
            0,
            0
          ]
        ]
      },
      "expected": [
        0,
        0
      ]
    },
    {
      "name": "case_05_edge_one_zero",
      "input": {
        "args": [
          [
            0,
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        6,
        0,
        0,
        0
      ]
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ]
      },
      "expected": [
        24,
        12,
        8,
        6
      ]
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            -1,
            1,
            0,
            -3,
            3
          ]
        ]
      },
      "expected": [
        0,
        0,
        9,
        0,
        0
      ]
    },
    {
      "name": "case_08_edge_two",
      "input": {
        "args": [
          [
            1,
            2
          ]
        ]
      },
      "expected": [
        2,
        1
      ]
    },
    {
      "name": "case_09_edge_two_zeroes",
      "input": {
        "args": [
          [
            0,
            0
          ]
        ]
      },
      "expected": [
        0,
        0
      ]
    },
    {
      "name": "case_10_edge_one_zero",
      "input": {
        "args": [
          [
            0,
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        6,
        0,
        0,
        0
      ]
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ]
      },
      "expected": [
        24,
        12,
        8,
        6
      ]
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          [
            -1,
            1,
            0,
            -3,
            3
          ]
        ]
      },
      "expected": [
        0,
        0,
        9,
        0,
        0
      ]
    },
    {
      "name": "case_13_edge_two",
      "input": {
        "args": [
          [
            1,
            2
          ]
        ]
      },
      "expected": [
        2,
        1
      ]
    },
    {
      "name": "case_14_edge_two_zeroes",
      "input": {
        "args": [
          [
            0,
            0
          ]
        ]
      },
      "expected": [
        0,
        0
      ]
    },
    {
      "name": "case_15_edge_one_zero",
      "input": {
        "args": [
          [
            0,
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        6,
        0,
        0,
        0
      ]
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ]
      },
      "expected": [
        24,
        12,
        8,
        6
      ]
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            -1,
            1,
            0,
            -3,
            3
          ]
        ]
      },
      "expected": [
        0,
        0,
        9,
        0,
        0
      ]
    },
    {
      "name": "case_18_edge_two",
      "input": {
        "args": [
          [
            1,
            2
          ]
        ]
      },
      "expected": [
        2,
        1
      ]
    },
    {
      "name": "case_19_edge_two_zeroes",
      "input": {
        "args": [
          [
            0,
            0
          ]
        ]
      },
      "expected": [
        0,
        0
      ]
    },
    {
      "name": "case_20_edge_one_zero",
      "input": {
        "args": [
          [
            0,
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        6,
        0,
        0,
        0
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ]
      },
      "expected": [
        24,
        12,
        8,
        6
      ]
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            -1,
            1,
            0,
            -3,
            3
          ]
        ]
      },
      "expected": [
        0,
        0,
        9,
        0,
        0
      ]
    },
    {
      "name": "case_23_edge_two",
      "input": {
        "args": [
          [
            1,
            2
          ]
        ]
      },
      "expected": [
        2,
        1
      ]
    },
    {
      "name": "case_24_edge_two_zeroes",
      "input": {
        "args": [
          [
            0,
            0
          ]
        ]
      },
      "expected": [
        0,
        0
      ]
    },
    {
      "name": "case_25_edge_one_zero",
      "input": {
        "args": [
          [
            0,
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        6,
        0,
        0,
        0
      ]
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ]
      },
      "expected": [
        24,
        12,
        8,
        6
      ]
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          [
            -1,
            1,
            0,
            -3,
            3
          ]
        ]
      },
      "expected": [
        0,
        0,
        9,
        0,
        0
      ]
    },
    {
      "name": "case_28_edge_two",
      "input": {
        "args": [
          [
            1,
            2
          ]
        ]
      },
      "expected": [
        2,
        1
      ]
    },
    {
      "name": "case_29_edge_two_zeroes",
      "input": {
        "args": [
          [
            0,
            0
          ]
        ]
      },
      "expected": [
        0,
        0
      ]
    },
    {
      "name": "case_30_edge_one_zero",
      "input": {
        "args": [
          [
            0,
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        6,
        0,
        0,
        0
      ]
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ]
      },
      "expected": [
        24,
        12,
        8,
        6
      ]
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          [
            -1,
            1,
            0,
            -3,
            3
          ]
        ]
      },
      "expected": [
        0,
        0,
        9,
        0,
        0
      ]
    },
    {
      "name": "case_33_edge_two",
      "input": {
        "args": [
          [
            1,
            2
          ]
        ]
      },
      "expected": [
        2,
        1
      ]
    },
    {
      "name": "case_34_edge_two_zeroes",
      "input": {
        "args": [
          [
            0,
            0
          ]
        ]
      },
      "expected": [
        0,
        0
      ]
    },
    {
      "name": "case_35_edge_one_zero",
      "input": {
        "args": [
          [
            0,
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        6,
        0,
        0,
        0
      ]
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ]
      },
      "expected": [
        24,
        12,
        8,
        6
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            -1,
            1,
            0,
            -3,
            3
          ]
        ]
      },
      "expected": [
        0,
        0,
        9,
        0,
        0
      ]
    },
    {
      "name": "case_38_edge_two",
      "input": {
        "args": [
          [
            1,
            2
          ]
        ]
      },
      "expected": [
        2,
        1
      ]
    },
    {
      "name": "case_39_edge_two_zeroes",
      "input": {
        "args": [
          [
            0,
            0
          ]
        ]
      },
      "expected": [
        0,
        0
      ]
    },
    {
      "name": "case_40_edge_one_zero",
      "input": {
        "args": [
          [
            0,
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        6,
        0,
        0,
        0
      ]
    }
  ]
}
```
