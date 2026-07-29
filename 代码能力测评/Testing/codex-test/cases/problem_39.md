# 题目39 组合总和

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个 无重复元素 的整数数组 `candidates` 和一个目标整数 `target` ，找出 `candidates` 中可以使数字和为目标数 `target` 的 _所有 _不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
`candidates` 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。
对于给定的输入，保证和为 `target` 的不同组合数少于 `150` 个。
示例 1：
输入：candidates = [2,3,6,7], target = 7输出：[[2,2,3],[7]]解释：2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。7 也是一个候选， 7 = 7 。仅有这两种组合。
示例 2：
输入: candidates = [2,3,5], target = 8输出: [[2,2,2,2],[2,3,3],[3,5]]
示例 3：
输入: candidates = [2], target = 1输出: []
提示：
`1 <= candidates.length <= 30`
`1 <= candidates[i] <= 200`
`candidate` 中的每个元素都 互不相同
`1 <= target <= 500`

```json
{
  "id": 39,
  "title": "组合总和",
  "difficulty": "中等",
  "method": "question_39",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            2,
            3,
            6,
            7
          ],
          7
        ]
      },
      "expected": [
        [
          2,
          2,
          3
        ],
        [
          7
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            2,
            3,
            5
          ],
          8
        ]
      },
      "expected": [
        [
          2,
          2,
          2,
          2
        ],
        [
          2,
          3,
          3
        ],
        [
          3,
          5
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_03_edge_no_combo",
      "input": {
        "args": [
          [
            2
          ],
          1
        ]
      },
      "comparison": "set_of_lists",
      "expected": []
    },
    {
      "name": "case_04_edge_one_candidate_reuse",
      "input": {
        "args": [
          [
            1
          ],
          2
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          1,
          1
        ]
      ]
    },
    {
      "name": "case_05_edge_unsorted",
      "input": {
        "args": [
          [
            7,
            3,
            2
          ],
          18
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2
        ],
        [
          2,
          2,
          2,
          2,
          2,
          2,
          3,
          3
        ],
        [
          2,
          2,
          2,
          2,
          3,
          7
        ],
        [
          2,
          2,
          2,
          3,
          3,
          3,
          3
        ],
        [
          2,
          2,
          7,
          7
        ],
        [
          2,
          3,
          3,
          3,
          7
        ],
        [
          3,
          3,
          3,
          3,
          3,
          3
        ]
      ]
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            2,
            3,
            6,
            7
          ],
          7
        ]
      },
      "expected": [
        [
          2,
          2,
          3
        ],
        [
          7
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            2,
            3,
            5
          ],
          8
        ]
      },
      "expected": [
        [
          2,
          2,
          2,
          2
        ],
        [
          2,
          3,
          3
        ],
        [
          3,
          5
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_08_edge_no_combo",
      "input": {
        "args": [
          [
            2
          ],
          1
        ]
      },
      "comparison": "set_of_lists",
      "expected": []
    },
    {
      "name": "case_09_edge_one_candidate_reuse",
      "input": {
        "args": [
          [
            1
          ],
          2
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          1,
          1
        ]
      ]
    },
    {
      "name": "case_10_edge_unsorted",
      "input": {
        "args": [
          [
            7,
            3,
            2
          ],
          18
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2
        ],
        [
          2,
          2,
          2,
          2,
          2,
          2,
          3,
          3
        ],
        [
          2,
          2,
          2,
          2,
          3,
          7
        ],
        [
          2,
          2,
          2,
          3,
          3,
          3,
          3
        ],
        [
          2,
          2,
          7,
          7
        ],
        [
          2,
          3,
          3,
          3,
          7
        ],
        [
          3,
          3,
          3,
          3,
          3,
          3
        ]
      ]
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            2,
            3,
            6,
            7
          ],
          7
        ]
      },
      "expected": [
        [
          2,
          2,
          3
        ],
        [
          7
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          [
            2,
            3,
            5
          ],
          8
        ]
      },
      "expected": [
        [
          2,
          2,
          2,
          2
        ],
        [
          2,
          3,
          3
        ],
        [
          3,
          5
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_13_edge_no_combo",
      "input": {
        "args": [
          [
            2
          ],
          1
        ]
      },
      "comparison": "set_of_lists",
      "expected": []
    },
    {
      "name": "case_14_edge_one_candidate_reuse",
      "input": {
        "args": [
          [
            1
          ],
          2
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          1,
          1
        ]
      ]
    },
    {
      "name": "case_15_edge_unsorted",
      "input": {
        "args": [
          [
            7,
            3,
            2
          ],
          18
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2
        ],
        [
          2,
          2,
          2,
          2,
          2,
          2,
          3,
          3
        ],
        [
          2,
          2,
          2,
          2,
          3,
          7
        ],
        [
          2,
          2,
          2,
          3,
          3,
          3,
          3
        ],
        [
          2,
          2,
          7,
          7
        ],
        [
          2,
          3,
          3,
          3,
          7
        ],
        [
          3,
          3,
          3,
          3,
          3,
          3
        ]
      ]
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            2,
            3,
            6,
            7
          ],
          7
        ]
      },
      "expected": [
        [
          2,
          2,
          3
        ],
        [
          7
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            2,
            3,
            5
          ],
          8
        ]
      },
      "expected": [
        [
          2,
          2,
          2,
          2
        ],
        [
          2,
          3,
          3
        ],
        [
          3,
          5
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_18_edge_no_combo",
      "input": {
        "args": [
          [
            2
          ],
          1
        ]
      },
      "comparison": "set_of_lists",
      "expected": []
    },
    {
      "name": "case_19_edge_one_candidate_reuse",
      "input": {
        "args": [
          [
            1
          ],
          2
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          1,
          1
        ]
      ]
    },
    {
      "name": "case_20_edge_unsorted",
      "input": {
        "args": [
          [
            7,
            3,
            2
          ],
          18
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2
        ],
        [
          2,
          2,
          2,
          2,
          2,
          2,
          3,
          3
        ],
        [
          2,
          2,
          2,
          2,
          3,
          7
        ],
        [
          2,
          2,
          2,
          3,
          3,
          3,
          3
        ],
        [
          2,
          2,
          7,
          7
        ],
        [
          2,
          3,
          3,
          3,
          7
        ],
        [
          3,
          3,
          3,
          3,
          3,
          3
        ]
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            2,
            3,
            6,
            7
          ],
          7
        ]
      },
      "expected": [
        [
          2,
          2,
          3
        ],
        [
          7
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            2,
            3,
            5
          ],
          8
        ]
      },
      "expected": [
        [
          2,
          2,
          2,
          2
        ],
        [
          2,
          3,
          3
        ],
        [
          3,
          5
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_23_edge_no_combo",
      "input": {
        "args": [
          [
            2
          ],
          1
        ]
      },
      "comparison": "set_of_lists",
      "expected": []
    },
    {
      "name": "case_24_edge_one_candidate_reuse",
      "input": {
        "args": [
          [
            1
          ],
          2
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          1,
          1
        ]
      ]
    },
    {
      "name": "case_25_edge_unsorted",
      "input": {
        "args": [
          [
            7,
            3,
            2
          ],
          18
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2
        ],
        [
          2,
          2,
          2,
          2,
          2,
          2,
          3,
          3
        ],
        [
          2,
          2,
          2,
          2,
          3,
          7
        ],
        [
          2,
          2,
          2,
          3,
          3,
          3,
          3
        ],
        [
          2,
          2,
          7,
          7
        ],
        [
          2,
          3,
          3,
          3,
          7
        ],
        [
          3,
          3,
          3,
          3,
          3,
          3
        ]
      ]
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            2,
            3,
            6,
            7
          ],
          7
        ]
      },
      "expected": [
        [
          2,
          2,
          3
        ],
        [
          7
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          [
            2,
            3,
            5
          ],
          8
        ]
      },
      "expected": [
        [
          2,
          2,
          2,
          2
        ],
        [
          2,
          3,
          3
        ],
        [
          3,
          5
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_28_edge_no_combo",
      "input": {
        "args": [
          [
            2
          ],
          1
        ]
      },
      "comparison": "set_of_lists",
      "expected": []
    },
    {
      "name": "case_29_edge_one_candidate_reuse",
      "input": {
        "args": [
          [
            1
          ],
          2
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          1,
          1
        ]
      ]
    },
    {
      "name": "case_30_edge_unsorted",
      "input": {
        "args": [
          [
            7,
            3,
            2
          ],
          18
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2
        ],
        [
          2,
          2,
          2,
          2,
          2,
          2,
          3,
          3
        ],
        [
          2,
          2,
          2,
          2,
          3,
          7
        ],
        [
          2,
          2,
          2,
          3,
          3,
          3,
          3
        ],
        [
          2,
          2,
          7,
          7
        ],
        [
          2,
          3,
          3,
          3,
          7
        ],
        [
          3,
          3,
          3,
          3,
          3,
          3
        ]
      ]
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            2,
            3,
            6,
            7
          ],
          7
        ]
      },
      "expected": [
        [
          2,
          2,
          3
        ],
        [
          7
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          [
            2,
            3,
            5
          ],
          8
        ]
      },
      "expected": [
        [
          2,
          2,
          2,
          2
        ],
        [
          2,
          3,
          3
        ],
        [
          3,
          5
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_33_edge_no_combo",
      "input": {
        "args": [
          [
            2
          ],
          1
        ]
      },
      "comparison": "set_of_lists",
      "expected": []
    },
    {
      "name": "case_34_edge_one_candidate_reuse",
      "input": {
        "args": [
          [
            1
          ],
          2
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          1,
          1
        ]
      ]
    },
    {
      "name": "case_35_edge_unsorted",
      "input": {
        "args": [
          [
            7,
            3,
            2
          ],
          18
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2
        ],
        [
          2,
          2,
          2,
          2,
          2,
          2,
          3,
          3
        ],
        [
          2,
          2,
          2,
          2,
          3,
          7
        ],
        [
          2,
          2,
          2,
          3,
          3,
          3,
          3
        ],
        [
          2,
          2,
          7,
          7
        ],
        [
          2,
          3,
          3,
          3,
          7
        ],
        [
          3,
          3,
          3,
          3,
          3,
          3
        ]
      ]
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          [
            2,
            3,
            6,
            7
          ],
          7
        ]
      },
      "expected": [
        [
          2,
          2,
          3
        ],
        [
          7
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            2,
            3,
            5
          ],
          8
        ]
      },
      "expected": [
        [
          2,
          2,
          2,
          2
        ],
        [
          2,
          3,
          3
        ],
        [
          3,
          5
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_38_edge_no_combo",
      "input": {
        "args": [
          [
            2
          ],
          1
        ]
      },
      "comparison": "set_of_lists",
      "expected": []
    },
    {
      "name": "case_39_edge_one_candidate_reuse",
      "input": {
        "args": [
          [
            1
          ],
          2
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          1,
          1
        ]
      ]
    },
    {
      "name": "case_40_edge_unsorted",
      "input": {
        "args": [
          [
            7,
            3,
            2
          ],
          18
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2,
          2
        ],
        [
          2,
          2,
          2,
          2,
          2,
          2,
          3,
          3
        ],
        [
          2,
          2,
          2,
          2,
          3,
          7
        ],
        [
          2,
          2,
          2,
          3,
          3,
          3,
          3
        ],
        [
          2,
          2,
          7,
          7
        ],
        [
          2,
          3,
          3,
          3,
          7
        ],
        [
          3,
          3,
          3,
          3,
          3,
          3
        ]
      ]
    }
  ]
}
```
