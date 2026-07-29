# 题目136 只出现一次的数字

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
示例 1:
输入: [2,2,1]输出: 1
示例 2:
输入: [4,1,2,1,2]输出: 4

```json
{
  "id": 136,
  "title": "只出现一次的数字",
  "difficulty": "简单",
  "method": "question_136",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            2,
            2,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            4,
            1,
            2,
            1,
            2
          ]
        ]
      },
      "expected": 4
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
      "name": "case_04_edge_zero",
      "input": {
        "args": [
          [
            0,
            1,
            0
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_05_edge_negative",
      "input": {
        "args": [
          [
            -1,
            2,
            2
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            2,
            2,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            4,
            1,
            2,
            1,
            2
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_08_edge_single",
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
      "name": "case_09_edge_zero",
      "input": {
        "args": [
          [
            0,
            1,
            0
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_10_edge_negative",
      "input": {
        "args": [
          [
            -1,
            2,
            2
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            2,
            2,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          [
            4,
            1,
            2,
            1,
            2
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_13_edge_single",
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
      "name": "case_14_edge_zero",
      "input": {
        "args": [
          [
            0,
            1,
            0
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_15_edge_negative",
      "input": {
        "args": [
          [
            -1,
            2,
            2
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            2,
            2,
            1
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
            4,
            1,
            2,
            1,
            2
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
      "name": "case_19_edge_zero",
      "input": {
        "args": [
          [
            0,
            1,
            0
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_20_edge_negative",
      "input": {
        "args": [
          [
            -1,
            2,
            2
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            2,
            2,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            4,
            1,
            2,
            1,
            2
          ]
        ]
      },
      "expected": 4
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
      "name": "case_24_edge_zero",
      "input": {
        "args": [
          [
            0,
            1,
            0
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_25_edge_negative",
      "input": {
        "args": [
          [
            -1,
            2,
            2
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            2,
            2,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          [
            4,
            1,
            2,
            1,
            2
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_28_edge_single",
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
      "name": "case_29_edge_zero",
      "input": {
        "args": [
          [
            0,
            1,
            0
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_30_edge_negative",
      "input": {
        "args": [
          [
            -1,
            2,
            2
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            2,
            2,
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          [
            4,
            1,
            2,
            1,
            2
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_33_edge_single",
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
      "name": "case_34_edge_zero",
      "input": {
        "args": [
          [
            0,
            1,
            0
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_35_edge_negative",
      "input": {
        "args": [
          [
            -1,
            2,
            2
          ]
        ]
      },
      "expected": -1
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          [
            2,
            2,
            1
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
            4,
            1,
            2,
            1,
            2
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
      "name": "case_39_edge_zero",
      "input": {
        "args": [
          [
            0,
            1,
            0
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_40_edge_negative",
      "input": {
        "args": [
          [
            -1,
            2,
            2
          ]
        ]
      },
      "expected": -1
    }
  ]
}
```
