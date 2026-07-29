# 题目79 单词搜索

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一个 `m x n` 二维字符网格 `board` 和一个字符串单词 `word` 。如果 `word` 存在于网格中，返回 `true` ；否则，返回 `false` 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
示例 1：
题目配图：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"输出：true
示例 2：
题目配图：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"输出：true
示例 3：
题目配图：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"输出：false
提示：
`m == board.length`
`n = board[i].length`
`1 <= m, n <= 6`
`1 <= word.length <= 15`
`board` 和 `word` 仅由大小写英文字母组成
进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 `board` 更大的情况下可以更快解决问题？

```json
{
  "id": 79,
  "title": "单词搜索",
  "difficulty": "中等",
  "method": "question_79",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            [
              "A",
              "B",
              "C",
              "E"
            ],
            [
              "S",
              "F",
              "C",
              "S"
            ],
            [
              "A",
              "D",
              "E",
              "E"
            ]
          ],
          "ABCCED"
        ]
      },
      "expected": true
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            [
              "A",
              "B"
            ],
            [
              "C",
              "D"
            ]
          ],
          "ACDB"
        ]
      },
      "expected": true
    },
    {
      "name": "case_03_edge_single_hit",
      "input": {
        "args": [
          [
            [
              "A"
            ]
          ],
          "A"
        ]
      },
      "expected": true
    },
    {
      "name": "case_04_edge_single_miss",
      "input": {
        "args": [
          [
            [
              "A"
            ]
          ],
          "B"
        ]
      },
      "expected": false
    },
    {
      "name": "case_05_edge_cannot_reuse",
      "input": {
        "args": [
          [
            [
              "A",
              "A"
            ]
          ],
          "AAA"
        ]
      },
      "expected": false
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            [
              "A",
              "B",
              "C",
              "E"
            ],
            [
              "S",
              "F",
              "C",
              "S"
            ],
            [
              "A",
              "D",
              "E",
              "E"
            ]
          ],
          "ABCCED"
        ]
      },
      "expected": true
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            [
              "A",
              "B"
            ],
            [
              "C",
              "D"
            ]
          ],
          "ACDB"
        ]
      },
      "expected": true
    },
    {
      "name": "case_08_edge_single_hit",
      "input": {
        "args": [
          [
            [
              "A"
            ]
          ],
          "A"
        ]
      },
      "expected": true
    },
    {
      "name": "case_09_edge_single_miss",
      "input": {
        "args": [
          [
            [
              "A"
            ]
          ],
          "B"
        ]
      },
      "expected": false
    },
    {
      "name": "case_10_edge_cannot_reuse",
      "input": {
        "args": [
          [
            [
              "A",
              "A"
            ]
          ],
          "AAA"
        ]
      },
      "expected": false
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            [
              "A",
              "B",
              "C",
              "E"
            ],
            [
              "S",
              "F",
              "C",
              "S"
            ],
            [
              "A",
              "D",
              "E",
              "E"
            ]
          ],
          "ABCCED"
        ]
      },
      "expected": true
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          [
            [
              "A",
              "B"
            ],
            [
              "C",
              "D"
            ]
          ],
          "ACDB"
        ]
      },
      "expected": true
    },
    {
      "name": "case_13_edge_single_hit",
      "input": {
        "args": [
          [
            [
              "A"
            ]
          ],
          "A"
        ]
      },
      "expected": true
    },
    {
      "name": "case_14_edge_single_miss",
      "input": {
        "args": [
          [
            [
              "A"
            ]
          ],
          "B"
        ]
      },
      "expected": false
    },
    {
      "name": "case_15_edge_cannot_reuse",
      "input": {
        "args": [
          [
            [
              "A",
              "A"
            ]
          ],
          "AAA"
        ]
      },
      "expected": false
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            [
              "A",
              "B",
              "C",
              "E"
            ],
            [
              "S",
              "F",
              "C",
              "S"
            ],
            [
              "A",
              "D",
              "E",
              "E"
            ]
          ],
          "ABCCED"
        ]
      },
      "expected": true
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            [
              "A",
              "B"
            ],
            [
              "C",
              "D"
            ]
          ],
          "ACDB"
        ]
      },
      "expected": true
    },
    {
      "name": "case_18_edge_single_hit",
      "input": {
        "args": [
          [
            [
              "A"
            ]
          ],
          "A"
        ]
      },
      "expected": true
    },
    {
      "name": "case_19_edge_single_miss",
      "input": {
        "args": [
          [
            [
              "A"
            ]
          ],
          "B"
        ]
      },
      "expected": false
    },
    {
      "name": "case_20_edge_cannot_reuse",
      "input": {
        "args": [
          [
            [
              "A",
              "A"
            ]
          ],
          "AAA"
        ]
      },
      "expected": false
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            [
              "A",
              "B",
              "C",
              "E"
            ],
            [
              "S",
              "F",
              "C",
              "S"
            ],
            [
              "A",
              "D",
              "E",
              "E"
            ]
          ],
          "ABCCED"
        ]
      },
      "expected": true
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            [
              "A",
              "B"
            ],
            [
              "C",
              "D"
            ]
          ],
          "ACDB"
        ]
      },
      "expected": true
    },
    {
      "name": "case_23_edge_single_hit",
      "input": {
        "args": [
          [
            [
              "A"
            ]
          ],
          "A"
        ]
      },
      "expected": true
    },
    {
      "name": "case_24_edge_single_miss",
      "input": {
        "args": [
          [
            [
              "A"
            ]
          ],
          "B"
        ]
      },
      "expected": false
    },
    {
      "name": "case_25_edge_cannot_reuse",
      "input": {
        "args": [
          [
            [
              "A",
              "A"
            ]
          ],
          "AAA"
        ]
      },
      "expected": false
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            [
              "A",
              "B",
              "C",
              "E"
            ],
            [
              "S",
              "F",
              "C",
              "S"
            ],
            [
              "A",
              "D",
              "E",
              "E"
            ]
          ],
          "ABCCED"
        ]
      },
      "expected": true
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          [
            [
              "A",
              "B"
            ],
            [
              "C",
              "D"
            ]
          ],
          "ACDB"
        ]
      },
      "expected": true
    },
    {
      "name": "case_28_edge_single_hit",
      "input": {
        "args": [
          [
            [
              "A"
            ]
          ],
          "A"
        ]
      },
      "expected": true
    },
    {
      "name": "case_29_edge_single_miss",
      "input": {
        "args": [
          [
            [
              "A"
            ]
          ],
          "B"
        ]
      },
      "expected": false
    },
    {
      "name": "case_30_edge_cannot_reuse",
      "input": {
        "args": [
          [
            [
              "A",
              "A"
            ]
          ],
          "AAA"
        ]
      },
      "expected": false
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            [
              "A",
              "B",
              "C",
              "E"
            ],
            [
              "S",
              "F",
              "C",
              "S"
            ],
            [
              "A",
              "D",
              "E",
              "E"
            ]
          ],
          "ABCCED"
        ]
      },
      "expected": true
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          [
            [
              "A",
              "B"
            ],
            [
              "C",
              "D"
            ]
          ],
          "ACDB"
        ]
      },
      "expected": true
    },
    {
      "name": "case_33_edge_single_hit",
      "input": {
        "args": [
          [
            [
              "A"
            ]
          ],
          "A"
        ]
      },
      "expected": true
    },
    {
      "name": "case_34_edge_single_miss",
      "input": {
        "args": [
          [
            [
              "A"
            ]
          ],
          "B"
        ]
      },
      "expected": false
    },
    {
      "name": "case_35_edge_cannot_reuse",
      "input": {
        "args": [
          [
            [
              "A",
              "A"
            ]
          ],
          "AAA"
        ]
      },
      "expected": false
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          [
            [
              "A",
              "B",
              "C",
              "E"
            ],
            [
              "S",
              "F",
              "C",
              "S"
            ],
            [
              "A",
              "D",
              "E",
              "E"
            ]
          ],
          "ABCCED"
        ]
      },
      "expected": true
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            [
              "A",
              "B"
            ],
            [
              "C",
              "D"
            ]
          ],
          "ACDB"
        ]
      },
      "expected": true
    },
    {
      "name": "case_38_edge_single_hit",
      "input": {
        "args": [
          [
            [
              "A"
            ]
          ],
          "A"
        ]
      },
      "expected": true
    },
    {
      "name": "case_39_edge_single_miss",
      "input": {
        "args": [
          [
            [
              "A"
            ]
          ],
          "B"
        ]
      },
      "expected": false
    },
    {
      "name": "case_40_edge_cannot_reuse",
      "input": {
        "args": [
          [
            [
              "A",
              "A"
            ]
          ],
          "AAA"
        ]
      },
      "expected": false
    }
  ]
}
```
