# 题目322 零钱兑换

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个整数数组 `coins` ，表示不同面额的硬币；以及一个整数 `amount` ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 `-1` 。
你可以认为每种硬币的数量是无限的。
示例 1：
输入：coins = [1, 2, 5], amount = 11输出：3解释：11 = 5 + 5 + 1
示例 2：
输入：coins = [2], amount = 3输出：-1
示例 3：
输入：coins = [1], amount = 0输出：0
提示：
`1 <= coins.length <= 12`
1 <= coins[i] <= 2<sup>31</sup> - 1
0 <= amount <= 10<sup>4</sup>

```json
{
  "id": 322,
  "title": "零钱兑换",
  "difficulty": "中等",
  "method": "question_322",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            1,
            2,
            5
          ],
          11
        ]
      },
      "expected": 3
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            2
          ],
          3
        ]
      },
      "expected": -1
    },
    {
      "name": "case_03_edge_zero_amount",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": 0
    },
    {
      "name": "case_04_edge_non_greedy",
      "input": {
        "args": [
          [
            1,
            3,
            4
          ],
          6
        ]
      },
      "expected": 2
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          [
            1,
            2,
            5
          ],
          11
        ]
      },
      "expected": 3
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            2
          ],
          3
        ]
      },
      "expected": -1
    },
    {
      "name": "case_07_edge_zero_amount",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": 0
    },
    {
      "name": "case_08_edge_non_greedy",
      "input": {
        "args": [
          [
            1,
            3,
            4
          ],
          6
        ]
      },
      "expected": 2
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          [
            1,
            2,
            5
          ],
          11
        ]
      },
      "expected": 3
    },
    {
      "name": "case_10_base",
      "input": {
        "args": [
          [
            2
          ],
          3
        ]
      },
      "expected": -1
    },
    {
      "name": "case_11_edge_zero_amount",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": 0
    },
    {
      "name": "case_12_edge_non_greedy",
      "input": {
        "args": [
          [
            1,
            3,
            4
          ],
          6
        ]
      },
      "expected": 2
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [
            1,
            2,
            5
          ],
          11
        ]
      },
      "expected": 3
    },
    {
      "name": "case_14_base",
      "input": {
        "args": [
          [
            2
          ],
          3
        ]
      },
      "expected": -1
    },
    {
      "name": "case_15_edge_zero_amount",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": 0
    },
    {
      "name": "case_16_edge_non_greedy",
      "input": {
        "args": [
          [
            1,
            3,
            4
          ],
          6
        ]
      },
      "expected": 2
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            1,
            2,
            5
          ],
          11
        ]
      },
      "expected": 3
    },
    {
      "name": "case_18_base",
      "input": {
        "args": [
          [
            2
          ],
          3
        ]
      },
      "expected": -1
    },
    {
      "name": "case_19_edge_zero_amount",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": 0
    },
    {
      "name": "case_20_edge_non_greedy",
      "input": {
        "args": [
          [
            1,
            3,
            4
          ],
          6
        ]
      },
      "expected": 2
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            1,
            2,
            5
          ],
          11
        ]
      },
      "expected": 3
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            2
          ],
          3
        ]
      },
      "expected": -1
    },
    {
      "name": "case_23_edge_zero_amount",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": 0
    },
    {
      "name": "case_24_edge_non_greedy",
      "input": {
        "args": [
          [
            1,
            3,
            4
          ],
          6
        ]
      },
      "expected": 2
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            1,
            2,
            5
          ],
          11
        ]
      },
      "expected": 3
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            2
          ],
          3
        ]
      },
      "expected": -1
    },
    {
      "name": "case_27_edge_zero_amount",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": 0
    },
    {
      "name": "case_28_edge_non_greedy",
      "input": {
        "args": [
          [
            1,
            3,
            4
          ],
          6
        ]
      },
      "expected": 2
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          [
            1,
            2,
            5
          ],
          11
        ]
      },
      "expected": 3
    },
    {
      "name": "case_30_base",
      "input": {
        "args": [
          [
            2
          ],
          3
        ]
      },
      "expected": -1
    },
    {
      "name": "case_31_edge_zero_amount",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": 0
    },
    {
      "name": "case_32_edge_non_greedy",
      "input": {
        "args": [
          [
            1,
            3,
            4
          ],
          6
        ]
      },
      "expected": 2
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          [
            1,
            2,
            5
          ],
          11
        ]
      },
      "expected": 3
    },
    {
      "name": "case_34_base",
      "input": {
        "args": [
          [
            2
          ],
          3
        ]
      },
      "expected": -1
    },
    {
      "name": "case_35_edge_zero_amount",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": 0
    },
    {
      "name": "case_36_edge_non_greedy",
      "input": {
        "args": [
          [
            1,
            3,
            4
          ],
          6
        ]
      },
      "expected": 2
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            1,
            2,
            5
          ],
          11
        ]
      },
      "expected": 3
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          [
            2
          ],
          3
        ]
      },
      "expected": -1
    },
    {
      "name": "case_39_edge_zero_amount",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": 0
    },
    {
      "name": "case_40_edge_non_greedy",
      "input": {
        "args": [
          [
            1,
            3,
            4
          ],
          6
        ]
      },
      "expected": 2
    }
  ]
}
```
