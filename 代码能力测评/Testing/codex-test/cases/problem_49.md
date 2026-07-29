# 题目49 字母异位词分组

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。
示例 1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
示例 2:
输入: strs = [""]输出: [[""]]
示例 3:
输入: strs = ["a"]输出: [["a"]]
提示：
1 <= strs.length <= 10<sup>4</sup>
`0 <= strs[i].length <= 100`
`strs[i]` 仅包含小写字母

```json
{
  "id": 49,
  "title": "字母异位词分组",
  "difficulty": "中等",
  "method": "question_49",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            "eat",
            "tea",
            "tan",
            "ate",
            "nat",
            "bat"
          ]
        ]
      },
      "expected": [
        [
          "bat"
        ],
        [
          "nat",
          "tan"
        ],
        [
          "ate",
          "eat",
          "tea"
        ]
      ],
      "comparison": "group_anagrams"
    },
    {
      "name": "case_02_edge_empty_string",
      "input": {
        "args": [
          [
            ""
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          ""
        ]
      ]
    },
    {
      "name": "case_03_edge_single",
      "input": {
        "args": [
          [
            "a"
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          "a"
        ]
      ]
    },
    {
      "name": "case_04_edge_one_group_plus_single",
      "input": {
        "args": [
          [
            "eat",
            "tea",
            "ate",
            "bat"
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          "eat",
          "tea",
          "ate"
        ],
        [
          "bat"
        ]
      ]
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          [
            "eat",
            "tea",
            "tan",
            "ate",
            "nat",
            "bat"
          ]
        ]
      },
      "expected": [
        [
          "bat"
        ],
        [
          "nat",
          "tan"
        ],
        [
          "ate",
          "eat",
          "tea"
        ]
      ],
      "comparison": "group_anagrams"
    },
    {
      "name": "case_06_edge_empty_string",
      "input": {
        "args": [
          [
            ""
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          ""
        ]
      ]
    },
    {
      "name": "case_07_edge_single",
      "input": {
        "args": [
          [
            "a"
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          "a"
        ]
      ]
    },
    {
      "name": "case_08_edge_one_group_plus_single",
      "input": {
        "args": [
          [
            "eat",
            "tea",
            "ate",
            "bat"
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          "eat",
          "tea",
          "ate"
        ],
        [
          "bat"
        ]
      ]
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          [
            "eat",
            "tea",
            "tan",
            "ate",
            "nat",
            "bat"
          ]
        ]
      },
      "expected": [
        [
          "bat"
        ],
        [
          "nat",
          "tan"
        ],
        [
          "ate",
          "eat",
          "tea"
        ]
      ],
      "comparison": "group_anagrams"
    },
    {
      "name": "case_10_edge_empty_string",
      "input": {
        "args": [
          [
            ""
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          ""
        ]
      ]
    },
    {
      "name": "case_11_edge_single",
      "input": {
        "args": [
          [
            "a"
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          "a"
        ]
      ]
    },
    {
      "name": "case_12_edge_one_group_plus_single",
      "input": {
        "args": [
          [
            "eat",
            "tea",
            "ate",
            "bat"
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          "eat",
          "tea",
          "ate"
        ],
        [
          "bat"
        ]
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [
            "eat",
            "tea",
            "tan",
            "ate",
            "nat",
            "bat"
          ]
        ]
      },
      "expected": [
        [
          "bat"
        ],
        [
          "nat",
          "tan"
        ],
        [
          "ate",
          "eat",
          "tea"
        ]
      ],
      "comparison": "group_anagrams"
    },
    {
      "name": "case_14_edge_empty_string",
      "input": {
        "args": [
          [
            ""
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          ""
        ]
      ]
    },
    {
      "name": "case_15_edge_single",
      "input": {
        "args": [
          [
            "a"
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          "a"
        ]
      ]
    },
    {
      "name": "case_16_edge_one_group_plus_single",
      "input": {
        "args": [
          [
            "eat",
            "tea",
            "ate",
            "bat"
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          "eat",
          "tea",
          "ate"
        ],
        [
          "bat"
        ]
      ]
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            "eat",
            "tea",
            "tan",
            "ate",
            "nat",
            "bat"
          ]
        ]
      },
      "expected": [
        [
          "bat"
        ],
        [
          "nat",
          "tan"
        ],
        [
          "ate",
          "eat",
          "tea"
        ]
      ],
      "comparison": "group_anagrams"
    },
    {
      "name": "case_18_edge_empty_string",
      "input": {
        "args": [
          [
            ""
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          ""
        ]
      ]
    },
    {
      "name": "case_19_edge_single",
      "input": {
        "args": [
          [
            "a"
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          "a"
        ]
      ]
    },
    {
      "name": "case_20_edge_one_group_plus_single",
      "input": {
        "args": [
          [
            "eat",
            "tea",
            "ate",
            "bat"
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          "eat",
          "tea",
          "ate"
        ],
        [
          "bat"
        ]
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            "eat",
            "tea",
            "tan",
            "ate",
            "nat",
            "bat"
          ]
        ]
      },
      "expected": [
        [
          "bat"
        ],
        [
          "nat",
          "tan"
        ],
        [
          "ate",
          "eat",
          "tea"
        ]
      ],
      "comparison": "group_anagrams"
    },
    {
      "name": "case_22_edge_empty_string",
      "input": {
        "args": [
          [
            ""
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          ""
        ]
      ]
    },
    {
      "name": "case_23_edge_single",
      "input": {
        "args": [
          [
            "a"
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          "a"
        ]
      ]
    },
    {
      "name": "case_24_edge_one_group_plus_single",
      "input": {
        "args": [
          [
            "eat",
            "tea",
            "ate",
            "bat"
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          "eat",
          "tea",
          "ate"
        ],
        [
          "bat"
        ]
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            "eat",
            "tea",
            "tan",
            "ate",
            "nat",
            "bat"
          ]
        ]
      },
      "expected": [
        [
          "bat"
        ],
        [
          "nat",
          "tan"
        ],
        [
          "ate",
          "eat",
          "tea"
        ]
      ],
      "comparison": "group_anagrams"
    },
    {
      "name": "case_26_edge_empty_string",
      "input": {
        "args": [
          [
            ""
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          ""
        ]
      ]
    },
    {
      "name": "case_27_edge_single",
      "input": {
        "args": [
          [
            "a"
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          "a"
        ]
      ]
    },
    {
      "name": "case_28_edge_one_group_plus_single",
      "input": {
        "args": [
          [
            "eat",
            "tea",
            "ate",
            "bat"
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          "eat",
          "tea",
          "ate"
        ],
        [
          "bat"
        ]
      ]
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          [
            "eat",
            "tea",
            "tan",
            "ate",
            "nat",
            "bat"
          ]
        ]
      },
      "expected": [
        [
          "bat"
        ],
        [
          "nat",
          "tan"
        ],
        [
          "ate",
          "eat",
          "tea"
        ]
      ],
      "comparison": "group_anagrams"
    },
    {
      "name": "case_30_edge_empty_string",
      "input": {
        "args": [
          [
            ""
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          ""
        ]
      ]
    },
    {
      "name": "case_31_edge_single",
      "input": {
        "args": [
          [
            "a"
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          "a"
        ]
      ]
    },
    {
      "name": "case_32_edge_one_group_plus_single",
      "input": {
        "args": [
          [
            "eat",
            "tea",
            "ate",
            "bat"
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          "eat",
          "tea",
          "ate"
        ],
        [
          "bat"
        ]
      ]
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          [
            "eat",
            "tea",
            "tan",
            "ate",
            "nat",
            "bat"
          ]
        ]
      },
      "expected": [
        [
          "bat"
        ],
        [
          "nat",
          "tan"
        ],
        [
          "ate",
          "eat",
          "tea"
        ]
      ],
      "comparison": "group_anagrams"
    },
    {
      "name": "case_34_edge_empty_string",
      "input": {
        "args": [
          [
            ""
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          ""
        ]
      ]
    },
    {
      "name": "case_35_edge_single",
      "input": {
        "args": [
          [
            "a"
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          "a"
        ]
      ]
    },
    {
      "name": "case_36_edge_one_group_plus_single",
      "input": {
        "args": [
          [
            "eat",
            "tea",
            "ate",
            "bat"
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          "eat",
          "tea",
          "ate"
        ],
        [
          "bat"
        ]
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            "eat",
            "tea",
            "tan",
            "ate",
            "nat",
            "bat"
          ]
        ]
      },
      "expected": [
        [
          "bat"
        ],
        [
          "nat",
          "tan"
        ],
        [
          "ate",
          "eat",
          "tea"
        ]
      ],
      "comparison": "group_anagrams"
    },
    {
      "name": "case_38_edge_empty_string",
      "input": {
        "args": [
          [
            ""
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          ""
        ]
      ]
    },
    {
      "name": "case_39_edge_single",
      "input": {
        "args": [
          [
            "a"
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          "a"
        ]
      ]
    },
    {
      "name": "case_40_edge_one_group_plus_single",
      "input": {
        "args": [
          [
            "eat",
            "tea",
            "ate",
            "bat"
          ]
        ]
      },
      "comparison": "group_anagrams",
      "expected": [
        [
          "eat",
          "tea",
          "ate"
        ],
        [
          "bat"
        ]
      ]
    }
  ]
}
```
