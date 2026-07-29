# 题目208 实现 Trie (前缀树)

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
请你实现 Trie 类：
`Trie()` 初始化前缀树对象。
`void insert(String word)` 向前缀树中插入字符串 `word` 。
`boolean search(String word)` 如果字符串 `word` 在前缀树中，返回 `true`（即，在检索之前已经插入）；否则，返回 `false` 。
`boolean startsWith(String prefix)` 如果之前已经插入的字符串 `word` 的前缀之一为 `prefix` ，返回 `true` ；否则，返回 `false` 。
示例：
输入["Trie", "insert", "search", "search", "startsWith", "insert", "search"][[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]输出[null, null, true, false, true, null, true]解释Trie trie = new Trie();trie.insert("apple");trie.search("apple");   // 返回 Truetrie.search("app");     // 返回 Falsetrie.startsWith("app"); // 返回 Truetrie.insert("app");trie.search("app");     // 返回 True
提示：
`1 <= word.length, prefix.length <= 2000`
`word` 和 `prefix` 仅由小写英文字母组成
`insert`、`search` 和 `startsWith` 调用次数 总计 不超过 3 * 10<sup>4</sup> 次

```json
{
  "id": 208,
  "title": "实现 Trie (前缀树)",
  "difficulty": "中等",
  "method": "question_208",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "search",
            "search",
            "startsWith",
            "insert",
            "search"
          ],
          [
            [],
            [
              "apple"
            ],
            [
              "apple"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        false,
        true,
        null,
        true
      ]
    },
    {
      "name": "case_02_edge_empty_trie",
      "input": {
        "args": [
          [
            "Trie",
            "search",
            "startsWith"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        false,
        false
      ]
    },
    {
      "name": "case_03_edge_single_word",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "startsWith",
            "search"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        true
      ]
    },
    {
      "name": "case_04_base",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "search",
            "search",
            "startsWith",
            "insert",
            "search"
          ],
          [
            [],
            [
              "apple"
            ],
            [
              "apple"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        false,
        true,
        null,
        true
      ]
    },
    {
      "name": "case_05_edge_empty_trie",
      "input": {
        "args": [
          [
            "Trie",
            "search",
            "startsWith"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        false,
        false
      ]
    },
    {
      "name": "case_06_edge_single_word",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "startsWith",
            "search"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        true
      ]
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "search",
            "search",
            "startsWith",
            "insert",
            "search"
          ],
          [
            [],
            [
              "apple"
            ],
            [
              "apple"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        false,
        true,
        null,
        true
      ]
    },
    {
      "name": "case_08_edge_empty_trie",
      "input": {
        "args": [
          [
            "Trie",
            "search",
            "startsWith"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        false,
        false
      ]
    },
    {
      "name": "case_09_edge_single_word",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "startsWith",
            "search"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        true
      ]
    },
    {
      "name": "case_10_base",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "search",
            "search",
            "startsWith",
            "insert",
            "search"
          ],
          [
            [],
            [
              "apple"
            ],
            [
              "apple"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        false,
        true,
        null,
        true
      ]
    },
    {
      "name": "case_11_edge_empty_trie",
      "input": {
        "args": [
          [
            "Trie",
            "search",
            "startsWith"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        false,
        false
      ]
    },
    {
      "name": "case_12_edge_single_word",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "startsWith",
            "search"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        true
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "search",
            "search",
            "startsWith",
            "insert",
            "search"
          ],
          [
            [],
            [
              "apple"
            ],
            [
              "apple"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        false,
        true,
        null,
        true
      ]
    },
    {
      "name": "case_14_edge_empty_trie",
      "input": {
        "args": [
          [
            "Trie",
            "search",
            "startsWith"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        false,
        false
      ]
    },
    {
      "name": "case_15_edge_single_word",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "startsWith",
            "search"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        true
      ]
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "search",
            "search",
            "startsWith",
            "insert",
            "search"
          ],
          [
            [],
            [
              "apple"
            ],
            [
              "apple"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        false,
        true,
        null,
        true
      ]
    },
    {
      "name": "case_17_edge_empty_trie",
      "input": {
        "args": [
          [
            "Trie",
            "search",
            "startsWith"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        false,
        false
      ]
    },
    {
      "name": "case_18_edge_single_word",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "startsWith",
            "search"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        true
      ]
    },
    {
      "name": "case_19_base",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "search",
            "search",
            "startsWith",
            "insert",
            "search"
          ],
          [
            [],
            [
              "apple"
            ],
            [
              "apple"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        false,
        true,
        null,
        true
      ]
    },
    {
      "name": "case_20_edge_empty_trie",
      "input": {
        "args": [
          [
            "Trie",
            "search",
            "startsWith"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        false,
        false
      ]
    },
    {
      "name": "case_21_edge_single_word",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "startsWith",
            "search"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        true
      ]
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "search",
            "search",
            "startsWith",
            "insert",
            "search"
          ],
          [
            [],
            [
              "apple"
            ],
            [
              "apple"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        false,
        true,
        null,
        true
      ]
    },
    {
      "name": "case_23_edge_empty_trie",
      "input": {
        "args": [
          [
            "Trie",
            "search",
            "startsWith"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        false,
        false
      ]
    },
    {
      "name": "case_24_edge_single_word",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "startsWith",
            "search"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        true
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "search",
            "search",
            "startsWith",
            "insert",
            "search"
          ],
          [
            [],
            [
              "apple"
            ],
            [
              "apple"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        false,
        true,
        null,
        true
      ]
    },
    {
      "name": "case_26_edge_empty_trie",
      "input": {
        "args": [
          [
            "Trie",
            "search",
            "startsWith"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        false,
        false
      ]
    },
    {
      "name": "case_27_edge_single_word",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "startsWith",
            "search"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        true
      ]
    },
    {
      "name": "case_28_base",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "search",
            "search",
            "startsWith",
            "insert",
            "search"
          ],
          [
            [],
            [
              "apple"
            ],
            [
              "apple"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        false,
        true,
        null,
        true
      ]
    },
    {
      "name": "case_29_edge_empty_trie",
      "input": {
        "args": [
          [
            "Trie",
            "search",
            "startsWith"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        false,
        false
      ]
    },
    {
      "name": "case_30_edge_single_word",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "startsWith",
            "search"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        true
      ]
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "search",
            "search",
            "startsWith",
            "insert",
            "search"
          ],
          [
            [],
            [
              "apple"
            ],
            [
              "apple"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        false,
        true,
        null,
        true
      ]
    },
    {
      "name": "case_32_edge_empty_trie",
      "input": {
        "args": [
          [
            "Trie",
            "search",
            "startsWith"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        false,
        false
      ]
    },
    {
      "name": "case_33_edge_single_word",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "startsWith",
            "search"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        true
      ]
    },
    {
      "name": "case_34_base",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "search",
            "search",
            "startsWith",
            "insert",
            "search"
          ],
          [
            [],
            [
              "apple"
            ],
            [
              "apple"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        false,
        true,
        null,
        true
      ]
    },
    {
      "name": "case_35_edge_empty_trie",
      "input": {
        "args": [
          [
            "Trie",
            "search",
            "startsWith"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        false,
        false
      ]
    },
    {
      "name": "case_36_edge_single_word",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "startsWith",
            "search"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        true
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "search",
            "search",
            "startsWith",
            "insert",
            "search"
          ],
          [
            [],
            [
              "apple"
            ],
            [
              "apple"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        false,
        true,
        null,
        true
      ]
    },
    {
      "name": "case_38_edge_empty_trie",
      "input": {
        "args": [
          [
            "Trie",
            "search",
            "startsWith"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        false,
        false
      ]
    },
    {
      "name": "case_39_edge_single_word",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "startsWith",
            "search"
          ],
          [
            [],
            [
              "a"
            ],
            [
              "a"
            ],
            [
              "a"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        true
      ]
    },
    {
      "name": "case_40_base",
      "input": {
        "args": [
          [
            "Trie",
            "insert",
            "search",
            "search",
            "startsWith",
            "insert",
            "search"
          ],
          [
            [],
            [
              "apple"
            ],
            [
              "apple"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ],
            [
              "app"
            ]
          ]
        ]
      },
      "expected": [
        null,
        null,
        true,
        false,
        true,
        null,
        true
      ]
    }
  ]
}
```
