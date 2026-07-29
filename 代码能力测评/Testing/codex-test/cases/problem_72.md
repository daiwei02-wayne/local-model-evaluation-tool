# 题目72 编辑距离

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你两个单词 `word1` 和 `word2`， _请返回将 `word1` 转换成 `word2` 所使用的最少操作数_  。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符
示例 1：
输入：word1 = "horse", word2 = "ros"输出：3解释：horse -> rorse (将 'h' 替换为 'r')rorse -> rose (删除 'r')rose -> ros (删除 'e')
示例 2：
输入：word1 = "intention", word2 = "execution"输出：5解释：intention -> inention (删除 't')inention -> enention (将 'i' 替换为 'e')enention -> exention (将 'n' 替换为 'x')exention -> exection (将 'n' 替换为 'c')exection -> execution (插入 'u')
提示：
`0 <= word1.length, word2.length <= 500`
`word1` 和 `word2` 由小写英文字母组成

```json
{
  "id": 72,
  "title": "编辑距离",
  "difficulty": "困难",
  "method": "question_72",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          "horse",
          "ros"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          "intention",
          "execution"
        ]
      },
      "expected": 5
    },
    {
      "name": "case_03_edge_both_empty",
      "input": {
        "args": [
          "",
          ""
        ]
      },
      "expected": 0
    },
    {
      "name": "case_04_edge_insert_all",
      "input": {
        "args": [
          "",
          "abc"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_05_edge_delete_all",
      "input": {
        "args": [
          "abc",
          ""
        ]
      },
      "expected": 3
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          "horse",
          "ros"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          "intention",
          "execution"
        ]
      },
      "expected": 5
    },
    {
      "name": "case_08_edge_both_empty",
      "input": {
        "args": [
          "",
          ""
        ]
      },
      "expected": 0
    },
    {
      "name": "case_09_edge_insert_all",
      "input": {
        "args": [
          "",
          "abc"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_10_edge_delete_all",
      "input": {
        "args": [
          "abc",
          ""
        ]
      },
      "expected": 3
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          "horse",
          "ros"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          "intention",
          "execution"
        ]
      },
      "expected": 5
    },
    {
      "name": "case_13_edge_both_empty",
      "input": {
        "args": [
          "",
          ""
        ]
      },
      "expected": 0
    },
    {
      "name": "case_14_edge_insert_all",
      "input": {
        "args": [
          "",
          "abc"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_15_edge_delete_all",
      "input": {
        "args": [
          "abc",
          ""
        ]
      },
      "expected": 3
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          "horse",
          "ros"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          "intention",
          "execution"
        ]
      },
      "expected": 5
    },
    {
      "name": "case_18_edge_both_empty",
      "input": {
        "args": [
          "",
          ""
        ]
      },
      "expected": 0
    },
    {
      "name": "case_19_edge_insert_all",
      "input": {
        "args": [
          "",
          "abc"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_20_edge_delete_all",
      "input": {
        "args": [
          "abc",
          ""
        ]
      },
      "expected": 3
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          "horse",
          "ros"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          "intention",
          "execution"
        ]
      },
      "expected": 5
    },
    {
      "name": "case_23_edge_both_empty",
      "input": {
        "args": [
          "",
          ""
        ]
      },
      "expected": 0
    },
    {
      "name": "case_24_edge_insert_all",
      "input": {
        "args": [
          "",
          "abc"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_25_edge_delete_all",
      "input": {
        "args": [
          "abc",
          ""
        ]
      },
      "expected": 3
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          "horse",
          "ros"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          "intention",
          "execution"
        ]
      },
      "expected": 5
    },
    {
      "name": "case_28_edge_both_empty",
      "input": {
        "args": [
          "",
          ""
        ]
      },
      "expected": 0
    },
    {
      "name": "case_29_edge_insert_all",
      "input": {
        "args": [
          "",
          "abc"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_30_edge_delete_all",
      "input": {
        "args": [
          "abc",
          ""
        ]
      },
      "expected": 3
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          "horse",
          "ros"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          "intention",
          "execution"
        ]
      },
      "expected": 5
    },
    {
      "name": "case_33_edge_both_empty",
      "input": {
        "args": [
          "",
          ""
        ]
      },
      "expected": 0
    },
    {
      "name": "case_34_edge_insert_all",
      "input": {
        "args": [
          "",
          "abc"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_35_edge_delete_all",
      "input": {
        "args": [
          "abc",
          ""
        ]
      },
      "expected": 3
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          "horse",
          "ros"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          "intention",
          "execution"
        ]
      },
      "expected": 5
    },
    {
      "name": "case_38_edge_both_empty",
      "input": {
        "args": [
          "",
          ""
        ]
      },
      "expected": 0
    },
    {
      "name": "case_39_edge_insert_all",
      "input": {
        "args": [
          "",
          "abc"
        ]
      },
      "expected": 3
    },
    {
      "name": "case_40_edge_delete_all",
      "input": {
        "args": [
          "abc",
          ""
        ]
      },
      "expected": 3
    }
  ]
}
```
