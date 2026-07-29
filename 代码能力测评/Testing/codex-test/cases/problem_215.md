# 题目215 数组中的第K个最大元素

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定整数数组 `nums` 和整数 `k`，请返回数组中第 `k` 个最大的元素。
请注意，你需要找的是数组排序后的第 `k` 个最大的元素，而不是第 `k` 个不同的元素。
你必须设计并实现时间复杂度为 `O(n)` 的算法解决此问题。
示例 1:
输入: [3,2,1,5,6,4], k = 2输出: 5
示例 2:
输入: [3,2,3,1,2,4,5,5,6], k = 4输出: 4
提示：
1 <= k <= nums.length <= 10<sup>5</sup>
-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>

```json
{
  "id": 215,
  "title": "数组中的第K个最大元素",
  "difficulty": "中等",
  "method": "question_215",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            3,
            2,
            1,
            5,
            6,
            4
          ],
          2
        ]
      },
      "expected": 5
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            3,
            2,
            3,
            1,
            2,
            4,
            5,
            5,
            6
          ],
          4
        ]
      },
      "expected": 4
    },
    {
      "name": "case_03_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_04_edge_k_last",
      "input": {
        "args": [
          [
            2,
            1
          ],
          2
        ]
      },
      "expected": 1
    },
    {
      "name": "case_05_edge_duplicates",
      "input": {
        "args": [
          [
            3,
            3,
            3,
            1
          ],
          2
        ]
      },
      "expected": 3
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            3,
            2,
            1,
            5,
            6,
            4
          ],
          2
        ]
      },
      "expected": 5
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            3,
            2,
            3,
            1,
            2,
            4,
            5,
            5,
            6
          ],
          4
        ]
      },
      "expected": 4
    },
    {
      "name": "case_08_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_09_edge_k_last",
      "input": {
        "args": [
          [
            2,
            1
          ],
          2
        ]
      },
      "expected": 1
    },
    {
      "name": "case_10_edge_duplicates",
      "input": {
        "args": [
          [
            3,
            3,
            3,
            1
          ],
          2
        ]
      },
      "expected": 3
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            3,
            2,
            1,
            5,
            6,
            4
          ],
          2
        ]
      },
      "expected": 5
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          [
            3,
            2,
            3,
            1,
            2,
            4,
            5,
            5,
            6
          ],
          4
        ]
      },
      "expected": 4
    },
    {
      "name": "case_13_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_14_edge_k_last",
      "input": {
        "args": [
          [
            2,
            1
          ],
          2
        ]
      },
      "expected": 1
    },
    {
      "name": "case_15_edge_duplicates",
      "input": {
        "args": [
          [
            3,
            3,
            3,
            1
          ],
          2
        ]
      },
      "expected": 3
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            3,
            2,
            1,
            5,
            6,
            4
          ],
          2
        ]
      },
      "expected": 5
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            3,
            2,
            3,
            1,
            2,
            4,
            5,
            5,
            6
          ],
          4
        ]
      },
      "expected": 4
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
      "expected": 1
    },
    {
      "name": "case_19_edge_k_last",
      "input": {
        "args": [
          [
            2,
            1
          ],
          2
        ]
      },
      "expected": 1
    },
    {
      "name": "case_20_edge_duplicates",
      "input": {
        "args": [
          [
            3,
            3,
            3,
            1
          ],
          2
        ]
      },
      "expected": 3
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            3,
            2,
            1,
            5,
            6,
            4
          ],
          2
        ]
      },
      "expected": 5
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            3,
            2,
            3,
            1,
            2,
            4,
            5,
            5,
            6
          ],
          4
        ]
      },
      "expected": 4
    },
    {
      "name": "case_23_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_24_edge_k_last",
      "input": {
        "args": [
          [
            2,
            1
          ],
          2
        ]
      },
      "expected": 1
    },
    {
      "name": "case_25_edge_duplicates",
      "input": {
        "args": [
          [
            3,
            3,
            3,
            1
          ],
          2
        ]
      },
      "expected": 3
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            3,
            2,
            1,
            5,
            6,
            4
          ],
          2
        ]
      },
      "expected": 5
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          [
            3,
            2,
            3,
            1,
            2,
            4,
            5,
            5,
            6
          ],
          4
        ]
      },
      "expected": 4
    },
    {
      "name": "case_28_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_29_edge_k_last",
      "input": {
        "args": [
          [
            2,
            1
          ],
          2
        ]
      },
      "expected": 1
    },
    {
      "name": "case_30_edge_duplicates",
      "input": {
        "args": [
          [
            3,
            3,
            3,
            1
          ],
          2
        ]
      },
      "expected": 3
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            3,
            2,
            1,
            5,
            6,
            4
          ],
          2
        ]
      },
      "expected": 5
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          [
            3,
            2,
            3,
            1,
            2,
            4,
            5,
            5,
            6
          ],
          4
        ]
      },
      "expected": 4
    },
    {
      "name": "case_33_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_34_edge_k_last",
      "input": {
        "args": [
          [
            2,
            1
          ],
          2
        ]
      },
      "expected": 1
    },
    {
      "name": "case_35_edge_duplicates",
      "input": {
        "args": [
          [
            3,
            3,
            3,
            1
          ],
          2
        ]
      },
      "expected": 3
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          [
            3,
            2,
            1,
            5,
            6,
            4
          ],
          2
        ]
      },
      "expected": 5
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            3,
            2,
            3,
            1,
            2,
            4,
            5,
            5,
            6
          ],
          4
        ]
      },
      "expected": 4
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
      "expected": 1
    },
    {
      "name": "case_39_edge_k_last",
      "input": {
        "args": [
          [
            2,
            1
          ],
          2
        ]
      },
      "expected": 1
    },
    {
      "name": "case_40_edge_duplicates",
      "input": {
        "args": [
          [
            3,
            3,
            3,
            1
          ],
          2
        ]
      },
      "expected": 3
    }
  ]
}
```
