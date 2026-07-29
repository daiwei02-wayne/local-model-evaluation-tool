# 题目763 划分字母区间

来源：LeetCode 热题 100（https://leetcode.cn/studyplan/top-100-liked/）

```json
{
  "id": 763,
  "title": "划分字母区间",
  "difficulty": "中等",
  "method": "question_763",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          "ababcbacadefegdehijhklij"
        ]
      },
      "expected": [
        9,
        7,
        8
      ]
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          "eccbbbbdec"
        ]
      },
      "expected": [
        10
      ]
    },
    {
      "name": "case_03_base",
      "input": {
        "args": [
          "a"
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_04_edge_all_same",
      "input": {
        "args": [
          "aaaa"
        ]
      },
      "expected": [
        4
      ]
    },
    {
      "name": "case_05_edge_all_single_parts",
      "input": {
        "args": [
          "abc"
        ]
      },
      "expected": [
        1,
        1,
        1
      ]
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          "ababcbacadefegdehijhklij"
        ]
      },
      "expected": [
        9,
        7,
        8
      ]
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          "eccbbbbdec"
        ]
      },
      "expected": [
        10
      ]
    },
    {
      "name": "case_08_base",
      "input": {
        "args": [
          "a"
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_09_edge_all_same",
      "input": {
        "args": [
          "aaaa"
        ]
      },
      "expected": [
        4
      ]
    },
    {
      "name": "case_10_edge_all_single_parts",
      "input": {
        "args": [
          "abc"
        ]
      },
      "expected": [
        1,
        1,
        1
      ]
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          "ababcbacadefegdehijhklij"
        ]
      },
      "expected": [
        9,
        7,
        8
      ]
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          "eccbbbbdec"
        ]
      },
      "expected": [
        10
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          "a"
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_14_edge_all_same",
      "input": {
        "args": [
          "aaaa"
        ]
      },
      "expected": [
        4
      ]
    },
    {
      "name": "case_15_edge_all_single_parts",
      "input": {
        "args": [
          "abc"
        ]
      },
      "expected": [
        1,
        1,
        1
      ]
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          "ababcbacadefegdehijhklij"
        ]
      },
      "expected": [
        9,
        7,
        8
      ]
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          "eccbbbbdec"
        ]
      },
      "expected": [
        10
      ]
    },
    {
      "name": "case_18_base",
      "input": {
        "args": [
          "a"
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_19_edge_all_same",
      "input": {
        "args": [
          "aaaa"
        ]
      },
      "expected": [
        4
      ]
    },
    {
      "name": "case_20_edge_all_single_parts",
      "input": {
        "args": [
          "abc"
        ]
      },
      "expected": [
        1,
        1,
        1
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          "ababcbacadefegdehijhklij"
        ]
      },
      "expected": [
        9,
        7,
        8
      ]
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          "eccbbbbdec"
        ]
      },
      "expected": [
        10
      ]
    },
    {
      "name": "case_23_base",
      "input": {
        "args": [
          "a"
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_24_edge_all_same",
      "input": {
        "args": [
          "aaaa"
        ]
      },
      "expected": [
        4
      ]
    },
    {
      "name": "case_25_edge_all_single_parts",
      "input": {
        "args": [
          "abc"
        ]
      },
      "expected": [
        1,
        1,
        1
      ]
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          "ababcbacadefegdehijhklij"
        ]
      },
      "expected": [
        9,
        7,
        8
      ]
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          "eccbbbbdec"
        ]
      },
      "expected": [
        10
      ]
    },
    {
      "name": "case_28_base",
      "input": {
        "args": [
          "a"
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_29_edge_all_same",
      "input": {
        "args": [
          "aaaa"
        ]
      },
      "expected": [
        4
      ]
    },
    {
      "name": "case_30_edge_all_single_parts",
      "input": {
        "args": [
          "abc"
        ]
      },
      "expected": [
        1,
        1,
        1
      ]
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          "ababcbacadefegdehijhklij"
        ]
      },
      "expected": [
        9,
        7,
        8
      ]
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          "eccbbbbdec"
        ]
      },
      "expected": [
        10
      ]
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          "a"
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_34_edge_all_same",
      "input": {
        "args": [
          "aaaa"
        ]
      },
      "expected": [
        4
      ]
    },
    {
      "name": "case_35_edge_all_single_parts",
      "input": {
        "args": [
          "abc"
        ]
      },
      "expected": [
        1,
        1,
        1
      ]
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          "ababcbacadefegdehijhklij"
        ]
      },
      "expected": [
        9,
        7,
        8
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          "eccbbbbdec"
        ]
      },
      "expected": [
        10
      ]
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          "a"
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_39_edge_all_same",
      "input": {
        "args": [
          "aaaa"
        ]
      },
      "expected": [
        4
      ]
    },
    {
      "name": "case_40_edge_all_single_parts",
      "input": {
        "args": [
          "abc"
        ]
      },
      "expected": [
        1,
        1,
        1
      ]
    }
  ]
}
```
