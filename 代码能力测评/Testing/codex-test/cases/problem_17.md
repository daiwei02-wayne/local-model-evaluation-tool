# 题目17 电话号码的字母组合

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一个仅包含数字 `2-9` 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
题目配图：
示例 1：
输入：digits = "23"输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：
输入：digits = ""输出：[]
示例 3：
输入：digits = "2"输出：["a","b","c"]
提示：
`0 <= digits.length <= 4`
`digits[i]` 是范围 `['2', '9']` 的一个数字。

```json
{
  "id": 17,
  "title": "电话号码的字母组合",
  "difficulty": "中等",
  "method": "question_17",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          "23"
        ]
      },
      "expected": [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": [],
      "comparison": "any_order"
    },
    {
      "name": "case_03_edge_single_digit",
      "input": {
        "args": [
          "2"
        ]
      },
      "comparison": "any_order",
      "expected": [
        "a",
        "b",
        "c"
      ]
    },
    {
      "name": "case_04_edge_four_letter_digits",
      "input": {
        "args": [
          "79"
        ]
      },
      "comparison": "any_order",
      "expected": [
        "pw",
        "px",
        "py",
        "pz",
        "qw",
        "qx",
        "qy",
        "qz",
        "rw",
        "rx",
        "ry",
        "rz",
        "sw",
        "sx",
        "sy",
        "sz"
      ]
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          "23"
        ]
      },
      "expected": [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": [],
      "comparison": "any_order"
    },
    {
      "name": "case_07_edge_single_digit",
      "input": {
        "args": [
          "2"
        ]
      },
      "comparison": "any_order",
      "expected": [
        "a",
        "b",
        "c"
      ]
    },
    {
      "name": "case_08_edge_four_letter_digits",
      "input": {
        "args": [
          "79"
        ]
      },
      "comparison": "any_order",
      "expected": [
        "pw",
        "px",
        "py",
        "pz",
        "qw",
        "qx",
        "qy",
        "qz",
        "rw",
        "rx",
        "ry",
        "rz",
        "sw",
        "sx",
        "sy",
        "sz"
      ]
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          "23"
        ]
      },
      "expected": [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_10_base",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": [],
      "comparison": "any_order"
    },
    {
      "name": "case_11_edge_single_digit",
      "input": {
        "args": [
          "2"
        ]
      },
      "comparison": "any_order",
      "expected": [
        "a",
        "b",
        "c"
      ]
    },
    {
      "name": "case_12_edge_four_letter_digits",
      "input": {
        "args": [
          "79"
        ]
      },
      "comparison": "any_order",
      "expected": [
        "pw",
        "px",
        "py",
        "pz",
        "qw",
        "qx",
        "qy",
        "qz",
        "rw",
        "rx",
        "ry",
        "rz",
        "sw",
        "sx",
        "sy",
        "sz"
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          "23"
        ]
      },
      "expected": [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_14_base",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": [],
      "comparison": "any_order"
    },
    {
      "name": "case_15_edge_single_digit",
      "input": {
        "args": [
          "2"
        ]
      },
      "comparison": "any_order",
      "expected": [
        "a",
        "b",
        "c"
      ]
    },
    {
      "name": "case_16_edge_four_letter_digits",
      "input": {
        "args": [
          "79"
        ]
      },
      "comparison": "any_order",
      "expected": [
        "pw",
        "px",
        "py",
        "pz",
        "qw",
        "qx",
        "qy",
        "qz",
        "rw",
        "rx",
        "ry",
        "rz",
        "sw",
        "sx",
        "sy",
        "sz"
      ]
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          "23"
        ]
      },
      "expected": [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_18_base",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": [],
      "comparison": "any_order"
    },
    {
      "name": "case_19_edge_single_digit",
      "input": {
        "args": [
          "2"
        ]
      },
      "comparison": "any_order",
      "expected": [
        "a",
        "b",
        "c"
      ]
    },
    {
      "name": "case_20_edge_four_letter_digits",
      "input": {
        "args": [
          "79"
        ]
      },
      "comparison": "any_order",
      "expected": [
        "pw",
        "px",
        "py",
        "pz",
        "qw",
        "qx",
        "qy",
        "qz",
        "rw",
        "rx",
        "ry",
        "rz",
        "sw",
        "sx",
        "sy",
        "sz"
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          "23"
        ]
      },
      "expected": [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": [],
      "comparison": "any_order"
    },
    {
      "name": "case_23_edge_single_digit",
      "input": {
        "args": [
          "2"
        ]
      },
      "comparison": "any_order",
      "expected": [
        "a",
        "b",
        "c"
      ]
    },
    {
      "name": "case_24_edge_four_letter_digits",
      "input": {
        "args": [
          "79"
        ]
      },
      "comparison": "any_order",
      "expected": [
        "pw",
        "px",
        "py",
        "pz",
        "qw",
        "qx",
        "qy",
        "qz",
        "rw",
        "rx",
        "ry",
        "rz",
        "sw",
        "sx",
        "sy",
        "sz"
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          "23"
        ]
      },
      "expected": [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": [],
      "comparison": "any_order"
    },
    {
      "name": "case_27_edge_single_digit",
      "input": {
        "args": [
          "2"
        ]
      },
      "comparison": "any_order",
      "expected": [
        "a",
        "b",
        "c"
      ]
    },
    {
      "name": "case_28_edge_four_letter_digits",
      "input": {
        "args": [
          "79"
        ]
      },
      "comparison": "any_order",
      "expected": [
        "pw",
        "px",
        "py",
        "pz",
        "qw",
        "qx",
        "qy",
        "qz",
        "rw",
        "rx",
        "ry",
        "rz",
        "sw",
        "sx",
        "sy",
        "sz"
      ]
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          "23"
        ]
      },
      "expected": [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_30_base",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": [],
      "comparison": "any_order"
    },
    {
      "name": "case_31_edge_single_digit",
      "input": {
        "args": [
          "2"
        ]
      },
      "comparison": "any_order",
      "expected": [
        "a",
        "b",
        "c"
      ]
    },
    {
      "name": "case_32_edge_four_letter_digits",
      "input": {
        "args": [
          "79"
        ]
      },
      "comparison": "any_order",
      "expected": [
        "pw",
        "px",
        "py",
        "pz",
        "qw",
        "qx",
        "qy",
        "qz",
        "rw",
        "rx",
        "ry",
        "rz",
        "sw",
        "sx",
        "sy",
        "sz"
      ]
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          "23"
        ]
      },
      "expected": [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_34_base",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": [],
      "comparison": "any_order"
    },
    {
      "name": "case_35_edge_single_digit",
      "input": {
        "args": [
          "2"
        ]
      },
      "comparison": "any_order",
      "expected": [
        "a",
        "b",
        "c"
      ]
    },
    {
      "name": "case_36_edge_four_letter_digits",
      "input": {
        "args": [
          "79"
        ]
      },
      "comparison": "any_order",
      "expected": [
        "pw",
        "px",
        "py",
        "pz",
        "qw",
        "qx",
        "qy",
        "qz",
        "rw",
        "rx",
        "ry",
        "rz",
        "sw",
        "sx",
        "sy",
        "sz"
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          "23"
        ]
      },
      "expected": [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf"
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          ""
        ]
      },
      "expected": [],
      "comparison": "any_order"
    },
    {
      "name": "case_39_edge_single_digit",
      "input": {
        "args": [
          "2"
        ]
      },
      "comparison": "any_order",
      "expected": [
        "a",
        "b",
        "c"
      ]
    },
    {
      "name": "case_40_edge_four_letter_digits",
      "input": {
        "args": [
          "79"
        ]
      },
      "comparison": "any_order",
      "expected": [
        "pw",
        "px",
        "py",
        "pz",
        "qw",
        "qx",
        "qy",
        "qz",
        "rw",
        "rx",
        "ry",
        "rz",
        "sw",
        "sx",
        "sy",
        "sz"
      ]
    }
  ]
}
```
