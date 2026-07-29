# 题目128 最长连续序列

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一个未排序的整数数组 `nums` ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 `O(n)`的算法解决此问题。
示例 1：
输入：nums = [100,4,200,1,3,2]输出：4解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]输出：9
提示：
0 <= nums.length <= 10<sup>5</sup>
-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>

```json
{
  "id": 128,
  "title": "最长连续序列",
  "difficulty": "中等",
  "method": "question_128",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            100,
            4,
            200,
            1,
            3,
            2
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            0,
            3,
            7,
            2,
            5,
            8,
            4,
            6,
            0,
            1
          ]
        ]
      },
      "expected": 9
    },
    {
      "name": "case_03_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
    },
    {
      "name": "case_04_edge_single",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_05_edge_duplicates",
      "input": {
        "args": [
          [
            1,
            2,
            0,
            1
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            100,
            4,
            200,
            1,
            3,
            2
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            0,
            3,
            7,
            2,
            5,
            8,
            4,
            6,
            0,
            1
          ]
        ]
      },
      "expected": 9
    },
    {
      "name": "case_08_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
    },
    {
      "name": "case_09_edge_single",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_10_edge_duplicates",
      "input": {
        "args": [
          [
            1,
            2,
            0,
            1
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            100,
            4,
            200,
            1,
            3,
            2
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          [
            0,
            3,
            7,
            2,
            5,
            8,
            4,
            6,
            0,
            1
          ]
        ]
      },
      "expected": 9
    },
    {
      "name": "case_13_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
    },
    {
      "name": "case_14_edge_single",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_15_edge_duplicates",
      "input": {
        "args": [
          [
            1,
            2,
            0,
            1
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            100,
            4,
            200,
            1,
            3,
            2
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            0,
            3,
            7,
            2,
            5,
            8,
            4,
            6,
            0,
            1
          ]
        ]
      },
      "expected": 9
    },
    {
      "name": "case_18_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
    },
    {
      "name": "case_19_edge_single",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_20_edge_duplicates",
      "input": {
        "args": [
          [
            1,
            2,
            0,
            1
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            100,
            4,
            200,
            1,
            3,
            2
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            0,
            3,
            7,
            2,
            5,
            8,
            4,
            6,
            0,
            1
          ]
        ]
      },
      "expected": 9
    },
    {
      "name": "case_23_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
    },
    {
      "name": "case_24_edge_single",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_25_edge_duplicates",
      "input": {
        "args": [
          [
            1,
            2,
            0,
            1
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            100,
            4,
            200,
            1,
            3,
            2
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          [
            0,
            3,
            7,
            2,
            5,
            8,
            4,
            6,
            0,
            1
          ]
        ]
      },
      "expected": 9
    },
    {
      "name": "case_28_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
    },
    {
      "name": "case_29_edge_single",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_30_edge_duplicates",
      "input": {
        "args": [
          [
            1,
            2,
            0,
            1
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            100,
            4,
            200,
            1,
            3,
            2
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          [
            0,
            3,
            7,
            2,
            5,
            8,
            4,
            6,
            0,
            1
          ]
        ]
      },
      "expected": 9
    },
    {
      "name": "case_33_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
    },
    {
      "name": "case_34_edge_single",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_35_edge_duplicates",
      "input": {
        "args": [
          [
            1,
            2,
            0,
            1
          ]
        ]
      },
      "expected": 3
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          [
            100,
            4,
            200,
            1,
            3,
            2
          ]
        ]
      },
      "expected": 4
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            0,
            3,
            7,
            2,
            5,
            8,
            4,
            6,
            0,
            1
          ]
        ]
      },
      "expected": 9
    },
    {
      "name": "case_38_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": 0
    },
    {
      "name": "case_39_edge_single",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": 1
    },
    {
      "name": "case_40_edge_duplicates",
      "input": {
        "args": [
          [
            1,
            2,
            0,
            1
          ]
        ]
      },
      "expected": 3
    }
  ]
}
```
