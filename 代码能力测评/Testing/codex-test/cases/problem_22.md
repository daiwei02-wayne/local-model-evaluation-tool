# 题目22 括号生成

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

数字 `n` 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
示例 1：
输入：n = 3输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：
输入：n = 1输出：["()"]
提示：
`1 <= n <= 8`

```json
{
  "id": 22,
  "title": "括号生成",
  "difficulty": "中等",
  "method": "question_22",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          3
        ]
      },
      "expected": [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          1
        ]
      },
      "expected": [
        "()"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_03_edge_zero",
      "input": {
        "args": [
          0
        ]
      },
      "comparison": "any_order",
      "expected": [
        ""
      ]
    },
    {
      "name": "case_04_edge_two",
      "input": {
        "args": [
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        "(())",
        "()()"
      ]
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          3
        ]
      },
      "expected": [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          1
        ]
      },
      "expected": [
        "()"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_07_edge_zero",
      "input": {
        "args": [
          0
        ]
      },
      "comparison": "any_order",
      "expected": [
        ""
      ]
    },
    {
      "name": "case_08_edge_two",
      "input": {
        "args": [
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        "(())",
        "()()"
      ]
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          3
        ]
      },
      "expected": [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_10_base",
      "input": {
        "args": [
          1
        ]
      },
      "expected": [
        "()"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_11_edge_zero",
      "input": {
        "args": [
          0
        ]
      },
      "comparison": "any_order",
      "expected": [
        ""
      ]
    },
    {
      "name": "case_12_edge_two",
      "input": {
        "args": [
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        "(())",
        "()()"
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          3
        ]
      },
      "expected": [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_14_base",
      "input": {
        "args": [
          1
        ]
      },
      "expected": [
        "()"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_15_edge_zero",
      "input": {
        "args": [
          0
        ]
      },
      "comparison": "any_order",
      "expected": [
        ""
      ]
    },
    {
      "name": "case_16_edge_two",
      "input": {
        "args": [
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        "(())",
        "()()"
      ]
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          3
        ]
      },
      "expected": [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_18_base",
      "input": {
        "args": [
          1
        ]
      },
      "expected": [
        "()"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_19_edge_zero",
      "input": {
        "args": [
          0
        ]
      },
      "comparison": "any_order",
      "expected": [
        ""
      ]
    },
    {
      "name": "case_20_edge_two",
      "input": {
        "args": [
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        "(())",
        "()()"
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          3
        ]
      },
      "expected": [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          1
        ]
      },
      "expected": [
        "()"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_23_edge_zero",
      "input": {
        "args": [
          0
        ]
      },
      "comparison": "any_order",
      "expected": [
        ""
      ]
    },
    {
      "name": "case_24_edge_two",
      "input": {
        "args": [
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        "(())",
        "()()"
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          3
        ]
      },
      "expected": [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          1
        ]
      },
      "expected": [
        "()"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_27_edge_zero",
      "input": {
        "args": [
          0
        ]
      },
      "comparison": "any_order",
      "expected": [
        ""
      ]
    },
    {
      "name": "case_28_edge_two",
      "input": {
        "args": [
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        "(())",
        "()()"
      ]
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          3
        ]
      },
      "expected": [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_30_base",
      "input": {
        "args": [
          1
        ]
      },
      "expected": [
        "()"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_31_edge_zero",
      "input": {
        "args": [
          0
        ]
      },
      "comparison": "any_order",
      "expected": [
        ""
      ]
    },
    {
      "name": "case_32_edge_two",
      "input": {
        "args": [
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        "(())",
        "()()"
      ]
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          3
        ]
      },
      "expected": [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_34_base",
      "input": {
        "args": [
          1
        ]
      },
      "expected": [
        "()"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_35_edge_zero",
      "input": {
        "args": [
          0
        ]
      },
      "comparison": "any_order",
      "expected": [
        ""
      ]
    },
    {
      "name": "case_36_edge_two",
      "input": {
        "args": [
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        "(())",
        "()()"
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          3
        ]
      },
      "expected": [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          1
        ]
      },
      "expected": [
        "()"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_39_edge_zero",
      "input": {
        "args": [
          0
        ]
      },
      "comparison": "any_order",
      "expected": [
        ""
      ]
    },
    {
      "name": "case_40_edge_two",
      "input": {
        "args": [
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        "(())",
        "()()"
      ]
    }
  ]
}
```
