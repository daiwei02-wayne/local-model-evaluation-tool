# 题目198 打家劫舍

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
示例 1：
输入：[1,2,3,1]输出：4解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：
输入：[2,7,9,3,1]输出：12解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
提示：
`1 <= nums.length <= 100`
`0 <= nums[i] <= 400`

```json
{
  "id": 198,
  "title": "打家劫舍",
  "difficulty": "中等",
  "method": "question_198",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            1
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            2,
            7,
            9,
            3,
            1
          ]
        ]
      },
      "expected": 12
    },
    {
      "name": "case_03_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
    },
    {
      "name": "case_04_edge_single",
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
      "name": "case_05_edge_choose_ends",
      "input": {
        "args": [
          [
            2,
            1,
            1,
            2
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
            2,
            3,
            1
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            2,
            7,
            9,
            3,
            1
          ]
        ]
      },
      "expected": 12
    },
    {
      "name": "case_08_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
    },
    {
      "name": "case_09_edge_single",
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
      "name": "case_10_edge_choose_ends",
      "input": {
        "args": [
          [
            2,
            1,
            1,
            2
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
            2,
            3,
            1
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          [
            2,
            7,
            9,
            3,
            1
          ]
        ]
      },
      "expected": 12
    },
    {
      "name": "case_13_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
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
      "name": "case_15_edge_choose_ends",
      "input": {
        "args": [
          [
            2,
            1,
            1,
            2
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
            2,
            3,
            1
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            2,
            7,
            9,
            3,
            1
          ]
        ]
      },
      "expected": 12
    },
    {
      "name": "case_18_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
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
      "name": "case_20_edge_choose_ends",
      "input": {
        "args": [
          [
            2,
            1,
            1,
            2
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
            2,
            3,
            1
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            2,
            7,
            9,
            3,
            1
          ]
        ]
      },
      "expected": 12
    },
    {
      "name": "case_23_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
    },
    {
      "name": "case_24_edge_single",
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
      "name": "case_25_edge_choose_ends",
      "input": {
        "args": [
          [
            2,
            1,
            1,
            2
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
            2,
            3,
            1
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          [
            2,
            7,
            9,
            3,
            1
          ]
        ]
      },
      "expected": 12
    },
    {
      "name": "case_28_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
    },
    {
      "name": "case_29_edge_single",
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
      "name": "case_30_edge_choose_ends",
      "input": {
        "args": [
          [
            2,
            1,
            1,
            2
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
            2,
            3,
            1
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          [
            2,
            7,
            9,
            3,
            1
          ]
        ]
      },
      "expected": 12
    },
    {
      "name": "case_33_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
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
      "name": "case_35_edge_choose_ends",
      "input": {
        "args": [
          [
            2,
            1,
            1,
            2
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
            2,
            3,
            1
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            2,
            7,
            9,
            3,
            1
          ]
        ]
      },
      "expected": 12
    },
    {
      "name": "case_38_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
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
      "name": "case_40_edge_choose_ends",
      "input": {
        "args": [
          [
            2,
            1,
            1,
            2
          ]
        ]
      },
      "expected": 4
    }
  ]
}
```
