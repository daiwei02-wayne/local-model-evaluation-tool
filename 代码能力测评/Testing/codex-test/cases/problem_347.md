# 题目347 前 K 个高频元素

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个整数数组 `nums` 和一个整数 `k` ，请你返回其中出现频率前 `k` 高的元素。你可以按 任意顺序 返回答案。
示例 1:
输入: nums = [1,1,1,2,2,3], k = 2输出: [1,2]
示例 2:
输入: nums = [1], k = 1输出: [1]
提示：
1 <= nums.length <= 10<sup>5</sup>
`k` 的取值范围是 `[1, 数组中不相同的元素的个数]`
题目数据保证答案唯一，换句话说，数组中前 `k` 个高频元素的集合是唯一的
进阶：你所设计算法的时间复杂度 必须 优于 `O(n log n)` ，其中 `n`是数组大小。

```json
{
  "id": 347,
  "title": "前 K 个高频元素",
  "difficulty": "中等",
  "method": "question_347",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            1,
            1,
            1,
            2,
            2,
            3
          ],
          2
        ]
      },
      "expected": [
        1,
        2
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_02_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "comparison": "any_order",
      "expected": [
        1
      ]
    },
    {
      "name": "case_03_edge_all",
      "input": {
        "args": [
          [
            1,
            2
          ],
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_04_edge_clear_top",
      "input": {
        "args": [
          [
            4,
            4,
            4,
            6,
            6,
            7
          ],
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        4,
        6
      ]
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          [
            1,
            1,
            1,
            2,
            2,
            3
          ],
          2
        ]
      },
      "expected": [
        1,
        2
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_06_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "comparison": "any_order",
      "expected": [
        1
      ]
    },
    {
      "name": "case_07_edge_all",
      "input": {
        "args": [
          [
            1,
            2
          ],
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_08_edge_clear_top",
      "input": {
        "args": [
          [
            4,
            4,
            4,
            6,
            6,
            7
          ],
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        4,
        6
      ]
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          [
            1,
            1,
            1,
            2,
            2,
            3
          ],
          2
        ]
      },
      "expected": [
        1,
        2
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_10_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "comparison": "any_order",
      "expected": [
        1
      ]
    },
    {
      "name": "case_11_edge_all",
      "input": {
        "args": [
          [
            1,
            2
          ],
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_12_edge_clear_top",
      "input": {
        "args": [
          [
            4,
            4,
            4,
            6,
            6,
            7
          ],
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        4,
        6
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [
            1,
            1,
            1,
            2,
            2,
            3
          ],
          2
        ]
      },
      "expected": [
        1,
        2
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_14_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "comparison": "any_order",
      "expected": [
        1
      ]
    },
    {
      "name": "case_15_edge_all",
      "input": {
        "args": [
          [
            1,
            2
          ],
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_16_edge_clear_top",
      "input": {
        "args": [
          [
            4,
            4,
            4,
            6,
            6,
            7
          ],
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        4,
        6
      ]
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            1,
            1,
            1,
            2,
            2,
            3
          ],
          2
        ]
      },
      "expected": [
        1,
        2
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_18_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "comparison": "any_order",
      "expected": [
        1
      ]
    },
    {
      "name": "case_19_edge_all",
      "input": {
        "args": [
          [
            1,
            2
          ],
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_20_edge_clear_top",
      "input": {
        "args": [
          [
            4,
            4,
            4,
            6,
            6,
            7
          ],
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        4,
        6
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            1,
            1,
            1,
            2,
            2,
            3
          ],
          2
        ]
      },
      "expected": [
        1,
        2
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_22_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "comparison": "any_order",
      "expected": [
        1
      ]
    },
    {
      "name": "case_23_edge_all",
      "input": {
        "args": [
          [
            1,
            2
          ],
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_24_edge_clear_top",
      "input": {
        "args": [
          [
            4,
            4,
            4,
            6,
            6,
            7
          ],
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        4,
        6
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            1,
            1,
            1,
            2,
            2,
            3
          ],
          2
        ]
      },
      "expected": [
        1,
        2
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_26_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "comparison": "any_order",
      "expected": [
        1
      ]
    },
    {
      "name": "case_27_edge_all",
      "input": {
        "args": [
          [
            1,
            2
          ],
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_28_edge_clear_top",
      "input": {
        "args": [
          [
            4,
            4,
            4,
            6,
            6,
            7
          ],
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        4,
        6
      ]
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          [
            1,
            1,
            1,
            2,
            2,
            3
          ],
          2
        ]
      },
      "expected": [
        1,
        2
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_30_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "comparison": "any_order",
      "expected": [
        1
      ]
    },
    {
      "name": "case_31_edge_all",
      "input": {
        "args": [
          [
            1,
            2
          ],
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_32_edge_clear_top",
      "input": {
        "args": [
          [
            4,
            4,
            4,
            6,
            6,
            7
          ],
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        4,
        6
      ]
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          [
            1,
            1,
            1,
            2,
            2,
            3
          ],
          2
        ]
      },
      "expected": [
        1,
        2
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_34_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "comparison": "any_order",
      "expected": [
        1
      ]
    },
    {
      "name": "case_35_edge_all",
      "input": {
        "args": [
          [
            1,
            2
          ],
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_36_edge_clear_top",
      "input": {
        "args": [
          [
            4,
            4,
            4,
            6,
            6,
            7
          ],
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        4,
        6
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            1,
            1,
            1,
            2,
            2,
            3
          ],
          2
        ]
      },
      "expected": [
        1,
        2
      ],
      "comparison": "any_order"
    },
    {
      "name": "case_38_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "comparison": "any_order",
      "expected": [
        1
      ]
    },
    {
      "name": "case_39_edge_all",
      "input": {
        "args": [
          [
            1,
            2
          ],
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_40_edge_clear_top",
      "input": {
        "args": [
          [
            4,
            4,
            4,
            6,
            6,
            7
          ],
          2
        ]
      },
      "comparison": "any_order",
      "expected": [
        4,
        6
      ]
    }
  ]
}
```
