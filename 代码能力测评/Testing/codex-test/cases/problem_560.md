# 题目560 和为 K 的子数组

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个整数数组 `nums` 和一个整数 `k` ，请你统计并返回 _该数组中和为 `k`的连续子数组的个数 _。
示例 1：
输入：nums = [1,1,1], k = 2输出：2
示例 2：
输入：nums = [1,2,3], k = 3输出：2
提示：
1 <= nums.length <= 2 * 10<sup>4</sup>
`-1000 <= nums[i] <= 1000`
-10<sup>7</sup> <= k <= 10<sup>7</sup>

```json
{
  "id": 560,
  "title": "和为 K 的子数组",
  "difficulty": "中等",
  "method": "question_560",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            1,
            1,
            1
          ],
          2
        ]
      },
      "expected": 2
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ],
          3
        ]
      },
      "expected": 2
    },
    {
      "name": "case_03_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ],
          0
        ]
      },
      "expected": 1
    },
    {
      "name": "case_04_edge_many_zero_subarrays",
      "input": {
        "args": [
          [
            0,
            0
          ],
          0
        ]
      },
      "expected": 3
    },
    {
      "name": "case_05_edge_negative",
      "input": {
        "args": [
          [
            -1,
            -1,
            1
          ],
          0
        ]
      },
      "expected": 1
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            1,
            1,
            1
          ],
          2
        ]
      },
      "expected": 2
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ],
          3
        ]
      },
      "expected": 2
    },
    {
      "name": "case_08_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ],
          0
        ]
      },
      "expected": 1
    },
    {
      "name": "case_09_edge_many_zero_subarrays",
      "input": {
        "args": [
          [
            0,
            0
          ],
          0
        ]
      },
      "expected": 3
    },
    {
      "name": "case_10_edge_negative",
      "input": {
        "args": [
          [
            -1,
            -1,
            1
          ],
          0
        ]
      },
      "expected": 1
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            1,
            1,
            1
          ],
          2
        ]
      },
      "expected": 2
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ],
          3
        ]
      },
      "expected": 2
    },
    {
      "name": "case_13_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ],
          0
        ]
      },
      "expected": 1
    },
    {
      "name": "case_14_edge_many_zero_subarrays",
      "input": {
        "args": [
          [
            0,
            0
          ],
          0
        ]
      },
      "expected": 3
    },
    {
      "name": "case_15_edge_negative",
      "input": {
        "args": [
          [
            -1,
            -1,
            1
          ],
          0
        ]
      },
      "expected": 1
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            1,
            1,
            1
          ],
          2
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
            3
          ],
          3
        ]
      },
      "expected": 2
    },
    {
      "name": "case_18_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ],
          0
        ]
      },
      "expected": 1
    },
    {
      "name": "case_19_edge_many_zero_subarrays",
      "input": {
        "args": [
          [
            0,
            0
          ],
          0
        ]
      },
      "expected": 3
    },
    {
      "name": "case_20_edge_negative",
      "input": {
        "args": [
          [
            -1,
            -1,
            1
          ],
          0
        ]
      },
      "expected": 1
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            1,
            1,
            1
          ],
          2
        ]
      },
      "expected": 2
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ],
          3
        ]
      },
      "expected": 2
    },
    {
      "name": "case_23_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ],
          0
        ]
      },
      "expected": 1
    },
    {
      "name": "case_24_edge_many_zero_subarrays",
      "input": {
        "args": [
          [
            0,
            0
          ],
          0
        ]
      },
      "expected": 3
    },
    {
      "name": "case_25_edge_negative",
      "input": {
        "args": [
          [
            -1,
            -1,
            1
          ],
          0
        ]
      },
      "expected": 1
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            1,
            1,
            1
          ],
          2
        ]
      },
      "expected": 2
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ],
          3
        ]
      },
      "expected": 2
    },
    {
      "name": "case_28_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ],
          0
        ]
      },
      "expected": 1
    },
    {
      "name": "case_29_edge_many_zero_subarrays",
      "input": {
        "args": [
          [
            0,
            0
          ],
          0
        ]
      },
      "expected": 3
    },
    {
      "name": "case_30_edge_negative",
      "input": {
        "args": [
          [
            -1,
            -1,
            1
          ],
          0
        ]
      },
      "expected": 1
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            1,
            1,
            1
          ],
          2
        ]
      },
      "expected": 2
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ],
          3
        ]
      },
      "expected": 2
    },
    {
      "name": "case_33_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ],
          0
        ]
      },
      "expected": 1
    },
    {
      "name": "case_34_edge_many_zero_subarrays",
      "input": {
        "args": [
          [
            0,
            0
          ],
          0
        ]
      },
      "expected": 3
    },
    {
      "name": "case_35_edge_negative",
      "input": {
        "args": [
          [
            -1,
            -1,
            1
          ],
          0
        ]
      },
      "expected": 1
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          [
            1,
            1,
            1
          ],
          2
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
            3
          ],
          3
        ]
      },
      "expected": 2
    },
    {
      "name": "case_38_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ],
          0
        ]
      },
      "expected": 1
    },
    {
      "name": "case_39_edge_many_zero_subarrays",
      "input": {
        "args": [
          [
            0,
            0
          ],
          0
        ]
      },
      "expected": 3
    },
    {
      "name": "case_40_edge_negative",
      "input": {
        "args": [
          [
            -1,
            -1,
            1
          ],
          0
        ]
      },
      "expected": 1
    }
  ]
}
```
