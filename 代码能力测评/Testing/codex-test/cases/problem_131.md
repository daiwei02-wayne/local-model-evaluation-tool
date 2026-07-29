# 题目131 分割回文串

来源：LeetCode 热题 100（https://leetcode.cn/studyplan/top-100-liked/）

```json
{
  "id": 131,
  "title": "分割回文串",
  "difficulty": "中等",
  "method": "question_131",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          "aab"
        ]
      },
      "expected": [
        [
          "a",
          "a",
          "b"
        ],
        [
          "aa",
          "b"
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          "a"
        ]
      },
      "expected": [
        [
          "a"
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_03_base",
      "input": {
        "args": [
          "efe"
        ]
      },
      "expected": [
        [
          "e",
          "f",
          "e"
        ],
        [
          "efe"
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_04_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        []
      ]
    },
    {
      "name": "case_05_edge_all_same",
      "input": {
        "args": [
          "aaa"
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          "a",
          "a",
          "a"
        ],
        [
          "a",
          "aa"
        ],
        [
          "aa",
          "a"
        ],
        [
          "aaa"
        ]
      ]
    },
    {
      "name": "case_06_edge_no_multi",
      "input": {
        "args": [
          "abc"
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          "a",
          "b",
          "c"
        ]
      ]
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          "aab"
        ]
      },
      "expected": [
        [
          "a",
          "a",
          "b"
        ],
        [
          "aa",
          "b"
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_08_base",
      "input": {
        "args": [
          "a"
        ]
      },
      "expected": [
        [
          "a"
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          "efe"
        ]
      },
      "expected": [
        [
          "e",
          "f",
          "e"
        ],
        [
          "efe"
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_10_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        []
      ]
    },
    {
      "name": "case_11_edge_all_same",
      "input": {
        "args": [
          "aaa"
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          "a",
          "a",
          "a"
        ],
        [
          "a",
          "aa"
        ],
        [
          "aa",
          "a"
        ],
        [
          "aaa"
        ]
      ]
    },
    {
      "name": "case_12_edge_no_multi",
      "input": {
        "args": [
          "abc"
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          "a",
          "b",
          "c"
        ]
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          "aab"
        ]
      },
      "expected": [
        [
          "a",
          "a",
          "b"
        ],
        [
          "aa",
          "b"
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_14_base",
      "input": {
        "args": [
          "a"
        ]
      },
      "expected": [
        [
          "a"
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_15_base",
      "input": {
        "args": [
          "efe"
        ]
      },
      "expected": [
        [
          "e",
          "f",
          "e"
        ],
        [
          "efe"
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_16_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        []
      ]
    },
    {
      "name": "case_17_edge_all_same",
      "input": {
        "args": [
          "aaa"
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          "a",
          "a",
          "a"
        ],
        [
          "a",
          "aa"
        ],
        [
          "aa",
          "a"
        ],
        [
          "aaa"
        ]
      ]
    },
    {
      "name": "case_18_edge_no_multi",
      "input": {
        "args": [
          "abc"
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          "a",
          "b",
          "c"
        ]
      ]
    },
    {
      "name": "case_19_base",
      "input": {
        "args": [
          "aab"
        ]
      },
      "expected": [
        [
          "a",
          "a",
          "b"
        ],
        [
          "aa",
          "b"
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_20_base",
      "input": {
        "args": [
          "a"
        ]
      },
      "expected": [
        [
          "a"
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          "efe"
        ]
      },
      "expected": [
        [
          "e",
          "f",
          "e"
        ],
        [
          "efe"
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_22_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        []
      ]
    },
    {
      "name": "case_23_edge_all_same",
      "input": {
        "args": [
          "aaa"
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          "a",
          "a",
          "a"
        ],
        [
          "a",
          "aa"
        ],
        [
          "aa",
          "a"
        ],
        [
          "aaa"
        ]
      ]
    },
    {
      "name": "case_24_edge_no_multi",
      "input": {
        "args": [
          "abc"
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          "a",
          "b",
          "c"
        ]
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          "aab"
        ]
      },
      "expected": [
        [
          "a",
          "a",
          "b"
        ],
        [
          "aa",
          "b"
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          "a"
        ]
      },
      "expected": [
        [
          "a"
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          "efe"
        ]
      },
      "expected": [
        [
          "e",
          "f",
          "e"
        ],
        [
          "efe"
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_28_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        []
      ]
    },
    {
      "name": "case_29_edge_all_same",
      "input": {
        "args": [
          "aaa"
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          "a",
          "a",
          "a"
        ],
        [
          "a",
          "aa"
        ],
        [
          "aa",
          "a"
        ],
        [
          "aaa"
        ]
      ]
    },
    {
      "name": "case_30_edge_no_multi",
      "input": {
        "args": [
          "abc"
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          "a",
          "b",
          "c"
        ]
      ]
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          "aab"
        ]
      },
      "expected": [
        [
          "a",
          "a",
          "b"
        ],
        [
          "aa",
          "b"
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          "a"
        ]
      },
      "expected": [
        [
          "a"
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          "efe"
        ]
      },
      "expected": [
        [
          "e",
          "f",
          "e"
        ],
        [
          "efe"
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_34_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        []
      ]
    },
    {
      "name": "case_35_edge_all_same",
      "input": {
        "args": [
          "aaa"
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          "a",
          "a",
          "a"
        ],
        [
          "a",
          "aa"
        ],
        [
          "aa",
          "a"
        ],
        [
          "aaa"
        ]
      ]
    },
    {
      "name": "case_36_edge_no_multi",
      "input": {
        "args": [
          "abc"
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        [
          "a",
          "b",
          "c"
        ]
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          "aab"
        ]
      },
      "expected": [
        [
          "a",
          "a",
          "b"
        ],
        [
          "aa",
          "b"
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          "a"
        ]
      },
      "expected": [
        [
          "a"
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_39_base",
      "input": {
        "args": [
          "efe"
        ]
      },
      "expected": [
        [
          "e",
          "f",
          "e"
        ],
        [
          "efe"
        ]
      ],
      "comparison": "set_of_lists"
    },
    {
      "name": "case_40_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "comparison": "set_of_lists",
      "expected": [
        []
      ]
    }
  ]
}
```
