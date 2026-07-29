# 题目4 寻找两个正序数组的中位数

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定两个大小分别为 `m` 和 `n` 的正序（从小到大）数组 `nums1` 和 `nums2`。请你找出并返回这两个正序数组的 中位数 。
算法的时间复杂度应该为 `O(log (m+n))` 。
示例 1：
输入：nums1 = [1,3], nums2 = [2]输出：2.00000解释：合并数组 = [1,2,3] ，中位数 2
示例 2：
输入：nums1 = [1,2], nums2 = [3,4]输出：2.50000解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
提示：
`nums1.length == m`
`nums2.length == n`
`0 <= m <= 1000`
`0 <= n <= 1000`
`1 <= m + n <= 2000`
-10<sup>6</sup> <= nums1[i], nums2[i] <= 10<sup>6</sup>

```json
{
  "id": 4,
  "title": "寻找两个正序数组的中位数",
  "difficulty": "困难",
  "method": "question_4",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            1,
            3
          ],
          [
            2
          ]
        ]
      },
      "expected": 2.0
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            3,
            4
          ]
        ]
      },
      "expected": 2.5
    },
    {
      "name": "case_03_base",
      "input": {
        "args": [
          [],
          [
            1
          ]
        ]
      },
      "expected": 1.0
    },
    {
      "name": "case_04_edge_all_zero_even",
      "input": {
        "args": [
          [
            0,
            0
          ],
          [
            0,
            0
          ]
        ]
      },
      "expected": 0.0
    },
    {
      "name": "case_05_edge_negatives",
      "input": {
        "args": [
          [
            -5,
            3,
            6
          ],
          [
            -2,
            -1,
            4
          ]
        ]
      },
      "expected": 1.0
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            1,
            3
          ],
          [
            2
          ]
        ]
      },
      "expected": 2.0
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            3,
            4
          ]
        ]
      },
      "expected": 2.5
    },
    {
      "name": "case_08_base",
      "input": {
        "args": [
          [],
          [
            1
          ]
        ]
      },
      "expected": 1.0
    },
    {
      "name": "case_09_edge_all_zero_even",
      "input": {
        "args": [
          [
            0,
            0
          ],
          [
            0,
            0
          ]
        ]
      },
      "expected": 0.0
    },
    {
      "name": "case_10_edge_negatives",
      "input": {
        "args": [
          [
            -5,
            3,
            6
          ],
          [
            -2,
            -1,
            4
          ]
        ]
      },
      "expected": 1.0
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            1,
            3
          ],
          [
            2
          ]
        ]
      },
      "expected": 2.0
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            3,
            4
          ]
        ]
      },
      "expected": 2.5
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [],
          [
            1
          ]
        ]
      },
      "expected": 1.0
    },
    {
      "name": "case_14_edge_all_zero_even",
      "input": {
        "args": [
          [
            0,
            0
          ],
          [
            0,
            0
          ]
        ]
      },
      "expected": 0.0
    },
    {
      "name": "case_15_edge_negatives",
      "input": {
        "args": [
          [
            -5,
            3,
            6
          ],
          [
            -2,
            -1,
            4
          ]
        ]
      },
      "expected": 1.0
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            1,
            3
          ],
          [
            2
          ]
        ]
      },
      "expected": 2.0
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            3,
            4
          ]
        ]
      },
      "expected": 2.5
    },
    {
      "name": "case_18_base",
      "input": {
        "args": [
          [],
          [
            1
          ]
        ]
      },
      "expected": 1.0
    },
    {
      "name": "case_19_edge_all_zero_even",
      "input": {
        "args": [
          [
            0,
            0
          ],
          [
            0,
            0
          ]
        ]
      },
      "expected": 0.0
    },
    {
      "name": "case_20_edge_negatives",
      "input": {
        "args": [
          [
            -5,
            3,
            6
          ],
          [
            -2,
            -1,
            4
          ]
        ]
      },
      "expected": 1.0
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            1,
            3
          ],
          [
            2
          ]
        ]
      },
      "expected": 2.0
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            3,
            4
          ]
        ]
      },
      "expected": 2.5
    },
    {
      "name": "case_23_base",
      "input": {
        "args": [
          [],
          [
            1
          ]
        ]
      },
      "expected": 1.0
    },
    {
      "name": "case_24_edge_all_zero_even",
      "input": {
        "args": [
          [
            0,
            0
          ],
          [
            0,
            0
          ]
        ]
      },
      "expected": 0.0
    },
    {
      "name": "case_25_edge_negatives",
      "input": {
        "args": [
          [
            -5,
            3,
            6
          ],
          [
            -2,
            -1,
            4
          ]
        ]
      },
      "expected": 1.0
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            1,
            3
          ],
          [
            2
          ]
        ]
      },
      "expected": 2.0
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            3,
            4
          ]
        ]
      },
      "expected": 2.5
    },
    {
      "name": "case_28_base",
      "input": {
        "args": [
          [],
          [
            1
          ]
        ]
      },
      "expected": 1.0
    },
    {
      "name": "case_29_edge_all_zero_even",
      "input": {
        "args": [
          [
            0,
            0
          ],
          [
            0,
            0
          ]
        ]
      },
      "expected": 0.0
    },
    {
      "name": "case_30_edge_negatives",
      "input": {
        "args": [
          [
            -5,
            3,
            6
          ],
          [
            -2,
            -1,
            4
          ]
        ]
      },
      "expected": 1.0
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            1,
            3
          ],
          [
            2
          ]
        ]
      },
      "expected": 2.0
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            3,
            4
          ]
        ]
      },
      "expected": 2.5
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          [],
          [
            1
          ]
        ]
      },
      "expected": 1.0
    },
    {
      "name": "case_34_edge_all_zero_even",
      "input": {
        "args": [
          [
            0,
            0
          ],
          [
            0,
            0
          ]
        ]
      },
      "expected": 0.0
    },
    {
      "name": "case_35_edge_negatives",
      "input": {
        "args": [
          [
            -5,
            3,
            6
          ],
          [
            -2,
            -1,
            4
          ]
        ]
      },
      "expected": 1.0
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          [
            1,
            3
          ],
          [
            2
          ]
        ]
      },
      "expected": 2.0
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            3,
            4
          ]
        ]
      },
      "expected": 2.5
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          [],
          [
            1
          ]
        ]
      },
      "expected": 1.0
    },
    {
      "name": "case_39_edge_all_zero_even",
      "input": {
        "args": [
          [
            0,
            0
          ],
          [
            0,
            0
          ]
        ]
      },
      "expected": 0.0
    },
    {
      "name": "case_40_edge_negatives",
      "input": {
        "args": [
          [
            -5,
            3,
            6
          ],
          [
            -2,
            -1,
            4
          ]
        ]
      },
      "expected": 1.0
    }
  ]
}
```
