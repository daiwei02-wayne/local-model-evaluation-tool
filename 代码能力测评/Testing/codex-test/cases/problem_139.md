# 题目139 单词拆分

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个字符串 `s` 和一个字符串列表 `wordDict` 作为字典。请你判断是否可以利用字典中出现的单词拼接出 `s` 。
注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]输出: true解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]输出: true解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。     注意，你可以重复使用字典中的单词。
示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]输出: false
提示：
`1 <= s.length <= 300`
`1 <= wordDict.length <= 1000`
`1 <= wordDict[i].length <= 20`
`s` 和 `wordDict[i]` 仅有小写英文字母组成
`wordDict` 中的所有字符串 互不相同

```json
{
  "id": 139,
  "title": "单词拆分",
  "difficulty": "中等",
  "method": "question_139",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          "leetcode",
          [
            "leet",
            "code"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          "catsandog",
          [
            "cats",
            "dog",
            "sand",
            "and",
            "cat"
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_03_edge_empty_s",
      "input": {
        "args": [
          "",
          [
            "a"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_04_edge_overlap_words",
      "input": {
        "args": [
          "aaaaaaa",
          [
            "aaaa",
            "aaa"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          "leetcode",
          [
            "leet",
            "code"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          "catsandog",
          [
            "cats",
            "dog",
            "sand",
            "and",
            "cat"
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_07_edge_empty_s",
      "input": {
        "args": [
          "",
          [
            "a"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_08_edge_overlap_words",
      "input": {
        "args": [
          "aaaaaaa",
          [
            "aaaa",
            "aaa"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          "leetcode",
          [
            "leet",
            "code"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_10_base",
      "input": {
        "args": [
          "catsandog",
          [
            "cats",
            "dog",
            "sand",
            "and",
            "cat"
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_11_edge_empty_s",
      "input": {
        "args": [
          "",
          [
            "a"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_12_edge_overlap_words",
      "input": {
        "args": [
          "aaaaaaa",
          [
            "aaaa",
            "aaa"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          "leetcode",
          [
            "leet",
            "code"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_14_base",
      "input": {
        "args": [
          "catsandog",
          [
            "cats",
            "dog",
            "sand",
            "and",
            "cat"
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_15_edge_empty_s",
      "input": {
        "args": [
          "",
          [
            "a"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_16_edge_overlap_words",
      "input": {
        "args": [
          "aaaaaaa",
          [
            "aaaa",
            "aaa"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          "leetcode",
          [
            "leet",
            "code"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_18_base",
      "input": {
        "args": [
          "catsandog",
          [
            "cats",
            "dog",
            "sand",
            "and",
            "cat"
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_19_edge_empty_s",
      "input": {
        "args": [
          "",
          [
            "a"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_20_edge_overlap_words",
      "input": {
        "args": [
          "aaaaaaa",
          [
            "aaaa",
            "aaa"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          "leetcode",
          [
            "leet",
            "code"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          "catsandog",
          [
            "cats",
            "dog",
            "sand",
            "and",
            "cat"
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_23_edge_empty_s",
      "input": {
        "args": [
          "",
          [
            "a"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_24_edge_overlap_words",
      "input": {
        "args": [
          "aaaaaaa",
          [
            "aaaa",
            "aaa"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          "leetcode",
          [
            "leet",
            "code"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          "catsandog",
          [
            "cats",
            "dog",
            "sand",
            "and",
            "cat"
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_27_edge_empty_s",
      "input": {
        "args": [
          "",
          [
            "a"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_28_edge_overlap_words",
      "input": {
        "args": [
          "aaaaaaa",
          [
            "aaaa",
            "aaa"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          "leetcode",
          [
            "leet",
            "code"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_30_base",
      "input": {
        "args": [
          "catsandog",
          [
            "cats",
            "dog",
            "sand",
            "and",
            "cat"
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_31_edge_empty_s",
      "input": {
        "args": [
          "",
          [
            "a"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_32_edge_overlap_words",
      "input": {
        "args": [
          "aaaaaaa",
          [
            "aaaa",
            "aaa"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          "leetcode",
          [
            "leet",
            "code"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_34_base",
      "input": {
        "args": [
          "catsandog",
          [
            "cats",
            "dog",
            "sand",
            "and",
            "cat"
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_35_edge_empty_s",
      "input": {
        "args": [
          "",
          [
            "a"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_36_edge_overlap_words",
      "input": {
        "args": [
          "aaaaaaa",
          [
            "aaaa",
            "aaa"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          "leetcode",
          [
            "leet",
            "code"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          "catsandog",
          [
            "cats",
            "dog",
            "sand",
            "and",
            "cat"
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_39_edge_empty_s",
      "input": {
        "args": [
          "",
          [
            "a"
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_40_edge_overlap_words",
      "input": {
        "args": [
          "aaaaaaa",
          [
            "aaaa",
            "aaa"
          ]
        ]
      },
      "expected": true
    }
  ]
}
```
