# 题目20 有效的括号

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一个只包括 `'('`，`')'`，`'{'`，`'}'`，`'['`，`']'` 的字符串 `s` ，判断字符串是否有效。
有效字符串需满足：
1.  左括号必须用相同类型的右括号闭合。
2.  左括号必须以正确的顺序闭合。
3.  每个右括号都有一个对应的相同类型的左括号。
示例 1：
输入：s = "()"输出：true
示例 2：
输入：s = "()[]{}"输出：true
示例 3：
输入：s = "(]"输出：false
提示：
1 <= s.length <= 10<sup>4</sup>
`s` 仅由括号 `'()[]{}'` 组成

```json
{
  "id": 20,
  "title": "有效的括号",
  "difficulty": "简单",
  "method": "question_20",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          "()"
        ]
      },
      "expected": true
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          "()[]{}"
        ]
      },
      "expected": true
    },
    {
      "name": "case_03_base",
      "input": {
        "args": [
          "(]"
        ]
      },
      "expected": false
    },
    {
      "name": "case_04_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": true
    },
    {
      "name": "case_05_edge_nested",
      "input": {
        "args": [
          "([{}])"
        ]
      },
      "expected": true
    },
    {
      "name": "case_06_edge_unclosed",
      "input": {
        "args": [
          "(("
        ]
      },
      "expected": false
    },
    {
      "name": "case_07_edge_wrong_start",
      "input": {
        "args": [
          "){"
        ]
      },
      "expected": false
    },
    {
      "name": "case_08_base",
      "input": {
        "args": [
          "()"
        ]
      },
      "expected": true
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          "()[]{}"
        ]
      },
      "expected": true
    },
    {
      "name": "case_10_base",
      "input": {
        "args": [
          "(]"
        ]
      },
      "expected": false
    },
    {
      "name": "case_11_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": true
    },
    {
      "name": "case_12_edge_nested",
      "input": {
        "args": [
          "([{}])"
        ]
      },
      "expected": true
    },
    {
      "name": "case_13_edge_unclosed",
      "input": {
        "args": [
          "(("
        ]
      },
      "expected": false
    },
    {
      "name": "case_14_edge_wrong_start",
      "input": {
        "args": [
          "){"
        ]
      },
      "expected": false
    },
    {
      "name": "case_15_base",
      "input": {
        "args": [
          "()"
        ]
      },
      "expected": true
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          "()[]{}"
        ]
      },
      "expected": true
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          "(]"
        ]
      },
      "expected": false
    },
    {
      "name": "case_18_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": true
    },
    {
      "name": "case_19_edge_nested",
      "input": {
        "args": [
          "([{}])"
        ]
      },
      "expected": true
    },
    {
      "name": "case_20_edge_unclosed",
      "input": {
        "args": [
          "(("
        ]
      },
      "expected": false
    },
    {
      "name": "case_21_edge_wrong_start",
      "input": {
        "args": [
          "){"
        ]
      },
      "expected": false
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          "()"
        ]
      },
      "expected": true
    },
    {
      "name": "case_23_base",
      "input": {
        "args": [
          "()[]{}"
        ]
      },
      "expected": true
    },
    {
      "name": "case_24_base",
      "input": {
        "args": [
          "(]"
        ]
      },
      "expected": false
    },
    {
      "name": "case_25_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": true
    },
    {
      "name": "case_26_edge_nested",
      "input": {
        "args": [
          "([{}])"
        ]
      },
      "expected": true
    },
    {
      "name": "case_27_edge_unclosed",
      "input": {
        "args": [
          "(("
        ]
      },
      "expected": false
    },
    {
      "name": "case_28_edge_wrong_start",
      "input": {
        "args": [
          "){"
        ]
      },
      "expected": false
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          "()"
        ]
      },
      "expected": true
    },
    {
      "name": "case_30_base",
      "input": {
        "args": [
          "()[]{}"
        ]
      },
      "expected": true
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          "(]"
        ]
      },
      "expected": false
    },
    {
      "name": "case_32_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": true
    },
    {
      "name": "case_33_edge_nested",
      "input": {
        "args": [
          "([{}])"
        ]
      },
      "expected": true
    },
    {
      "name": "case_34_edge_unclosed",
      "input": {
        "args": [
          "(("
        ]
      },
      "expected": false
    },
    {
      "name": "case_35_edge_wrong_start",
      "input": {
        "args": [
          "){"
        ]
      },
      "expected": false
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          "()"
        ]
      },
      "expected": true
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          "()[]{}"
        ]
      },
      "expected": true
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          "(]"
        ]
      },
      "expected": false
    },
    {
      "name": "case_39_edge_empty",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": true
    },
    {
      "name": "case_40_edge_nested",
      "input": {
        "args": [
          "([{}])"
        ]
      },
      "expected": true
    }
  ]
}
```
