# 题目34 在排序数组中查找元素的第一个和最后一个位置

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个按照非递减顺序排列的整数数组 `nums`，和一个目标值 `target`。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 `target`，返回 `[-1, -1]`。
你必须设计并实现时间复杂度为 `O(log n)` 的算法解决此问题。
示例 1：
输入：nums = [5,7,7,8,8,10], target = 8输出：[3,4]
示例 2：
输入：nums = [5,7,7,8,8,10], target = 6输出：[-1,-1]
示例 3：
输入：nums = [], target = 0输出：[-1,-1]
提示：
0 <= nums.length <= 10<sup>5</sup>
-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>
`nums` 是一个非递减数组
-10<sup>9</sup> <= target <= 10<sup>9</sup>

```json
{
  "id": 34,
  "title": "在排序数组中查找元素的第一个和最后一个位置",
  "difficulty": "中等",
  "method": "question_34",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            5,
            7,
            7,
            8,
            8,
            10
          ],
          8
        ]
      },
      "expected": [
        3,
        4
      ]
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            5,
            7,
            7,
            8,
            8,
            10
          ],
          6
        ]
      },
      "expected": [
        -1,
        -1
      ]
    },
    {
      "name": "case_03_edge_single_hit",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "expected": [
        0,
        0
      ]
    },
    {
      "name": "case_04_edge_single_missing",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": [
        -1,
        -1
      ]
    },
    {
      "name": "case_05_edge_all_same",
      "input": {
        "args": [
          [
            2,
            2,
            2
          ],
          2
        ]
      },
      "expected": [
        0,
        2
      ]
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            5,
            7,
            7,
            8,
            8,
            10
          ],
          8
        ]
      },
      "expected": [
        3,
        4
      ]
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            5,
            7,
            7,
            8,
            8,
            10
          ],
          6
        ]
      },
      "expected": [
        -1,
        -1
      ]
    },
    {
      "name": "case_08_edge_single_hit",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "expected": [
        0,
        0
      ]
    },
    {
      "name": "case_09_edge_single_missing",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": [
        -1,
        -1
      ]
    },
    {
      "name": "case_10_edge_all_same",
      "input": {
        "args": [
          [
            2,
            2,
            2
          ],
          2
        ]
      },
      "expected": [
        0,
        2
      ]
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            5,
            7,
            7,
            8,
            8,
            10
          ],
          8
        ]
      },
      "expected": [
        3,
        4
      ]
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          [
            5,
            7,
            7,
            8,
            8,
            10
          ],
          6
        ]
      },
      "expected": [
        -1,
        -1
      ]
    },
    {
      "name": "case_13_edge_single_hit",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "expected": [
        0,
        0
      ]
    },
    {
      "name": "case_14_edge_single_missing",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": [
        -1,
        -1
      ]
    },
    {
      "name": "case_15_edge_all_same",
      "input": {
        "args": [
          [
            2,
            2,
            2
          ],
          2
        ]
      },
      "expected": [
        0,
        2
      ]
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            5,
            7,
            7,
            8,
            8,
            10
          ],
          8
        ]
      },
      "expected": [
        3,
        4
      ]
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            5,
            7,
            7,
            8,
            8,
            10
          ],
          6
        ]
      },
      "expected": [
        -1,
        -1
      ]
    },
    {
      "name": "case_18_edge_single_hit",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "expected": [
        0,
        0
      ]
    },
    {
      "name": "case_19_edge_single_missing",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": [
        -1,
        -1
      ]
    },
    {
      "name": "case_20_edge_all_same",
      "input": {
        "args": [
          [
            2,
            2,
            2
          ],
          2
        ]
      },
      "expected": [
        0,
        2
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            5,
            7,
            7,
            8,
            8,
            10
          ],
          8
        ]
      },
      "expected": [
        3,
        4
      ]
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            5,
            7,
            7,
            8,
            8,
            10
          ],
          6
        ]
      },
      "expected": [
        -1,
        -1
      ]
    },
    {
      "name": "case_23_edge_single_hit",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "expected": [
        0,
        0
      ]
    },
    {
      "name": "case_24_edge_single_missing",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": [
        -1,
        -1
      ]
    },
    {
      "name": "case_25_edge_all_same",
      "input": {
        "args": [
          [
            2,
            2,
            2
          ],
          2
        ]
      },
      "expected": [
        0,
        2
      ]
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            5,
            7,
            7,
            8,
            8,
            10
          ],
          8
        ]
      },
      "expected": [
        3,
        4
      ]
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          [
            5,
            7,
            7,
            8,
            8,
            10
          ],
          6
        ]
      },
      "expected": [
        -1,
        -1
      ]
    },
    {
      "name": "case_28_edge_single_hit",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "expected": [
        0,
        0
      ]
    },
    {
      "name": "case_29_edge_single_missing",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": [
        -1,
        -1
      ]
    },
    {
      "name": "case_30_edge_all_same",
      "input": {
        "args": [
          [
            2,
            2,
            2
          ],
          2
        ]
      },
      "expected": [
        0,
        2
      ]
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            5,
            7,
            7,
            8,
            8,
            10
          ],
          8
        ]
      },
      "expected": [
        3,
        4
      ]
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          [
            5,
            7,
            7,
            8,
            8,
            10
          ],
          6
        ]
      },
      "expected": [
        -1,
        -1
      ]
    },
    {
      "name": "case_33_edge_single_hit",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "expected": [
        0,
        0
      ]
    },
    {
      "name": "case_34_edge_single_missing",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": [
        -1,
        -1
      ]
    },
    {
      "name": "case_35_edge_all_same",
      "input": {
        "args": [
          [
            2,
            2,
            2
          ],
          2
        ]
      },
      "expected": [
        0,
        2
      ]
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          [
            5,
            7,
            7,
            8,
            8,
            10
          ],
          8
        ]
      },
      "expected": [
        3,
        4
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            5,
            7,
            7,
            8,
            8,
            10
          ],
          6
        ]
      },
      "expected": [
        -1,
        -1
      ]
    },
    {
      "name": "case_38_edge_single_hit",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "expected": [
        0,
        0
      ]
    },
    {
      "name": "case_39_edge_single_missing",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": [
        -1,
        -1
      ]
    },
    {
      "name": "case_40_edge_all_same",
      "input": {
        "args": [
          [
            2,
            2,
            2
          ],
          2
        ]
      },
      "expected": [
        0,
        2
      ]
    }
  ]
}
```
