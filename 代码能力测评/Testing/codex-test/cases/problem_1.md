# 题目1 两数之和

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 和为目标值 _`target`_  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
示例 1：
输入：nums = [2,7,11,15], target = 9输出：[0,1]解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：
输入：nums = [3,2,4], target = 6输出：[1,2]
示例 3：
输入：nums = [3,3], target = 6输出：[0,1]
提示：
2 <= nums.length <= 10<sup>4</sup>
-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>
-10<sup>9</sup> <= target <= 10<sup>9</sup>
只会存在一个有效答案
进阶：你可以想出一个时间复杂度小于 O(n<sup>2</sup>) 的算法吗？

```json
{
  "id": 1,
  "title": "两数之和",
  "difficulty": "简单",
  "method": "question_1",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            2,
            7,
            11,
            15
          ],
          9
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            3,
            2,
            4
          ],
          6
        ]
      },
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_03_base",
      "input": {
        "args": [
          [
            3,
            3
          ],
          6
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_04_edge_zero_pair",
      "input": {
        "args": [
          [
            0,
            4,
            3,
            0
          ],
          0
        ]
      },
      "expected": [
        0,
        3
      ]
    },
    {
      "name": "case_05_edge_negative_pair",
      "input": {
        "args": [
          [
            -3,
            4,
            3,
            90
          ],
          0
        ]
      },
      "expected": [
        0,
        2
      ]
    },
    {
      "name": "case_06_edge_large_opposites",
      "input": {
        "args": [
          [
            1000000000,
            -1000000000,
            7
          ],
          0
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            2,
            7,
            11,
            15
          ],
          9
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_08_base",
      "input": {
        "args": [
          [
            3,
            2,
            4
          ],
          6
        ]
      },
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          [
            3,
            3
          ],
          6
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_10_edge_zero_pair",
      "input": {
        "args": [
          [
            0,
            4,
            3,
            0
          ],
          0
        ]
      },
      "expected": [
        0,
        3
      ]
    },
    {
      "name": "case_11_edge_negative_pair",
      "input": {
        "args": [
          [
            -3,
            4,
            3,
            90
          ],
          0
        ]
      },
      "expected": [
        0,
        2
      ]
    },
    {
      "name": "case_12_edge_large_opposites",
      "input": {
        "args": [
          [
            1000000000,
            -1000000000,
            7
          ],
          0
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [
            2,
            7,
            11,
            15
          ],
          9
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_14_base",
      "input": {
        "args": [
          [
            3,
            2,
            4
          ],
          6
        ]
      },
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_15_base",
      "input": {
        "args": [
          [
            3,
            3
          ],
          6
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_16_edge_zero_pair",
      "input": {
        "args": [
          [
            0,
            4,
            3,
            0
          ],
          0
        ]
      },
      "expected": [
        0,
        3
      ]
    },
    {
      "name": "case_17_edge_negative_pair",
      "input": {
        "args": [
          [
            -3,
            4,
            3,
            90
          ],
          0
        ]
      },
      "expected": [
        0,
        2
      ]
    },
    {
      "name": "case_18_edge_large_opposites",
      "input": {
        "args": [
          [
            1000000000,
            -1000000000,
            7
          ],
          0
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_19_base",
      "input": {
        "args": [
          [
            2,
            7,
            11,
            15
          ],
          9
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_20_base",
      "input": {
        "args": [
          [
            3,
            2,
            4
          ],
          6
        ]
      },
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            3,
            3
          ],
          6
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_22_edge_zero_pair",
      "input": {
        "args": [
          [
            0,
            4,
            3,
            0
          ],
          0
        ]
      },
      "expected": [
        0,
        3
      ]
    },
    {
      "name": "case_23_edge_negative_pair",
      "input": {
        "args": [
          [
            -3,
            4,
            3,
            90
          ],
          0
        ]
      },
      "expected": [
        0,
        2
      ]
    },
    {
      "name": "case_24_edge_large_opposites",
      "input": {
        "args": [
          [
            1000000000,
            -1000000000,
            7
          ],
          0
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            2,
            7,
            11,
            15
          ],
          9
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            3,
            2,
            4
          ],
          6
        ]
      },
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          [
            3,
            3
          ],
          6
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_28_edge_zero_pair",
      "input": {
        "args": [
          [
            0,
            4,
            3,
            0
          ],
          0
        ]
      },
      "expected": [
        0,
        3
      ]
    },
    {
      "name": "case_29_edge_negative_pair",
      "input": {
        "args": [
          [
            -3,
            4,
            3,
            90
          ],
          0
        ]
      },
      "expected": [
        0,
        2
      ]
    },
    {
      "name": "case_30_edge_large_opposites",
      "input": {
        "args": [
          [
            1000000000,
            -1000000000,
            7
          ],
          0
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            2,
            7,
            11,
            15
          ],
          9
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          [
            3,
            2,
            4
          ],
          6
        ]
      },
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          [
            3,
            3
          ],
          6
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_34_edge_zero_pair",
      "input": {
        "args": [
          [
            0,
            4,
            3,
            0
          ],
          0
        ]
      },
      "expected": [
        0,
        3
      ]
    },
    {
      "name": "case_35_edge_negative_pair",
      "input": {
        "args": [
          [
            -3,
            4,
            3,
            90
          ],
          0
        ]
      },
      "expected": [
        0,
        2
      ]
    },
    {
      "name": "case_36_edge_large_opposites",
      "input": {
        "args": [
          [
            1000000000,
            -1000000000,
            7
          ],
          0
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            2,
            7,
            11,
            15
          ],
          9
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          [
            3,
            2,
            4
          ],
          6
        ]
      },
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_39_base",
      "input": {
        "args": [
          [
            3,
            3
          ],
          6
        ]
      },
      "expected": [
        0,
        1
      ]
    },
    {
      "name": "case_40_edge_zero_pair",
      "input": {
        "args": [
          [
            0,
            4,
            3,
            0
          ],
          0
        ]
      },
      "expected": [
        0,
        3
      ]
    }
  ]
}
```
