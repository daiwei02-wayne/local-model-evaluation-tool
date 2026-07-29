# 题目239 滑动窗口最大值

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个整数数组 `nums`，有一个大小为 `k`的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 `k` 个数字。滑动窗口每次只向右移动一位。
返回 _滑动窗口中的最大值_ 。
示例 1：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3输出：[3,3,5,5,6,7]解释：滑动窗口的位置                最大值---------------               -----[1  3  -1] -3  5  3  6  7       3 1 [3  -1  -3] 5  3  6  7       3 1  3 [-1  -3  5] 3  6  7       5 1  3  -1 [-3  5  3] 6  7       5 1  3  -1  -3 [5  3  6] 7       6 1  3  -1  -3  5 [3  6  7]      7
示例 2：
输入：nums = [1], k = 1输出：[1]
提示：
1 <= nums.length <= 10<sup>5</sup>
-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>
`1 <= k <= nums.length`

```json
{
  "id": 239,
  "title": "滑动窗口最大值",
  "difficulty": "困难",
  "method": "question_239",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            1,
            3,
            -1,
            -3,
            5,
            3,
            6,
            7
          ],
          3
        ]
      },
      "expected": [
        3,
        3,
        5,
        5,
        6,
        7
      ]
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_03_edge_window_all",
      "input": {
        "args": [
          [
            9,
            11
          ],
          2
        ]
      },
      "expected": [
        11
      ]
    },
    {
      "name": "case_04_edge_k_one",
      "input": {
        "args": [
          [
            4,
            -2
          ],
          1
        ]
      },
      "expected": [
        4,
        -2
      ]
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          [
            1,
            3,
            -1,
            -3,
            5,
            3,
            6,
            7
          ],
          3
        ]
      },
      "expected": [
        3,
        3,
        5,
        5,
        6,
        7
      ]
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_07_edge_window_all",
      "input": {
        "args": [
          [
            9,
            11
          ],
          2
        ]
      },
      "expected": [
        11
      ]
    },
    {
      "name": "case_08_edge_k_one",
      "input": {
        "args": [
          [
            4,
            -2
          ],
          1
        ]
      },
      "expected": [
        4,
        -2
      ]
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          [
            1,
            3,
            -1,
            -3,
            5,
            3,
            6,
            7
          ],
          3
        ]
      },
      "expected": [
        3,
        3,
        5,
        5,
        6,
        7
      ]
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_11_edge_window_all",
      "input": {
        "args": [
          [
            9,
            11
          ],
          2
        ]
      },
      "expected": [
        11
      ]
    },
    {
      "name": "case_12_edge_k_one",
      "input": {
        "args": [
          [
            4,
            -2
          ],
          1
        ]
      },
      "expected": [
        4,
        -2
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [
            1,
            3,
            -1,
            -3,
            5,
            3,
            6,
            7
          ],
          3
        ]
      },
      "expected": [
        3,
        3,
        5,
        5,
        6,
        7
      ]
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_15_edge_window_all",
      "input": {
        "args": [
          [
            9,
            11
          ],
          2
        ]
      },
      "expected": [
        11
      ]
    },
    {
      "name": "case_16_edge_k_one",
      "input": {
        "args": [
          [
            4,
            -2
          ],
          1
        ]
      },
      "expected": [
        4,
        -2
      ]
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            1,
            3,
            -1,
            -3,
            5,
            3,
            6,
            7
          ],
          3
        ]
      },
      "expected": [
        3,
        3,
        5,
        5,
        6,
        7
      ]
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_19_edge_window_all",
      "input": {
        "args": [
          [
            9,
            11
          ],
          2
        ]
      },
      "expected": [
        11
      ]
    },
    {
      "name": "case_20_edge_k_one",
      "input": {
        "args": [
          [
            4,
            -2
          ],
          1
        ]
      },
      "expected": [
        4,
        -2
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            1,
            3,
            -1,
            -3,
            5,
            3,
            6,
            7
          ],
          3
        ]
      },
      "expected": [
        3,
        3,
        5,
        5,
        6,
        7
      ]
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_23_edge_window_all",
      "input": {
        "args": [
          [
            9,
            11
          ],
          2
        ]
      },
      "expected": [
        11
      ]
    },
    {
      "name": "case_24_edge_k_one",
      "input": {
        "args": [
          [
            4,
            -2
          ],
          1
        ]
      },
      "expected": [
        4,
        -2
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            1,
            3,
            -1,
            -3,
            5,
            3,
            6,
            7
          ],
          3
        ]
      },
      "expected": [
        3,
        3,
        5,
        5,
        6,
        7
      ]
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_27_edge_window_all",
      "input": {
        "args": [
          [
            9,
            11
          ],
          2
        ]
      },
      "expected": [
        11
      ]
    },
    {
      "name": "case_28_edge_k_one",
      "input": {
        "args": [
          [
            4,
            -2
          ],
          1
        ]
      },
      "expected": [
        4,
        -2
      ]
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          [
            1,
            3,
            -1,
            -3,
            5,
            3,
            6,
            7
          ],
          3
        ]
      },
      "expected": [
        3,
        3,
        5,
        5,
        6,
        7
      ]
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_31_edge_window_all",
      "input": {
        "args": [
          [
            9,
            11
          ],
          2
        ]
      },
      "expected": [
        11
      ]
    },
    {
      "name": "case_32_edge_k_one",
      "input": {
        "args": [
          [
            4,
            -2
          ],
          1
        ]
      },
      "expected": [
        4,
        -2
      ]
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          [
            1,
            3,
            -1,
            -3,
            5,
            3,
            6,
            7
          ],
          3
        ]
      },
      "expected": [
        3,
        3,
        5,
        5,
        6,
        7
      ]
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_35_edge_window_all",
      "input": {
        "args": [
          [
            9,
            11
          ],
          2
        ]
      },
      "expected": [
        11
      ]
    },
    {
      "name": "case_36_edge_k_one",
      "input": {
        "args": [
          [
            4,
            -2
          ],
          1
        ]
      },
      "expected": [
        4,
        -2
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            1,
            3,
            -1,
            -3,
            5,
            3,
            6,
            7
          ],
          3
        ]
      },
      "expected": [
        3,
        3,
        5,
        5,
        6,
        7
      ]
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_39_edge_window_all",
      "input": {
        "args": [
          [
            9,
            11
          ],
          2
        ]
      },
      "expected": [
        11
      ]
    },
    {
      "name": "case_40_edge_k_one",
      "input": {
        "args": [
          [
            4,
            -2
          ],
          1
        ]
      },
      "expected": [
        4,
        -2
      ]
    }
  ]
}
```
