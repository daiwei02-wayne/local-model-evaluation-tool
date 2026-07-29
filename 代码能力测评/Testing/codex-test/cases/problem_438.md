# 题目438 找到字符串中所有字母异位词

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定两个字符串 `s` 和 `p`，找到 `s`中所有 `p`的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
示例 1:
输入: s = "cbaebabacd", p = "abc"输出: [0,6]解释:起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
示例 2:
输入: s = "abab", p = "ab"输出: [0,1,2]解释:起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
提示:
1 <= s.length, p.length <= 3 * 10<sup>4</sup>
`s` 和 `p` 仅包含小写字母

```json
{
  "id": 438,
  "title": "找到字符串中所有字母异位词",
  "difficulty": "中等",
  "method": "question_438",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          "cbaebabacd",
          "abc"
        ]
      },
      "expected": [
        0,
        6
      ]
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          "abab",
          "ab"
        ]
      },
      "expected": [
        0,
        1,
        2
      ]
    },
    {
      "name": "case_03_edge_empty_s",
      "input": {
        "args": [
          "",
          "a"
        ]
      },
      "expected": []
    },
    {
      "name": "case_04_edge_single_hit",
      "input": {
        "args": [
          "a",
          "a"
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_05_edge_repeated",
      "input": {
        "args": [
          "aaaaaaaaaa",
          "aa"
        ]
      },
      "expected": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8
      ]
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          "cbaebabacd",
          "abc"
        ]
      },
      "expected": [
        0,
        6
      ]
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          "abab",
          "ab"
        ]
      },
      "expected": [
        0,
        1,
        2
      ]
    },
    {
      "name": "case_08_edge_empty_s",
      "input": {
        "args": [
          "",
          "a"
        ]
      },
      "expected": []
    },
    {
      "name": "case_09_edge_single_hit",
      "input": {
        "args": [
          "a",
          "a"
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_10_edge_repeated",
      "input": {
        "args": [
          "aaaaaaaaaa",
          "aa"
        ]
      },
      "expected": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8
      ]
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          "cbaebabacd",
          "abc"
        ]
      },
      "expected": [
        0,
        6
      ]
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          "abab",
          "ab"
        ]
      },
      "expected": [
        0,
        1,
        2
      ]
    },
    {
      "name": "case_13_edge_empty_s",
      "input": {
        "args": [
          "",
          "a"
        ]
      },
      "expected": []
    },
    {
      "name": "case_14_edge_single_hit",
      "input": {
        "args": [
          "a",
          "a"
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_15_edge_repeated",
      "input": {
        "args": [
          "aaaaaaaaaa",
          "aa"
        ]
      },
      "expected": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8
      ]
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          "cbaebabacd",
          "abc"
        ]
      },
      "expected": [
        0,
        6
      ]
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          "abab",
          "ab"
        ]
      },
      "expected": [
        0,
        1,
        2
      ]
    },
    {
      "name": "case_18_edge_empty_s",
      "input": {
        "args": [
          "",
          "a"
        ]
      },
      "expected": []
    },
    {
      "name": "case_19_edge_single_hit",
      "input": {
        "args": [
          "a",
          "a"
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_20_edge_repeated",
      "input": {
        "args": [
          "aaaaaaaaaa",
          "aa"
        ]
      },
      "expected": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          "cbaebabacd",
          "abc"
        ]
      },
      "expected": [
        0,
        6
      ]
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          "abab",
          "ab"
        ]
      },
      "expected": [
        0,
        1,
        2
      ]
    },
    {
      "name": "case_23_edge_empty_s",
      "input": {
        "args": [
          "",
          "a"
        ]
      },
      "expected": []
    },
    {
      "name": "case_24_edge_single_hit",
      "input": {
        "args": [
          "a",
          "a"
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_25_edge_repeated",
      "input": {
        "args": [
          "aaaaaaaaaa",
          "aa"
        ]
      },
      "expected": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8
      ]
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          "cbaebabacd",
          "abc"
        ]
      },
      "expected": [
        0,
        6
      ]
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          "abab",
          "ab"
        ]
      },
      "expected": [
        0,
        1,
        2
      ]
    },
    {
      "name": "case_28_edge_empty_s",
      "input": {
        "args": [
          "",
          "a"
        ]
      },
      "expected": []
    },
    {
      "name": "case_29_edge_single_hit",
      "input": {
        "args": [
          "a",
          "a"
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_30_edge_repeated",
      "input": {
        "args": [
          "aaaaaaaaaa",
          "aa"
        ]
      },
      "expected": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8
      ]
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          "cbaebabacd",
          "abc"
        ]
      },
      "expected": [
        0,
        6
      ]
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          "abab",
          "ab"
        ]
      },
      "expected": [
        0,
        1,
        2
      ]
    },
    {
      "name": "case_33_edge_empty_s",
      "input": {
        "args": [
          "",
          "a"
        ]
      },
      "expected": []
    },
    {
      "name": "case_34_edge_single_hit",
      "input": {
        "args": [
          "a",
          "a"
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_35_edge_repeated",
      "input": {
        "args": [
          "aaaaaaaaaa",
          "aa"
        ]
      },
      "expected": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8
      ]
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          "cbaebabacd",
          "abc"
        ]
      },
      "expected": [
        0,
        6
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          "abab",
          "ab"
        ]
      },
      "expected": [
        0,
        1,
        2
      ]
    },
    {
      "name": "case_38_edge_empty_s",
      "input": {
        "args": [
          "",
          "a"
        ]
      },
      "expected": []
    },
    {
      "name": "case_39_edge_single_hit",
      "input": {
        "args": [
          "a",
          "a"
        ]
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_40_edge_repeated",
      "input": {
        "args": [
          "aaaaaaaaaa",
          "aa"
        ]
      },
      "expected": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8
      ]
    }
  ]
}
```
