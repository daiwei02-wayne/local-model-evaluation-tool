# 题目33 搜索旋转排序数组

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

整数数组 `nums` 按升序排列，数组中的值 互不相同 。
在传递给函数之前，`nums` 在预先未知的某个下标 `k`（`0 <= k < nums.length`）上进行了 旋转，使数组变为 `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`（下标 从 0 开始 计数）。例如， `[0,1,2,4,5,6,7]` 在下标 `3` 处经旋转后可能变为 `[4,5,6,7,0,1,2]` 。
给你 旋转后 的数组 `nums` 和一个整数 `target` ，如果 `nums` 中存在这个目标值 `target` ，则返回它的下标，否则返回 `-1` 。
你必须设计一个时间复杂度为 `O(log n)` 的算法解决此问题。
示例 1：
输入：nums = [4,5,6,7,0,1,2], target = 0输出：4
示例 2：
输入：nums = [4,5,6,7,0,1,2], target = 3输出：-1
示例 3：
输入：nums = [1], target = 0输出：-1
提示：
`1 <= nums.length <= 5000`
-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>
`nums` 中的每个值都 独一无二
题目数据保证 `nums` 在预先未知的某个下标上进行了旋转
-10<sup>4</sup> <= target <= 10<sup>4</sup>

```json
{
  "id": 33,
  "title": "搜索旋转排序数组",
  "difficulty": "中等",
  "method": "question_33",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ],
          0
        ]
      },
      "expected": 4
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ],
          3
        ]
      },
      "expected": -1
    },
    {
      "name": "case_03_edge_single_missing",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": -1
    },
    {
      "name": "case_04_edge_single_hit",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "expected": 0
    },
    {
      "name": "case_05_edge_two_rotated",
      "input": {
        "args": [
          [
            3,
            1
          ],
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ],
          0
        ]
      },
      "expected": 4
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ],
          3
        ]
      },
      "expected": -1
    },
    {
      "name": "case_08_edge_single_missing",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": -1
    },
    {
      "name": "case_09_edge_single_hit",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "expected": 0
    },
    {
      "name": "case_10_edge_two_rotated",
      "input": {
        "args": [
          [
            3,
            1
          ],
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ],
          0
        ]
      },
      "expected": 4
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          [
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ],
          3
        ]
      },
      "expected": -1
    },
    {
      "name": "case_13_edge_single_missing",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": -1
    },
    {
      "name": "case_14_edge_single_hit",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "expected": 0
    },
    {
      "name": "case_15_edge_two_rotated",
      "input": {
        "args": [
          [
            3,
            1
          ],
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ],
          0
        ]
      },
      "expected": 4
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ],
          3
        ]
      },
      "expected": -1
    },
    {
      "name": "case_18_edge_single_missing",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": -1
    },
    {
      "name": "case_19_edge_single_hit",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "expected": 0
    },
    {
      "name": "case_20_edge_two_rotated",
      "input": {
        "args": [
          [
            3,
            1
          ],
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ],
          0
        ]
      },
      "expected": 4
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ],
          3
        ]
      },
      "expected": -1
    },
    {
      "name": "case_23_edge_single_missing",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": -1
    },
    {
      "name": "case_24_edge_single_hit",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "expected": 0
    },
    {
      "name": "case_25_edge_two_rotated",
      "input": {
        "args": [
          [
            3,
            1
          ],
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ],
          0
        ]
      },
      "expected": 4
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          [
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ],
          3
        ]
      },
      "expected": -1
    },
    {
      "name": "case_28_edge_single_missing",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": -1
    },
    {
      "name": "case_29_edge_single_hit",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "expected": 0
    },
    {
      "name": "case_30_edge_two_rotated",
      "input": {
        "args": [
          [
            3,
            1
          ],
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ],
          0
        ]
      },
      "expected": 4
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          [
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ],
          3
        ]
      },
      "expected": -1
    },
    {
      "name": "case_33_edge_single_missing",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": -1
    },
    {
      "name": "case_34_edge_single_hit",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "expected": 0
    },
    {
      "name": "case_35_edge_two_rotated",
      "input": {
        "args": [
          [
            3,
            1
          ],
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          [
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ],
          0
        ]
      },
      "expected": 4
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            4,
            5,
            6,
            7,
            0,
            1,
            2
          ],
          3
        ]
      },
      "expected": -1
    },
    {
      "name": "case_38_edge_single_missing",
      "input": {
        "args": [
          [
            1
          ],
          0
        ]
      },
      "expected": -1
    },
    {
      "name": "case_39_edge_single_hit",
      "input": {
        "args": [
          [
            1
          ],
          1
        ]
      },
      "expected": 0
    },
    {
      "name": "case_40_edge_two_rotated",
      "input": {
        "args": [
          [
            3,
            1
          ],
          1
        ]
      },
      "expected": 1
    }
  ]
}
```
