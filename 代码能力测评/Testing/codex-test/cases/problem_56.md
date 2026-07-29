# 题目56 合并区间

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

以数组 `intervals` 表示若干个区间的集合，其中单个区间为 intervals[i] = [start<sub>i</sub>, end<sub>i</sub>] 。请你合并所有重叠的区间，并返回 _一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间_ 。
示例 1：
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]输出：[[1,6],[8,10],[15,18]]解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：
输入：intervals = [[1,4],[4,5]]输出：[[1,5]]解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
提示：
1 <= intervals.length <= 10<sup>4</sup>
`intervals[i].length == 2`
0 <= start<sub>i</sub> <= end<sub>i</sub> <= 10<sup>4</sup>

```json
{
  "id": 56,
  "title": "合并区间",
  "difficulty": "中等",
  "method": "question_56",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            [
              1,
              3
            ],
            [
              2,
              6
            ],
            [
              8,
              10
            ],
            [
              15,
              18
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          6
        ],
        [
          8,
          10
        ],
        [
          15,
          18
        ]
      ]
    },
    {
      "name": "case_02_edge_touching",
      "input": {
        "args": [
          [
            [
              1,
              4
            ],
            [
              4,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          5
        ]
      ]
    },
    {
      "name": "case_03_edge_nested_overlap",
      "input": {
        "args": [
          [
            [
              1,
              4
            ],
            [
              0,
              2
            ],
            [
              3,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          0,
          5
        ]
      ]
    },
    {
      "name": "case_04_edge_single",
      "input": {
        "args": [
          [
            [
              1,
              2
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          2
        ]
      ]
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          [
            [
              1,
              3
            ],
            [
              2,
              6
            ],
            [
              8,
              10
            ],
            [
              15,
              18
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          6
        ],
        [
          8,
          10
        ],
        [
          15,
          18
        ]
      ]
    },
    {
      "name": "case_06_edge_touching",
      "input": {
        "args": [
          [
            [
              1,
              4
            ],
            [
              4,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          5
        ]
      ]
    },
    {
      "name": "case_07_edge_nested_overlap",
      "input": {
        "args": [
          [
            [
              1,
              4
            ],
            [
              0,
              2
            ],
            [
              3,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          0,
          5
        ]
      ]
    },
    {
      "name": "case_08_edge_single",
      "input": {
        "args": [
          [
            [
              1,
              2
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          2
        ]
      ]
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          [
            [
              1,
              3
            ],
            [
              2,
              6
            ],
            [
              8,
              10
            ],
            [
              15,
              18
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          6
        ],
        [
          8,
          10
        ],
        [
          15,
          18
        ]
      ]
    },
    {
      "name": "case_10_edge_touching",
      "input": {
        "args": [
          [
            [
              1,
              4
            ],
            [
              4,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          5
        ]
      ]
    },
    {
      "name": "case_11_edge_nested_overlap",
      "input": {
        "args": [
          [
            [
              1,
              4
            ],
            [
              0,
              2
            ],
            [
              3,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          0,
          5
        ]
      ]
    },
    {
      "name": "case_12_edge_single",
      "input": {
        "args": [
          [
            [
              1,
              2
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          2
        ]
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [
            [
              1,
              3
            ],
            [
              2,
              6
            ],
            [
              8,
              10
            ],
            [
              15,
              18
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          6
        ],
        [
          8,
          10
        ],
        [
          15,
          18
        ]
      ]
    },
    {
      "name": "case_14_edge_touching",
      "input": {
        "args": [
          [
            [
              1,
              4
            ],
            [
              4,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          5
        ]
      ]
    },
    {
      "name": "case_15_edge_nested_overlap",
      "input": {
        "args": [
          [
            [
              1,
              4
            ],
            [
              0,
              2
            ],
            [
              3,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          0,
          5
        ]
      ]
    },
    {
      "name": "case_16_edge_single",
      "input": {
        "args": [
          [
            [
              1,
              2
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          2
        ]
      ]
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            [
              1,
              3
            ],
            [
              2,
              6
            ],
            [
              8,
              10
            ],
            [
              15,
              18
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          6
        ],
        [
          8,
          10
        ],
        [
          15,
          18
        ]
      ]
    },
    {
      "name": "case_18_edge_touching",
      "input": {
        "args": [
          [
            [
              1,
              4
            ],
            [
              4,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          5
        ]
      ]
    },
    {
      "name": "case_19_edge_nested_overlap",
      "input": {
        "args": [
          [
            [
              1,
              4
            ],
            [
              0,
              2
            ],
            [
              3,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          0,
          5
        ]
      ]
    },
    {
      "name": "case_20_edge_single",
      "input": {
        "args": [
          [
            [
              1,
              2
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          2
        ]
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            [
              1,
              3
            ],
            [
              2,
              6
            ],
            [
              8,
              10
            ],
            [
              15,
              18
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          6
        ],
        [
          8,
          10
        ],
        [
          15,
          18
        ]
      ]
    },
    {
      "name": "case_22_edge_touching",
      "input": {
        "args": [
          [
            [
              1,
              4
            ],
            [
              4,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          5
        ]
      ]
    },
    {
      "name": "case_23_edge_nested_overlap",
      "input": {
        "args": [
          [
            [
              1,
              4
            ],
            [
              0,
              2
            ],
            [
              3,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          0,
          5
        ]
      ]
    },
    {
      "name": "case_24_edge_single",
      "input": {
        "args": [
          [
            [
              1,
              2
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          2
        ]
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            [
              1,
              3
            ],
            [
              2,
              6
            ],
            [
              8,
              10
            ],
            [
              15,
              18
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          6
        ],
        [
          8,
          10
        ],
        [
          15,
          18
        ]
      ]
    },
    {
      "name": "case_26_edge_touching",
      "input": {
        "args": [
          [
            [
              1,
              4
            ],
            [
              4,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          5
        ]
      ]
    },
    {
      "name": "case_27_edge_nested_overlap",
      "input": {
        "args": [
          [
            [
              1,
              4
            ],
            [
              0,
              2
            ],
            [
              3,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          0,
          5
        ]
      ]
    },
    {
      "name": "case_28_edge_single",
      "input": {
        "args": [
          [
            [
              1,
              2
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          2
        ]
      ]
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          [
            [
              1,
              3
            ],
            [
              2,
              6
            ],
            [
              8,
              10
            ],
            [
              15,
              18
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          6
        ],
        [
          8,
          10
        ],
        [
          15,
          18
        ]
      ]
    },
    {
      "name": "case_30_edge_touching",
      "input": {
        "args": [
          [
            [
              1,
              4
            ],
            [
              4,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          5
        ]
      ]
    },
    {
      "name": "case_31_edge_nested_overlap",
      "input": {
        "args": [
          [
            [
              1,
              4
            ],
            [
              0,
              2
            ],
            [
              3,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          0,
          5
        ]
      ]
    },
    {
      "name": "case_32_edge_single",
      "input": {
        "args": [
          [
            [
              1,
              2
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          2
        ]
      ]
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          [
            [
              1,
              3
            ],
            [
              2,
              6
            ],
            [
              8,
              10
            ],
            [
              15,
              18
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          6
        ],
        [
          8,
          10
        ],
        [
          15,
          18
        ]
      ]
    },
    {
      "name": "case_34_edge_touching",
      "input": {
        "args": [
          [
            [
              1,
              4
            ],
            [
              4,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          5
        ]
      ]
    },
    {
      "name": "case_35_edge_nested_overlap",
      "input": {
        "args": [
          [
            [
              1,
              4
            ],
            [
              0,
              2
            ],
            [
              3,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          0,
          5
        ]
      ]
    },
    {
      "name": "case_36_edge_single",
      "input": {
        "args": [
          [
            [
              1,
              2
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          2
        ]
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            [
              1,
              3
            ],
            [
              2,
              6
            ],
            [
              8,
              10
            ],
            [
              15,
              18
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          6
        ],
        [
          8,
          10
        ],
        [
          15,
          18
        ]
      ]
    },
    {
      "name": "case_38_edge_touching",
      "input": {
        "args": [
          [
            [
              1,
              4
            ],
            [
              4,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          5
        ]
      ]
    },
    {
      "name": "case_39_edge_nested_overlap",
      "input": {
        "args": [
          [
            [
              1,
              4
            ],
            [
              0,
              2
            ],
            [
              3,
              5
            ]
          ]
        ]
      },
      "expected": [
        [
          0,
          5
        ]
      ]
    },
    {
      "name": "case_40_edge_single",
      "input": {
        "args": [
          [
            [
              1,
              2
            ]
          ]
        ]
      },
      "expected": [
        [
          1,
          2
        ]
      ]
    }
  ]
}
```
