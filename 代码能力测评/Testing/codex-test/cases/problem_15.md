# 题目15 三数之和

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个整数数组 `nums` ，判断是否存在三元组 `[nums[i], nums[j], nums[k]]` 满足 `i != j`、`i != k` 且 `j != k` ，同时还满足 `nums[i] + nums[j] + nums[k] == 0` 。请
你返回所有和为 `0` 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例 1：
输入：nums = [-1,0,1,2,-1,-4]输出：[[-1,-1,2],[-1,0,1]]解释：nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。注意，输出的顺序和三元组的顺序并不重要。
示例 2：
输入：nums = [0,1,1]输出：[]解释：唯一可能的三元组和不为 0 。
示例 3：
输入：nums = [0,0,0]输出：[[0,0,0]]解释：唯一可能的三元组和为 0 。
提示：
`3 <= nums.length <= 3000`
-10<sup>5</sup> <= nums[i] <= 10<sup>5</sup>

```json
{
  "id": 15,
  "title": "三数之和",
  "difficulty": "中等",
  "method": "question_15",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            -1,
            0,
            1,
            2,
            -1,
            -4
          ]
        ]
      },
      "expected": [
        [
          -1,
          -1,
          2
        ],
        [
          -1,
          0,
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
            0,
            0,
            0
          ]
        ]
      },
      "expected": [
        [
          0,
          0,
          0
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_03_edge_all_zero",
      "input": {
        "args": [
          [
            0,
            0,
            0,
            0
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          0,
          0,
          0
        ]
      ]
    },
    {
      "name": "case_04_edge_duplicates",
      "input": {
        "args": [
          [
            -2,
            0,
            1,
            1,
            2
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          -2,
          0,
          2
        ],
        [
          -2,
          1,
          1
        ]
      ]
    },
    {
      "name": "case_05_edge_no_answer",
      "input": {
        "args": [
          [
            1,
            2,
            -2,
            -1
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": []
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            -1,
            0,
            1,
            2,
            -1,
            -4
          ]
        ]
      },
      "expected": [
        [
          -1,
          -1,
          2
        ],
        [
          -1,
          0,
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            0,
            0,
            0
          ]
        ]
      },
      "expected": [
        [
          0,
          0,
          0
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_08_edge_all_zero",
      "input": {
        "args": [
          [
            0,
            0,
            0,
            0
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          0,
          0,
          0
        ]
      ]
    },
    {
      "name": "case_09_edge_duplicates",
      "input": {
        "args": [
          [
            -2,
            0,
            1,
            1,
            2
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          -2,
          0,
          2
        ],
        [
          -2,
          1,
          1
        ]
      ]
    },
    {
      "name": "case_10_edge_no_answer",
      "input": {
        "args": [
          [
            1,
            2,
            -2,
            -1
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": []
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            -1,
            0,
            1,
            2,
            -1,
            -4
          ]
        ]
      },
      "expected": [
        [
          -1,
          -1,
          2
        ],
        [
          -1,
          0,
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          [
            0,
            0,
            0
          ]
        ]
      },
      "expected": [
        [
          0,
          0,
          0
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_13_edge_all_zero",
      "input": {
        "args": [
          [
            0,
            0,
            0,
            0
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          0,
          0,
          0
        ]
      ]
    },
    {
      "name": "case_14_edge_duplicates",
      "input": {
        "args": [
          [
            -2,
            0,
            1,
            1,
            2
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          -2,
          0,
          2
        ],
        [
          -2,
          1,
          1
        ]
      ]
    },
    {
      "name": "case_15_edge_no_answer",
      "input": {
        "args": [
          [
            1,
            2,
            -2,
            -1
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": []
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            -1,
            0,
            1,
            2,
            -1,
            -4
          ]
        ]
      },
      "expected": [
        [
          -1,
          -1,
          2
        ],
        [
          -1,
          0,
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
            0,
            0,
            0
          ]
        ]
      },
      "expected": [
        [
          0,
          0,
          0
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_18_edge_all_zero",
      "input": {
        "args": [
          [
            0,
            0,
            0,
            0
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          0,
          0,
          0
        ]
      ]
    },
    {
      "name": "case_19_edge_duplicates",
      "input": {
        "args": [
          [
            -2,
            0,
            1,
            1,
            2
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          -2,
          0,
          2
        ],
        [
          -2,
          1,
          1
        ]
      ]
    },
    {
      "name": "case_20_edge_no_answer",
      "input": {
        "args": [
          [
            1,
            2,
            -2,
            -1
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": []
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            -1,
            0,
            1,
            2,
            -1,
            -4
          ]
        ]
      },
      "expected": [
        [
          -1,
          -1,
          2
        ],
        [
          -1,
          0,
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            0,
            0,
            0
          ]
        ]
      },
      "expected": [
        [
          0,
          0,
          0
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_23_edge_all_zero",
      "input": {
        "args": [
          [
            0,
            0,
            0,
            0
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          0,
          0,
          0
        ]
      ]
    },
    {
      "name": "case_24_edge_duplicates",
      "input": {
        "args": [
          [
            -2,
            0,
            1,
            1,
            2
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          -2,
          0,
          2
        ],
        [
          -2,
          1,
          1
        ]
      ]
    },
    {
      "name": "case_25_edge_no_answer",
      "input": {
        "args": [
          [
            1,
            2,
            -2,
            -1
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": []
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            -1,
            0,
            1,
            2,
            -1,
            -4
          ]
        ]
      },
      "expected": [
        [
          -1,
          -1,
          2
        ],
        [
          -1,
          0,
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          [
            0,
            0,
            0
          ]
        ]
      },
      "expected": [
        [
          0,
          0,
          0
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_28_edge_all_zero",
      "input": {
        "args": [
          [
            0,
            0,
            0,
            0
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          0,
          0,
          0
        ]
      ]
    },
    {
      "name": "case_29_edge_duplicates",
      "input": {
        "args": [
          [
            -2,
            0,
            1,
            1,
            2
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          -2,
          0,
          2
        ],
        [
          -2,
          1,
          1
        ]
      ]
    },
    {
      "name": "case_30_edge_no_answer",
      "input": {
        "args": [
          [
            1,
            2,
            -2,
            -1
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": []
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            -1,
            0,
            1,
            2,
            -1,
            -4
          ]
        ]
      },
      "expected": [
        [
          -1,
          -1,
          2
        ],
        [
          -1,
          0,
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
            0,
            0,
            0
          ]
        ]
      },
      "expected": [
        [
          0,
          0,
          0
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_33_edge_all_zero",
      "input": {
        "args": [
          [
            0,
            0,
            0,
            0
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          0,
          0,
          0
        ]
      ]
    },
    {
      "name": "case_34_edge_duplicates",
      "input": {
        "args": [
          [
            -2,
            0,
            1,
            1,
            2
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          -2,
          0,
          2
        ],
        [
          -2,
          1,
          1
        ]
      ]
    },
    {
      "name": "case_35_edge_no_answer",
      "input": {
        "args": [
          [
            1,
            2,
            -2,
            -1
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": []
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          [
            -1,
            0,
            1,
            2,
            -1,
            -4
          ]
        ]
      },
      "expected": [
        [
          -1,
          -1,
          2
        ],
        [
          -1,
          0,
          1
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            0,
            0,
            0
          ]
        ]
      },
      "expected": [
        [
          0,
          0,
          0
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_38_edge_all_zero",
      "input": {
        "args": [
          [
            0,
            0,
            0,
            0
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          0,
          0,
          0
        ]
      ]
    },
    {
      "name": "case_39_edge_duplicates",
      "input": {
        "args": [
          [
            -2,
            0,
            1,
            1,
            2
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          -2,
          0,
          2
        ],
        [
          -2,
          1,
          1
        ]
      ]
    },
    {
      "name": "case_40_edge_no_answer",
      "input": {
        "args": [
          [
            1,
            2,
            -2,
            -1
          ]
        ]
      },
      "comparison": "set_of_lists",
      "expected": []
    }
  ]
}
```
