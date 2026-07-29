# 题目76 最小覆盖子串

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个字符串 `s` 、一个字符串 `t` 。返回 `s` 中涵盖 `t` 所有字符的最小子串。如果 `s` 中不存在涵盖 `t` 所有字符的子串，则返回空字符串 `""` 。
注意：
对于 `t` 中重复字符，我们寻找的子字符串中该字符数量必须不少于 `t` 中该字符数量。
如果 `s` 中存在这样的子串，我们保证它是唯一的答案。
示例 1：
输入：s = "ADOBECODEBANC", t = "ABC"输出："BANC"
示例 2：
输入：s = "a", t = "a"输出："a"
示例 3:
输入: s = "a", t = "aa"输出: ""解释: t 中两个字符 'a' 均应包含在 s 的子串中，因此没有符合条件的子字符串，返回空字符串。
提示：
1 <= s.length, t.length <= 10<sup>5</sup>
`s` 和 `t` 由英文字母组成
进阶：你能设计一个在 `o(n)` 时间内解决此问题的算法吗？

```json
{
  "id": 76,
  "title": "最小覆盖子串",
  "difficulty": "困难",
  "method": "question_76",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          "ADOBECODEBANC",
          "ABC"
        ]
      },
      "expected": "BANC"
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          "a",
          "a"
        ]
      },
      "expected": "a"
    },
    {
      "name": "case_03_base",
      "input": {
        "args": [
          "a",
          "aa"
        ]
      },
      "expected": ""
    },
    {
      "name": "case_04_edge_t_longer_than_s",
      "input": {
        "args": [
          "A",
          "AA"
        ]
      },
      "expected": ""
    },
    {
      "name": "case_05_edge_full_match",
      "input": {
        "args": [
          "AA",
          "AA"
        ]
      },
      "expected": "AA"
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          "ADOBECODEBANC",
          "ABC"
        ]
      },
      "expected": "BANC"
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          "a",
          "a"
        ]
      },
      "expected": "a"
    },
    {
      "name": "case_08_base",
      "input": {
        "args": [
          "a",
          "aa"
        ]
      },
      "expected": ""
    },
    {
      "name": "case_09_edge_t_longer_than_s",
      "input": {
        "args": [
          "A",
          "AA"
        ]
      },
      "expected": ""
    },
    {
      "name": "case_10_edge_full_match",
      "input": {
        "args": [
          "AA",
          "AA"
        ]
      },
      "expected": "AA"
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          "ADOBECODEBANC",
          "ABC"
        ]
      },
      "expected": "BANC"
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          "a",
          "a"
        ]
      },
      "expected": "a"
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          "a",
          "aa"
        ]
      },
      "expected": ""
    },
    {
      "name": "case_14_edge_t_longer_than_s",
      "input": {
        "args": [
          "A",
          "AA"
        ]
      },
      "expected": ""
    },
    {
      "name": "case_15_edge_full_match",
      "input": {
        "args": [
          "AA",
          "AA"
        ]
      },
      "expected": "AA"
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          "ADOBECODEBANC",
          "ABC"
        ]
      },
      "expected": "BANC"
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          "a",
          "a"
        ]
      },
      "expected": "a"
    },
    {
      "name": "case_18_base",
      "input": {
        "args": [
          "a",
          "aa"
        ]
      },
      "expected": ""
    },
    {
      "name": "case_19_edge_t_longer_than_s",
      "input": {
        "args": [
          "A",
          "AA"
        ]
      },
      "expected": ""
    },
    {
      "name": "case_20_edge_full_match",
      "input": {
        "args": [
          "AA",
          "AA"
        ]
      },
      "expected": "AA"
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          "ADOBECODEBANC",
          "ABC"
        ]
      },
      "expected": "BANC"
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          "a",
          "a"
        ]
      },
      "expected": "a"
    },
    {
      "name": "case_23_base",
      "input": {
        "args": [
          "a",
          "aa"
        ]
      },
      "expected": ""
    },
    {
      "name": "case_24_edge_t_longer_than_s",
      "input": {
        "args": [
          "A",
          "AA"
        ]
      },
      "expected": ""
    },
    {
      "name": "case_25_edge_full_match",
      "input": {
        "args": [
          "AA",
          "AA"
        ]
      },
      "expected": "AA"
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          "ADOBECODEBANC",
          "ABC"
        ]
      },
      "expected": "BANC"
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          "a",
          "a"
        ]
      },
      "expected": "a"
    },
    {
      "name": "case_28_base",
      "input": {
        "args": [
          "a",
          "aa"
        ]
      },
      "expected": ""
    },
    {
      "name": "case_29_edge_t_longer_than_s",
      "input": {
        "args": [
          "A",
          "AA"
        ]
      },
      "expected": ""
    },
    {
      "name": "case_30_edge_full_match",
      "input": {
        "args": [
          "AA",
          "AA"
        ]
      },
      "expected": "AA"
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          "ADOBECODEBANC",
          "ABC"
        ]
      },
      "expected": "BANC"
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          "a",
          "a"
        ]
      },
      "expected": "a"
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          "a",
          "aa"
        ]
      },
      "expected": ""
    },
    {
      "name": "case_34_edge_t_longer_than_s",
      "input": {
        "args": [
          "A",
          "AA"
        ]
      },
      "expected": ""
    },
    {
      "name": "case_35_edge_full_match",
      "input": {
        "args": [
          "AA",
          "AA"
        ]
      },
      "expected": "AA"
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          "ADOBECODEBANC",
          "ABC"
        ]
      },
      "expected": "BANC"
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          "a",
          "a"
        ]
      },
      "expected": "a"
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          "a",
          "aa"
        ]
      },
      "expected": ""
    },
    {
      "name": "case_39_edge_t_longer_than_s",
      "input": {
        "args": [
          "A",
          "AA"
        ]
      },
      "expected": ""
    },
    {
      "name": "case_40_edge_full_match",
      "input": {
        "args": [
          "AA",
          "AA"
        ]
      },
      "expected": "AA"
    }
  ]
}
```
