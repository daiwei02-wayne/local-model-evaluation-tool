# 题目283 移动零

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。
示例 1:
输入: nums = [0,1,0,3,12]输出: [1,3,12,0,0]
示例 2:
输入: nums = [0]输出: [0]
提示:
1 <= nums.length <= 10<sup>4</sup>
-2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1
进阶：你能尽量减少完成的操作次数吗？

```json
{
  "id": 283,
  "title": "移动零",
  "difficulty": "简单",
  "method": "question_283",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            0,
            1,
            0,
            3,
            12
          ]
        ]
      },
      "expected": [
        1,
        3,
        12,
        0,
        0
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_02_edge_many_zero_front",
      "input": {
        "args": [
          [
            0,
            0,
            1
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        0,
        0
      ]
    },
    {
      "name": "case_03_edge_zero_tail",
      "input": {
        "args": [
          [
            1,
            0,
            0
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        0,
        0
      ]
    },
    {
      "name": "case_04_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          [
            0,
            1,
            0,
            3,
            12
          ]
        ]
      },
      "expected": [
        1,
        3,
        12,
        0,
        0
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_06_edge_many_zero_front",
      "input": {
        "args": [
          [
            0,
            0,
            1
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        0,
        0
      ]
    },
    {
      "name": "case_07_edge_zero_tail",
      "input": {
        "args": [
          [
            1,
            0,
            0
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        0,
        0
      ]
    },
    {
      "name": "case_08_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          [
            0,
            1,
            0,
            3,
            12
          ]
        ]
      },
      "expected": [
        1,
        3,
        12,
        0,
        0
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_10_edge_many_zero_front",
      "input": {
        "args": [
          [
            0,
            0,
            1
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        0,
        0
      ]
    },
    {
      "name": "case_11_edge_zero_tail",
      "input": {
        "args": [
          [
            1,
            0,
            0
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        0,
        0
      ]
    },
    {
      "name": "case_12_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [
            0,
            1,
            0,
            3,
            12
          ]
        ]
      },
      "expected": [
        1,
        3,
        12,
        0,
        0
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_14_edge_many_zero_front",
      "input": {
        "args": [
          [
            0,
            0,
            1
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        0,
        0
      ]
    },
    {
      "name": "case_15_edge_zero_tail",
      "input": {
        "args": [
          [
            1,
            0,
            0
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        0,
        0
      ]
    },
    {
      "name": "case_16_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            0,
            1,
            0,
            3,
            12
          ]
        ]
      },
      "expected": [
        1,
        3,
        12,
        0,
        0
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_18_edge_many_zero_front",
      "input": {
        "args": [
          [
            0,
            0,
            1
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        0,
        0
      ]
    },
    {
      "name": "case_19_edge_zero_tail",
      "input": {
        "args": [
          [
            1,
            0,
            0
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        0,
        0
      ]
    },
    {
      "name": "case_20_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            0,
            1,
            0,
            3,
            12
          ]
        ]
      },
      "expected": [
        1,
        3,
        12,
        0,
        0
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_22_edge_many_zero_front",
      "input": {
        "args": [
          [
            0,
            0,
            1
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        0,
        0
      ]
    },
    {
      "name": "case_23_edge_zero_tail",
      "input": {
        "args": [
          [
            1,
            0,
            0
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        0,
        0
      ]
    },
    {
      "name": "case_24_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            0,
            1,
            0,
            3,
            12
          ]
        ]
      },
      "expected": [
        1,
        3,
        12,
        0,
        0
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_26_edge_many_zero_front",
      "input": {
        "args": [
          [
            0,
            0,
            1
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        0,
        0
      ]
    },
    {
      "name": "case_27_edge_zero_tail",
      "input": {
        "args": [
          [
            1,
            0,
            0
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        0,
        0
      ]
    },
    {
      "name": "case_28_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          [
            0,
            1,
            0,
            3,
            12
          ]
        ]
      },
      "expected": [
        1,
        3,
        12,
        0,
        0
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_30_edge_many_zero_front",
      "input": {
        "args": [
          [
            0,
            0,
            1
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        0,
        0
      ]
    },
    {
      "name": "case_31_edge_zero_tail",
      "input": {
        "args": [
          [
            1,
            0,
            0
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        0,
        0
      ]
    },
    {
      "name": "case_32_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          [
            0,
            1,
            0,
            3,
            12
          ]
        ]
      },
      "expected": [
        1,
        3,
        12,
        0,
        0
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_34_edge_many_zero_front",
      "input": {
        "args": [
          [
            0,
            0,
            1
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        0,
        0
      ]
    },
    {
      "name": "case_35_edge_zero_tail",
      "input": {
        "args": [
          [
            1,
            0,
            0
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        0,
        0
      ]
    },
    {
      "name": "case_36_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        0
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            0,
            1,
            0,
            3,
            12
          ]
        ]
      },
      "expected": [
        1,
        3,
        12,
        0,
        0
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_38_edge_many_zero_front",
      "input": {
        "args": [
          [
            0,
            0,
            1
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        0,
        0
      ]
    },
    {
      "name": "case_39_edge_zero_tail",
      "input": {
        "args": [
          [
            1,
            0,
            0
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        0,
        0
      ]
    },
    {
      "name": "case_40_edge_single_zero",
      "input": {
        "args": [
          [
            0
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        0
      ]
    }
  ]
}
```
