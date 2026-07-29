# 题目5 最长回文子串

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个字符串 `s`，找到 `s` 中最长的回文子串。
示例 1：
输入：s = "babad"输出："bab"解释："aba" 同样是符合题意的答案。
示例 2：
输入：s = "cbbd"输出："bb"
提示：
`1 <= s.length <= 1000`
`s` 仅由数字和英文字母组成

```json
{
  "id": 5,
  "title": "最长回文子串",
  "difficulty": "中等",
  "method": "question_5",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          "cbbd"
        ]
      },
      "expected": "bb"
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          "a"
        ]
      },
      "expected": "a"
    },
    {
      "name": "case_03_base",
      "input": {
        "args": [
          "bb"
        ]
      },
      "expected": "bb"
    },
    {
      "name": "case_04_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": ""
    },
    {
      "name": "case_05_edge_all_same",
      "input": {
        "args": [
          "aaaa"
        ]
      },
      "expected": "aaaa"
    },
    {
      "name": "case_06_edge_odd_choice",
      "input": {
        "args": [
          "babad"
        ]
      },
      "expected": "bab"
    },
    {
      "name": "case_07_edge_no_long",
      "input": {
        "args": [
          "abcda"
        ]
      },
      "expected": "a"
    },
    {
      "name": "case_08_base",
      "input": {
        "args": [
          "cbbd"
        ]
      },
      "expected": "bb"
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          "a"
        ]
      },
      "expected": "a"
    },
    {
      "name": "case_10_base",
      "input": {
        "args": [
          "bb"
        ]
      },
      "expected": "bb"
    },
    {
      "name": "case_11_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": ""
    },
    {
      "name": "case_12_edge_all_same",
      "input": {
        "args": [
          "aaaa"
        ]
      },
      "expected": "aaaa"
    },
    {
      "name": "case_13_edge_odd_choice",
      "input": {
        "args": [
          "babad"
        ]
      },
      "expected": "bab"
    },
    {
      "name": "case_14_edge_no_long",
      "input": {
        "args": [
          "abcda"
        ]
      },
      "expected": "a"
    },
    {
      "name": "case_15_base",
      "input": {
        "args": [
          "cbbd"
        ]
      },
      "expected": "bb"
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          "a"
        ]
      },
      "expected": "a"
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          "bb"
        ]
      },
      "expected": "bb"
    },
    {
      "name": "case_18_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": ""
    },
    {
      "name": "case_19_edge_all_same",
      "input": {
        "args": [
          "aaaa"
        ]
      },
      "expected": "aaaa"
    },
    {
      "name": "case_20_edge_odd_choice",
      "input": {
        "args": [
          "babad"
        ]
      },
      "expected": "bab"
    },
    {
      "name": "case_21_edge_no_long",
      "input": {
        "args": [
          "abcda"
        ]
      },
      "expected": "a"
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          "cbbd"
        ]
      },
      "expected": "bb"
    },
    {
      "name": "case_23_base",
      "input": {
        "args": [
          "a"
        ]
      },
      "expected": "a"
    },
    {
      "name": "case_24_base",
      "input": {
        "args": [
          "bb"
        ]
      },
      "expected": "bb"
    },
    {
      "name": "case_25_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": ""
    },
    {
      "name": "case_26_edge_all_same",
      "input": {
        "args": [
          "aaaa"
        ]
      },
      "expected": "aaaa"
    },
    {
      "name": "case_27_edge_odd_choice",
      "input": {
        "args": [
          "babad"
        ]
      },
      "expected": "bab"
    },
    {
      "name": "case_28_edge_no_long",
      "input": {
        "args": [
          "abcda"
        ]
      },
      "expected": "a"
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          "cbbd"
        ]
      },
      "expected": "bb"
    },
    {
      "name": "case_30_base",
      "input": {
        "args": [
          "a"
        ]
      },
      "expected": "a"
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          "bb"
        ]
      },
      "expected": "bb"
    },
    {
      "name": "case_32_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": ""
    },
    {
      "name": "case_33_edge_all_same",
      "input": {
        "args": [
          "aaaa"
        ]
      },
      "expected": "aaaa"
    },
    {
      "name": "case_34_edge_odd_choice",
      "input": {
        "args": [
          "babad"
        ]
      },
      "expected": "bab"
    },
    {
      "name": "case_35_edge_no_long",
      "input": {
        "args": [
          "abcda"
        ]
      },
      "expected": "a"
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          "cbbd"
        ]
      },
      "expected": "bb"
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          "a"
        ]
      },
      "expected": "a"
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          "bb"
        ]
      },
      "expected": "bb"
    },
    {
      "name": "case_39_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": ""
    },
    {
      "name": "case_40_edge_all_same",
      "input": {
        "args": [
          "aaaa"
        ]
      },
      "expected": "aaaa"
    }
  ]
}
```
