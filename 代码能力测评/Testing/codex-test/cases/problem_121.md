# 题目121 买卖股票的最佳时机

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一个数组 `prices` ，它的第 `i` 个元素 `prices[i]` 表示一支给定股票第 `i` 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 `0` 。
示例 1：
输入：[7,1,5,3,6,4]输出：5解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：
输入：prices = [7,6,4,3,1]输出：0解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
提示：
1 <= prices.length <= 10<sup>5</sup>
0 <= prices[i] <= 10<sup>4</sup>

```json
{
  "id": 121,
  "title": "买卖股票的最佳时机",
  "difficulty": "简单",
  "method": "question_121",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            7,
            1,
            5,
            3,
            6,
            4
          ]
        ]
      },
      "expected": 5
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            7,
            6,
            4,
            3,
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_03_edge_one_day",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_04_edge_no_profit_two",
      "input": {
        "args": [
          [
            2,
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_05_edge_profit_two",
      "input": {
        "args": [
          [
            1,
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            7,
            1,
            5,
            3,
            6,
            4
          ]
        ]
      },
      "expected": 5
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            7,
            6,
            4,
            3,
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_08_edge_one_day",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_09_edge_no_profit_two",
      "input": {
        "args": [
          [
            2,
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_10_edge_profit_two",
      "input": {
        "args": [
          [
            1,
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            7,
            1,
            5,
            3,
            6,
            4
          ]
        ]
      },
      "expected": 5
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          [
            7,
            6,
            4,
            3,
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_13_edge_one_day",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_14_edge_no_profit_two",
      "input": {
        "args": [
          [
            2,
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_15_edge_profit_two",
      "input": {
        "args": [
          [
            1,
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            7,
            1,
            5,
            3,
            6,
            4
          ]
        ]
      },
      "expected": 5
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            7,
            6,
            4,
            3,
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_18_edge_one_day",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_19_edge_no_profit_two",
      "input": {
        "args": [
          [
            2,
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_20_edge_profit_two",
      "input": {
        "args": [
          [
            1,
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            7,
            1,
            5,
            3,
            6,
            4
          ]
        ]
      },
      "expected": 5
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            7,
            6,
            4,
            3,
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_23_edge_one_day",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_24_edge_no_profit_two",
      "input": {
        "args": [
          [
            2,
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_25_edge_profit_two",
      "input": {
        "args": [
          [
            1,
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            7,
            1,
            5,
            3,
            6,
            4
          ]
        ]
      },
      "expected": 5
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          [
            7,
            6,
            4,
            3,
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_28_edge_one_day",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_29_edge_no_profit_two",
      "input": {
        "args": [
          [
            2,
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_30_edge_profit_two",
      "input": {
        "args": [
          [
            1,
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            7,
            1,
            5,
            3,
            6,
            4
          ]
        ]
      },
      "expected": 5
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          [
            7,
            6,
            4,
            3,
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_33_edge_one_day",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_34_edge_no_profit_two",
      "input": {
        "args": [
          [
            2,
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_35_edge_profit_two",
      "input": {
        "args": [
          [
            1,
            2
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          [
            7,
            1,
            5,
            3,
            6,
            4
          ]
        ]
      },
      "expected": 5
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            7,
            6,
            4,
            3,
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_38_edge_one_day",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_39_edge_no_profit_two",
      "input": {
        "args": [
          [
            2,
            1
          ]
        ]
      },
      "expected": 0
    },
    {
      "name": "case_40_edge_profit_two",
      "input": {
        "args": [
          [
            1,
            2
          ]
        ]
      },
      "expected": 1
    }
  ]
}
```
