# 题目46 全排列

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一个不含重复数字的数组 `nums` ，返回其 _所有可能的全排列_ 。你可以 按任意顺序 返回答案。
示例 1：
输入：nums = [1,2,3]输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：
输入：nums = [0,1]输出：[[0,1],[1,0]]
示例 3：
输入：nums = [1]输出：[[1]]
提示：
`1 <= nums.length <= 6`
`-10 <= nums[i] <= 10`
`nums` 中的所有整数 互不相同

```json
{
  "id": 46,
  "title": "全排列",
  "difficulty": "中等",
  "method": "question_46",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        [
          1,
          2,
          3
        ],
        [
          1,
          3,
          2
        ],
        [
          2,
          1,
          3
        ],
        [
          2,
          3,
          1
        ],
        [
          3,
          1,
          2
        ],
        [
          3,
          2,
          1
        ]
      ],
      "comparison": "set_of_lists"
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
      "expected": [
        [
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_03_edge_two",
      "input": {
        "args": [
          [
            0,
            1
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          0,
          1
        ],
        [
          1,
          0
        ]
      ]
    },
    {
      "name": "case_04_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        [
          1,
          2,
          3
        ],
        [
          1,
          3,
          2
        ],
        [
          2,
          1,
          3
        ],
        [
          2,
          3,
          1
        ],
        [
          3,
          1,
          2
        ],
        [
          3,
          2,
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": [
        [
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_06_edge_two",
      "input": {
        "args": [
          [
            0,
            1
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          0,
          1
        ],
        [
          1,
          0
        ]
      ]
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        [
          1,
          2,
          3
        ],
        [
          1,
          3,
          2
        ],
        [
          2,
          1,
          3
        ],
        [
          2,
          3,
          1
        ],
        [
          3,
          1,
          2
        ],
        [
          3,
          2,
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_08_base",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": [
        [
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_09_edge_two",
      "input": {
        "args": [
          [
            0,
            1
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          0,
          1
        ],
        [
          1,
          0
        ]
      ]
    },
    {
      "name": "case_10_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        [
          1,
          2,
          3
        ],
        [
          1,
          3,
          2
        ],
        [
          2,
          1,
          3
        ],
        [
          2,
          3,
          1
        ],
        [
          3,
          1,
          2
        ],
        [
          3,
          2,
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": [
        [
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_12_edge_two",
      "input": {
        "args": [
          [
            0,
            1
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          0,
          1
        ],
        [
          1,
          0
        ]
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        [
          1,
          2,
          3
        ],
        [
          1,
          3,
          2
        ],
        [
          2,
          1,
          3
        ],
        [
          2,
          3,
          1
        ],
        [
          3,
          1,
          2
        ],
        [
          3,
          2,
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_14_base",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": [
        [
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_15_edge_two",
      "input": {
        "args": [
          [
            0,
            1
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          0,
          1
        ],
        [
          1,
          0
        ]
      ]
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        [
          1,
          2,
          3
        ],
        [
          1,
          3,
          2
        ],
        [
          2,
          1,
          3
        ],
        [
          2,
          3,
          1
        ],
        [
          3,
          1,
          2
        ],
        [
          3,
          2,
          1
        ]
      ],
      "comparison": "set_of_lists"
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
      "expected": [
        [
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_18_edge_two",
      "input": {
        "args": [
          [
            0,
            1
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          0,
          1
        ],
        [
          1,
          0
        ]
      ]
    },
    {
      "name": "case_19_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        [
          1,
          2,
          3
        ],
        [
          1,
          3,
          2
        ],
        [
          2,
          1,
          3
        ],
        [
          2,
          3,
          1
        ],
        [
          3,
          1,
          2
        ],
        [
          3,
          2,
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_20_base",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": [
        [
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_21_edge_two",
      "input": {
        "args": [
          [
            0,
            1
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          0,
          1
        ],
        [
          1,
          0
        ]
      ]
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        [
          1,
          2,
          3
        ],
        [
          1,
          3,
          2
        ],
        [
          2,
          1,
          3
        ],
        [
          2,
          3,
          1
        ],
        [
          3,
          1,
          2
        ],
        [
          3,
          2,
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_23_base",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": [
        [
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_24_edge_two",
      "input": {
        "args": [
          [
            0,
            1
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          0,
          1
        ],
        [
          1,
          0
        ]
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        [
          1,
          2,
          3
        ],
        [
          1,
          3,
          2
        ],
        [
          2,
          1,
          3
        ],
        [
          2,
          3,
          1
        ],
        [
          3,
          1,
          2
        ],
        [
          3,
          2,
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": [
        [
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_27_edge_two",
      "input": {
        "args": [
          [
            0,
            1
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          0,
          1
        ],
        [
          1,
          0
        ]
      ]
    },
    {
      "name": "case_28_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        [
          1,
          2,
          3
        ],
        [
          1,
          3,
          2
        ],
        [
          2,
          1,
          3
        ],
        [
          2,
          3,
          1
        ],
        [
          3,
          1,
          2
        ],
        [
          3,
          2,
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": [
        [
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_30_edge_two",
      "input": {
        "args": [
          [
            0,
            1
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          0,
          1
        ],
        [
          1,
          0
        ]
      ]
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        [
          1,
          2,
          3
        ],
        [
          1,
          3,
          2
        ],
        [
          2,
          1,
          3
        ],
        [
          2,
          3,
          1
        ],
        [
          3,
          1,
          2
        ],
        [
          3,
          2,
          1
        ]
      ],
      "comparison": "set_of_lists"
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
      "expected": [
        [
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_33_edge_two",
      "input": {
        "args": [
          [
            0,
            1
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          0,
          1
        ],
        [
          1,
          0
        ]
      ]
    },
    {
      "name": "case_34_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        [
          1,
          2,
          3
        ],
        [
          1,
          3,
          2
        ],
        [
          2,
          1,
          3
        ],
        [
          2,
          3,
          1
        ],
        [
          3,
          1,
          2
        ],
        [
          3,
          2,
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_35_base",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": [
        [
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_36_edge_two",
      "input": {
        "args": [
          [
            0,
            1
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          0,
          1
        ],
        [
          1,
          0
        ]
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        [
          1,
          2,
          3
        ],
        [
          1,
          3,
          2
        ],
        [
          2,
          1,
          3
        ],
        [
          2,
          3,
          1
        ],
        [
          3,
          1,
          2
        ],
        [
          3,
          2,
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": [
        [
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_39_edge_two",
      "input": {
        "args": [
          [
            0,
            1
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          0,
          1
        ],
        [
          1,
          0
        ]
      ]
    },
    {
      "name": "case_40_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        [
          1,
          2,
          3
        ],
        [
          1,
          3,
          2
        ],
        [
          2,
          1,
          3
        ],
        [
          2,
          3,
          1
        ],
        [
          3,
          1,
          2
        ],
        [
          3,
          2,
          1
        ]
      ],
      "comparison": "set_of_lists"
    }
  ]
}
```
