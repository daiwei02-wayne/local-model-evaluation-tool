# 题目78 子集

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个整数数组 `nums` ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
示例 1：
输入：nums = [1,2,3]输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：
输入：nums = [0]输出：[[],[0]]
提示：
`1 <= nums.length <= 10`
`-10 <= nums[i] <= 10`
`nums` 中的所有元素 互不相同

```json
{
  "id": 78,
  "title": "子集",
  "difficulty": "中等",
  "method": "question_78",
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
        [],
        [
          1
        ],
        [
          2
        ],
        [
          3
        ],
        [
          1,
          2
        ],
        [
          1,
          3
        ],
        [
          2,
          3
        ],
        [
          1,
          2,
          3
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_02_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        []
      ]
    },
    {
      "name": "case_03_edge_single",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [],
        [
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
        [],
        [
          1
        ],
        [
          2
        ],
        [
          3
        ],
        [
          1,
          2
        ],
        [
          1,
          3
        ],
        [
          2,
          3
        ],
        [
          1,
          2,
          3
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_05_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        []
      ]
    },
    {
      "name": "case_06_edge_single",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [],
        [
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
        [],
        [
          1
        ],
        [
          2
        ],
        [
          3
        ],
        [
          1,
          2
        ],
        [
          1,
          3
        ],
        [
          2,
          3
        ],
        [
          1,
          2,
          3
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_08_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        []
      ]
    },
    {
      "name": "case_09_edge_single",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [],
        [
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
        [],
        [
          1
        ],
        [
          2
        ],
        [
          3
        ],
        [
          1,
          2
        ],
        [
          1,
          3
        ],
        [
          2,
          3
        ],
        [
          1,
          2,
          3
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_11_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        []
      ]
    },
    {
      "name": "case_12_edge_single",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [],
        [
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
        [],
        [
          1
        ],
        [
          2
        ],
        [
          3
        ],
        [
          1,
          2
        ],
        [
          1,
          3
        ],
        [
          2,
          3
        ],
        [
          1,
          2,
          3
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_14_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        []
      ]
    },
    {
      "name": "case_15_edge_single",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [],
        [
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
        [],
        [
          1
        ],
        [
          2
        ],
        [
          3
        ],
        [
          1,
          2
        ],
        [
          1,
          3
        ],
        [
          2,
          3
        ],
        [
          1,
          2,
          3
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_17_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        []
      ]
    },
    {
      "name": "case_18_edge_single",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [],
        [
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
        [],
        [
          1
        ],
        [
          2
        ],
        [
          3
        ],
        [
          1,
          2
        ],
        [
          1,
          3
        ],
        [
          2,
          3
        ],
        [
          1,
          2,
          3
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_20_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        []
      ]
    },
    {
      "name": "case_21_edge_single",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [],
        [
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
        [],
        [
          1
        ],
        [
          2
        ],
        [
          3
        ],
        [
          1,
          2
        ],
        [
          1,
          3
        ],
        [
          2,
          3
        ],
        [
          1,
          2,
          3
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_23_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        []
      ]
    },
    {
      "name": "case_24_edge_single",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [],
        [
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
        [],
        [
          1
        ],
        [
          2
        ],
        [
          3
        ],
        [
          1,
          2
        ],
        [
          1,
          3
        ],
        [
          2,
          3
        ],
        [
          1,
          2,
          3
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_26_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        []
      ]
    },
    {
      "name": "case_27_edge_single",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [],
        [
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
        [],
        [
          1
        ],
        [
          2
        ],
        [
          3
        ],
        [
          1,
          2
        ],
        [
          1,
          3
        ],
        [
          2,
          3
        ],
        [
          1,
          2,
          3
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_29_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        []
      ]
    },
    {
      "name": "case_30_edge_single",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [],
        [
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
        [],
        [
          1
        ],
        [
          2
        ],
        [
          3
        ],
        [
          1,
          2
        ],
        [
          1,
          3
        ],
        [
          2,
          3
        ],
        [
          1,
          2,
          3
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_32_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        []
      ]
    },
    {
      "name": "case_33_edge_single",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [],
        [
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
        [],
        [
          1
        ],
        [
          2
        ],
        [
          3
        ],
        [
          1,
          2
        ],
        [
          1,
          3
        ],
        [
          2,
          3
        ],
        [
          1,
          2,
          3
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_35_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        []
      ]
    },
    {
      "name": "case_36_edge_single",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [],
        [
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
        [],
        [
          1
        ],
        [
          2
        ],
        [
          3
        ],
        [
          1,
          2
        ],
        [
          1,
          3
        ],
        [
          2,
          3
        ],
        [
          1,
          2,
          3
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_38_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        []
      ]
    },
    {
      "name": "case_39_edge_single",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [],
        [
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
        [],
        [
          1
        ],
        [
          2
        ],
        [
          3
        ],
        [
          1,
          2
        ],
        [
          1,
          3
        ],
        [
          2,
          3
        ],
        [
          1,
          2,
          3
        ]
      ],
      "comparison": "set_of_lists"
    }
  ]
}
```
