# 题目32 最长有效括号

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个只包含 `'('` 和 `')'` 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
示例 1：
输入：s = "(()"输出：2解释：最长有效括号子串是 "()"
示例 2：
输入：s = ")()())"输出：4解释：最长有效括号子串是 "()()"
示例 3：
输入：s = ""输出：0
提示：
0 <= s.length <= 3 * 10<sup>4</sup>
`s[i]` 为 `'('` 或 `')'`

```json
{
  "id": 32,
  "title": "最长有效括号",
  "difficulty": "困难",
  "method": "question_32",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          "(()"
        ]
      },
      "expected": 2
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          ")()())"
        ]
      },
      "expected": 4
    },
    {
      "name": "case_03_base",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": 0
    },
    {
      "name": "case_04_edge_unclosed_suffix",
      "input": {
        "args": [
          "()(()"
        ]
      },
      "expected": 2
    },
    {
      "name": "case_05_edge_nested_valid",
      "input": {
        "args": [
          "()(())"
        ]
      },
      "expected": 6
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          "(()"
        ]
      },
      "expected": 2
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          ")()())"
        ]
      },
      "expected": 4
    },
    {
      "name": "case_08_base",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": 0
    },
    {
      "name": "case_09_edge_unclosed_suffix",
      "input": {
        "args": [
          "()(()"
        ]
      },
      "expected": 2
    },
    {
      "name": "case_10_edge_nested_valid",
      "input": {
        "args": [
          "()(())"
        ]
      },
      "expected": 6
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          "(()"
        ]
      },
      "expected": 2
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          ")()())"
        ]
      },
      "expected": 4
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": 0
    },
    {
      "name": "case_14_edge_unclosed_suffix",
      "input": {
        "args": [
          "()(()"
        ]
      },
      "expected": 2
    },
    {
      "name": "case_15_edge_nested_valid",
      "input": {
        "args": [
          "()(())"
        ]
      },
      "expected": 6
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          "(()"
        ]
      },
      "expected": 2
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          ")()())"
        ]
      },
      "expected": 4
    },
    {
      "name": "case_18_base",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": 0
    },
    {
      "name": "case_19_edge_unclosed_suffix",
      "input": {
        "args": [
          "()(()"
        ]
      },
      "expected": 2
    },
    {
      "name": "case_20_edge_nested_valid",
      "input": {
        "args": [
          "()(())"
        ]
      },
      "expected": 6
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          "(()"
        ]
      },
      "expected": 2
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          ")()())"
        ]
      },
      "expected": 4
    },
    {
      "name": "case_23_base",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": 0
    },
    {
      "name": "case_24_edge_unclosed_suffix",
      "input": {
        "args": [
          "()(()"
        ]
      },
      "expected": 2
    },
    {
      "name": "case_25_edge_nested_valid",
      "input": {
        "args": [
          "()(())"
        ]
      },
      "expected": 6
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          "(()"
        ]
      },
      "expected": 2
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          ")()())"
        ]
      },
      "expected": 4
    },
    {
      "name": "case_28_base",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": 0
    },
    {
      "name": "case_29_edge_unclosed_suffix",
      "input": {
        "args": [
          "()(()"
        ]
      },
      "expected": 2
    },
    {
      "name": "case_30_edge_nested_valid",
      "input": {
        "args": [
          "()(())"
        ]
      },
      "expected": 6
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          "(()"
        ]
      },
      "expected": 2
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          ")()())"
        ]
      },
      "expected": 4
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": 0
    },
    {
      "name": "case_34_edge_unclosed_suffix",
      "input": {
        "args": [
          "()(()"
        ]
      },
      "expected": 2
    },
    {
      "name": "case_35_edge_nested_valid",
      "input": {
        "args": [
          "()(())"
        ]
      },
      "expected": 6
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          "(()"
        ]
      },
      "expected": 2
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          ")()())"
        ]
      },
      "expected": 4
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": 0
    },
    {
      "name": "case_39_edge_unclosed_suffix",
      "input": {
        "args": [
          "()(()"
        ]
      },
      "expected": 2
    },
    {
      "name": "case_40_edge_nested_valid",
      "input": {
        "args": [
          "()(())"
        ]
      },
      "expected": 6
    }
  ]
}
```
