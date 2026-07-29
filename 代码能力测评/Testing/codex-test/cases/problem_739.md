# 题目739 每日温度

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一个整数数组 `temperatures` ，表示每天的温度，返回一个数组 `answer` ，其中 `answer[i]` 是指对于第 `i` 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 `0` 来代替。
示例 1:
输入: temperatures = [73,74,75,71,69,72,76,73]输出: [1,1,4,2,1,1,0,0]
示例 2:
输入: temperatures = [30,40,50,60]输出: [1,1,1,0]
示例 3:
输入: temperatures = [30,60,90]输出: [1,1,0]
提示：
1 <= temperatures.length <= 10<sup>5</sup>
`30 <= temperatures[i] <= 100`

```json
{
  "id": 739,
  "title": "每日温度",
  "difficulty": "中等",
  "method": "question_739",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            73,
            74,
            75,
            71,
            69,
            72,
            76,
            73
          ]
        ]
      },
      "expected": [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0
      ]
    },
    {
      "name": "case_02_edge_single",
      "input": {
        "args": [
          [
            30
          ]
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_03_edge_decreasing",
      "input": {
        "args": [
          [
            30,
            29,
            28
          ]
        ]
      },
      "expected": [
        0,
        0,
        0
      ]
    },
    {
      "name": "case_04_edge_increasing",
      "input": {
        "args": [
          [
            30,
            40,
            50,
            60
          ]
        ]
      },
      "expected": [
        1,
        1,
        1,
        0
      ]
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          [
            73,
            74,
            75,
            71,
            69,
            72,
            76,
            73
          ]
        ]
      },
      "expected": [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0
      ]
    },
    {
      "name": "case_06_edge_single",
      "input": {
        "args": [
          [
            30
          ]
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_07_edge_decreasing",
      "input": {
        "args": [
          [
            30,
            29,
            28
          ]
        ]
      },
      "expected": [
        0,
        0,
        0
      ]
    },
    {
      "name": "case_08_edge_increasing",
      "input": {
        "args": [
          [
            30,
            40,
            50,
            60
          ]
        ]
      },
      "expected": [
        1,
        1,
        1,
        0
      ]
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          [
            73,
            74,
            75,
            71,
            69,
            72,
            76,
            73
          ]
        ]
      },
      "expected": [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0
      ]
    },
    {
      "name": "case_10_edge_single",
      "input": {
        "args": [
          [
            30
          ]
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_11_edge_decreasing",
      "input": {
        "args": [
          [
            30,
            29,
            28
          ]
        ]
      },
      "expected": [
        0,
        0,
        0
      ]
    },
    {
      "name": "case_12_edge_increasing",
      "input": {
        "args": [
          [
            30,
            40,
            50,
            60
          ]
        ]
      },
      "expected": [
        1,
        1,
        1,
        0
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [
            73,
            74,
            75,
            71,
            69,
            72,
            76,
            73
          ]
        ]
      },
      "expected": [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0
      ]
    },
    {
      "name": "case_14_edge_single",
      "input": {
        "args": [
          [
            30
          ]
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_15_edge_decreasing",
      "input": {
        "args": [
          [
            30,
            29,
            28
          ]
        ]
      },
      "expected": [
        0,
        0,
        0
      ]
    },
    {
      "name": "case_16_edge_increasing",
      "input": {
        "args": [
          [
            30,
            40,
            50,
            60
          ]
        ]
      },
      "expected": [
        1,
        1,
        1,
        0
      ]
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            73,
            74,
            75,
            71,
            69,
            72,
            76,
            73
          ]
        ]
      },
      "expected": [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0
      ]
    },
    {
      "name": "case_18_edge_single",
      "input": {
        "args": [
          [
            30
          ]
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_19_edge_decreasing",
      "input": {
        "args": [
          [
            30,
            29,
            28
          ]
        ]
      },
      "expected": [
        0,
        0,
        0
      ]
    },
    {
      "name": "case_20_edge_increasing",
      "input": {
        "args": [
          [
            30,
            40,
            50,
            60
          ]
        ]
      },
      "expected": [
        1,
        1,
        1,
        0
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            73,
            74,
            75,
            71,
            69,
            72,
            76,
            73
          ]
        ]
      },
      "expected": [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0
      ]
    },
    {
      "name": "case_22_edge_single",
      "input": {
        "args": [
          [
            30
          ]
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_23_edge_decreasing",
      "input": {
        "args": [
          [
            30,
            29,
            28
          ]
        ]
      },
      "expected": [
        0,
        0,
        0
      ]
    },
    {
      "name": "case_24_edge_increasing",
      "input": {
        "args": [
          [
            30,
            40,
            50,
            60
          ]
        ]
      },
      "expected": [
        1,
        1,
        1,
        0
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            73,
            74,
            75,
            71,
            69,
            72,
            76,
            73
          ]
        ]
      },
      "expected": [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0
      ]
    },
    {
      "name": "case_26_edge_single",
      "input": {
        "args": [
          [
            30
          ]
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_27_edge_decreasing",
      "input": {
        "args": [
          [
            30,
            29,
            28
          ]
        ]
      },
      "expected": [
        0,
        0,
        0
      ]
    },
    {
      "name": "case_28_edge_increasing",
      "input": {
        "args": [
          [
            30,
            40,
            50,
            60
          ]
        ]
      },
      "expected": [
        1,
        1,
        1,
        0
      ]
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          [
            73,
            74,
            75,
            71,
            69,
            72,
            76,
            73
          ]
        ]
      },
      "expected": [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0
      ]
    },
    {
      "name": "case_30_edge_single",
      "input": {
        "args": [
          [
            30
          ]
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_31_edge_decreasing",
      "input": {
        "args": [
          [
            30,
            29,
            28
          ]
        ]
      },
      "expected": [
        0,
        0,
        0
      ]
    },
    {
      "name": "case_32_edge_increasing",
      "input": {
        "args": [
          [
            30,
            40,
            50,
            60
          ]
        ]
      },
      "expected": [
        1,
        1,
        1,
        0
      ]
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          [
            73,
            74,
            75,
            71,
            69,
            72,
            76,
            73
          ]
        ]
      },
      "expected": [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0
      ]
    },
    {
      "name": "case_34_edge_single",
      "input": {
        "args": [
          [
            30
          ]
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_35_edge_decreasing",
      "input": {
        "args": [
          [
            30,
            29,
            28
          ]
        ]
      },
      "expected": [
        0,
        0,
        0
      ]
    },
    {
      "name": "case_36_edge_increasing",
      "input": {
        "args": [
          [
            30,
            40,
            50,
            60
          ]
        ]
      },
      "expected": [
        1,
        1,
        1,
        0
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            73,
            74,
            75,
            71,
            69,
            72,
            76,
            73
          ]
        ]
      },
      "expected": [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0
      ]
    },
    {
      "name": "case_38_edge_single",
      "input": {
        "args": [
          [
            30
          ]
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_39_edge_decreasing",
      "input": {
        "args": [
          [
            30,
            29,
            28
          ]
        ]
      },
      "expected": [
        0,
        0,
        0
      ]
    },
    {
      "name": "case_40_edge_increasing",
      "input": {
        "args": [
          [
            30,
            40,
            50,
            60
          ]
        ]
      },
      "expected": [
        1,
        1,
        1,
        0
      ]
    }
  ]
}
```
