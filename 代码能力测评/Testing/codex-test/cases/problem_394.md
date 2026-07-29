# 题目394 字符串解码

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: `k[encoded_string]`，表示其中方括号内部的 `encoded_string` 正好重复 `k` 次。注意 `k` 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 `k` ，例如不会出现像 `3a` 或 `2[4]` 的输入。
示例 1：
输入：s = "3[a]2[bc]"输出："aaabcbc"
示例 2：
输入：s = "3[a2[c]]"输出："accaccacc"
示例 3：
输入：s = "2[abc]3[cd]ef"输出："abcabccdcdcdef"
示例 4：
输入：s = "abc3[cd]xyz"输出："abccdcdcdxyz"
提示：
`1 <= s.length <= 30`
`s` 由小写英文字母、数字和方括号 `'[]'` 组成
`s` 保证是一个 有效 的输入。
`s` 中所有整数的取值范围为 `[1, 300]`

```json
{
  "id": 394,
  "title": "字符串解码",
  "difficulty": "中等",
  "method": "question_394",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          "3[a]2[bc]"
        ]
      },
      "expected": "aaabcbc"
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          "3[a2[c]]"
        ]
      },
      "expected": "accaccacc"
    },
    {
      "name": "case_03_edge_mixed",
      "input": {
        "args": [
          "abc3[cd]xyz"
        ]
      },
      "expected": "abccdcdcdxyz"
    },
    {
      "name": "case_04_edge_two_digit",
      "input": {
        "args": [
          "10[a]"
        ]
      },
      "expected": "aaaaaaaaaa"
    },
    {
      "name": "case_05_edge_multiple_blocks",
      "input": {
        "args": [
          "2[abc]3[cd]ef"
        ]
      },
      "expected": "abcabccdcdcdef"
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          "3[a]2[bc]"
        ]
      },
      "expected": "aaabcbc"
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          "3[a2[c]]"
        ]
      },
      "expected": "accaccacc"
    },
    {
      "name": "case_08_edge_mixed",
      "input": {
        "args": [
          "abc3[cd]xyz"
        ]
      },
      "expected": "abccdcdcdxyz"
    },
    {
      "name": "case_09_edge_two_digit",
      "input": {
        "args": [
          "10[a]"
        ]
      },
      "expected": "aaaaaaaaaa"
    },
    {
      "name": "case_10_edge_multiple_blocks",
      "input": {
        "args": [
          "2[abc]3[cd]ef"
        ]
      },
      "expected": "abcabccdcdcdef"
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          "3[a]2[bc]"
        ]
      },
      "expected": "aaabcbc"
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          "3[a2[c]]"
        ]
      },
      "expected": "accaccacc"
    },
    {
      "name": "case_13_edge_mixed",
      "input": {
        "args": [
          "abc3[cd]xyz"
        ]
      },
      "expected": "abccdcdcdxyz"
    },
    {
      "name": "case_14_edge_two_digit",
      "input": {
        "args": [
          "10[a]"
        ]
      },
      "expected": "aaaaaaaaaa"
    },
    {
      "name": "case_15_edge_multiple_blocks",
      "input": {
        "args": [
          "2[abc]3[cd]ef"
        ]
      },
      "expected": "abcabccdcdcdef"
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          "3[a]2[bc]"
        ]
      },
      "expected": "aaabcbc"
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          "3[a2[c]]"
        ]
      },
      "expected": "accaccacc"
    },
    {
      "name": "case_18_edge_mixed",
      "input": {
        "args": [
          "abc3[cd]xyz"
        ]
      },
      "expected": "abccdcdcdxyz"
    },
    {
      "name": "case_19_edge_two_digit",
      "input": {
        "args": [
          "10[a]"
        ]
      },
      "expected": "aaaaaaaaaa"
    },
    {
      "name": "case_20_edge_multiple_blocks",
      "input": {
        "args": [
          "2[abc]3[cd]ef"
        ]
      },
      "expected": "abcabccdcdcdef"
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          "3[a]2[bc]"
        ]
      },
      "expected": "aaabcbc"
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          "3[a2[c]]"
        ]
      },
      "expected": "accaccacc"
    },
    {
      "name": "case_23_edge_mixed",
      "input": {
        "args": [
          "abc3[cd]xyz"
        ]
      },
      "expected": "abccdcdcdxyz"
    },
    {
      "name": "case_24_edge_two_digit",
      "input": {
        "args": [
          "10[a]"
        ]
      },
      "expected": "aaaaaaaaaa"
    },
    {
      "name": "case_25_edge_multiple_blocks",
      "input": {
        "args": [
          "2[abc]3[cd]ef"
        ]
      },
      "expected": "abcabccdcdcdef"
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          "3[a]2[bc]"
        ]
      },
      "expected": "aaabcbc"
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          "3[a2[c]]"
        ]
      },
      "expected": "accaccacc"
    },
    {
      "name": "case_28_edge_mixed",
      "input": {
        "args": [
          "abc3[cd]xyz"
        ]
      },
      "expected": "abccdcdcdxyz"
    },
    {
      "name": "case_29_edge_two_digit",
      "input": {
        "args": [
          "10[a]"
        ]
      },
      "expected": "aaaaaaaaaa"
    },
    {
      "name": "case_30_edge_multiple_blocks",
      "input": {
        "args": [
          "2[abc]3[cd]ef"
        ]
      },
      "expected": "abcabccdcdcdef"
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          "3[a]2[bc]"
        ]
      },
      "expected": "aaabcbc"
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          "3[a2[c]]"
        ]
      },
      "expected": "accaccacc"
    },
    {
      "name": "case_33_edge_mixed",
      "input": {
        "args": [
          "abc3[cd]xyz"
        ]
      },
      "expected": "abccdcdcdxyz"
    },
    {
      "name": "case_34_edge_two_digit",
      "input": {
        "args": [
          "10[a]"
        ]
      },
      "expected": "aaaaaaaaaa"
    },
    {
      "name": "case_35_edge_multiple_blocks",
      "input": {
        "args": [
          "2[abc]3[cd]ef"
        ]
      },
      "expected": "abcabccdcdcdef"
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          "3[a]2[bc]"
        ]
      },
      "expected": "aaabcbc"
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          "3[a2[c]]"
        ]
      },
      "expected": "accaccacc"
    },
    {
      "name": "case_38_edge_mixed",
      "input": {
        "args": [
          "abc3[cd]xyz"
        ]
      },
      "expected": "abccdcdcdxyz"
    },
    {
      "name": "case_39_edge_two_digit",
      "input": {
        "args": [
          "10[a]"
        ]
      },
      "expected": "aaaaaaaaaa"
    },
    {
      "name": "case_40_edge_multiple_blocks",
      "input": {
        "args": [
          "2[abc]3[cd]ef"
        ]
      },
      "expected": "abcabccdcdcdef"
    }
  ]
}
```
