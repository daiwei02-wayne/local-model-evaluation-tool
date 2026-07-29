# 题目3 无重复字符的最长子串

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一个字符串 `s` ，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: s = "abcabcbb"输出: 3解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: s = "bbbbb"输出: 1解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: s = "pwwkew"输出: 3解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
提示：
0 <= s.length <= 5 * 10<sup>4</sup>
`s` 由英文字母、数字、符号和空格组成

```json
{
  "id": 3,
  "title": "无重复字符的最长子串",
  "difficulty": "中等",
  "method": "question_3",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          "abcabcbb"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          "bbbbb"
        ]
      },
      "expected": 1
    },
    {
      "name": "case_03_base",
      "input": {
        "args": [
          "pwwkew"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_04_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": 0
    },
    {
      "name": "case_05_edge_space",
      "input": {
        "args": [
          " "
        ]
      },
      "expected": 1
    },
    {
      "name": "case_06_edge_repeat_inside",
      "input": {
        "args": [
          "dvdf"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_07_edge_shrink_left",
      "input": {
        "args": [
          "abba"
        ]
      },
      "expected": 2
    },
    {
      "name": "case_08_base",
      "input": {
        "args": [
          "abcabcbb"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          "bbbbb"
        ]
      },
      "expected": 1
    },
    {
      "name": "case_10_base",
      "input": {
        "args": [
          "pwwkew"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_11_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": 0
    },
    {
      "name": "case_12_edge_space",
      "input": {
        "args": [
          " "
        ]
      },
      "expected": 1
    },
    {
      "name": "case_13_edge_repeat_inside",
      "input": {
        "args": [
          "dvdf"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_14_edge_shrink_left",
      "input": {
        "args": [
          "abba"
        ]
      },
      "expected": 2
    },
    {
      "name": "case_15_base",
      "input": {
        "args": [
          "abcabcbb"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          "bbbbb"
        ]
      },
      "expected": 1
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          "pwwkew"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_18_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": 0
    },
    {
      "name": "case_19_edge_space",
      "input": {
        "args": [
          " "
        ]
      },
      "expected": 1
    },
    {
      "name": "case_20_edge_repeat_inside",
      "input": {
        "args": [
          "dvdf"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_21_edge_shrink_left",
      "input": {
        "args": [
          "abba"
        ]
      },
      "expected": 2
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          "abcabcbb"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_23_base",
      "input": {
        "args": [
          "bbbbb"
        ]
      },
      "expected": 1
    },
    {
      "name": "case_24_base",
      "input": {
        "args": [
          "pwwkew"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_25_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": 0
    },
    {
      "name": "case_26_edge_space",
      "input": {
        "args": [
          " "
        ]
      },
      "expected": 1
    },
    {
      "name": "case_27_edge_repeat_inside",
      "input": {
        "args": [
          "dvdf"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_28_edge_shrink_left",
      "input": {
        "args": [
          "abba"
        ]
      },
      "expected": 2
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          "abcabcbb"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_30_base",
      "input": {
        "args": [
          "bbbbb"
        ]
      },
      "expected": 1
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          "pwwkew"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_32_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": 0
    },
    {
      "name": "case_33_edge_space",
      "input": {
        "args": [
          " "
        ]
      },
      "expected": 1
    },
    {
      "name": "case_34_edge_repeat_inside",
      "input": {
        "args": [
          "dvdf"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_35_edge_shrink_left",
      "input": {
        "args": [
          "abba"
        ]
      },
      "expected": 2
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          "abcabcbb"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          "bbbbb"
        ]
      },
      "expected": 1
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          "pwwkew"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_39_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": 0
    },
    {
      "name": "case_40_edge_space",
      "input": {
        "args": [
          " "
        ]
      },
      "expected": 1
    }
  ]
}
```
