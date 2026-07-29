# 题目31 下一个排列

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。
例如，`arr = [1,2,3]` ，以下这些都可以视作 `arr` 的排列：`[1,2,3]`、`[1,3,2]`、`[3,1,2]`、`[2,3,1]` 。
整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。
例如，`arr = [1,2,3]` 的下一个排列是 `[1,3,2]` 。
类似地，`arr = [2,3,1]` 的下一个排列是 `[3,1,2]` 。
而 `arr = [3,2,1]` 的下一个排列是 `[1,2,3]` ，因为 `[3,2,1]` 不存在一个字典序更大的排列。
给你一个整数数组 `nums` ，找出 `nums` 的下一个排列。
必须修改，只允许使用额外常数空间。
示例 1：
输入：nums = [1,2,3]输出：[1,3,2]
示例 2：
输入：nums = [3,2,1]输出：[1,2,3]
示例 3：
输入：nums = [1,1,5]输出：[1,5,1]
提示：
`1 <= nums.length <= 100`
`0 <= nums[i] <= 100`

```json
{
  "id": 31,
  "title": "下一个排列",
  "difficulty": "中等",
  "method": "question_31",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        1,
        3,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            3,
            2,
            1
          ]
        ]
      },
      "expected": [
        1,
        2,
        3
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_03_edge_duplicates",
      "input": {
        "args": [
          [
            1,
            1,
            5
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        5,
        1
      ]
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
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_05_edge_suffix_reverse",
      "input": {
        "args": [
          [
            2,
            3,
            1
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        3,
        1,
        2
      ]
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        1,
        3,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            3,
            2,
            1
          ]
        ]
      },
      "expected": [
        1,
        2,
        3
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_08_edge_duplicates",
      "input": {
        "args": [
          [
            1,
            1,
            5
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        5,
        1
      ]
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
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_10_edge_suffix_reverse",
      "input": {
        "args": [
          [
            2,
            3,
            1
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        3,
        1,
        2
      ]
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        1,
        3,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          [
            3,
            2,
            1
          ]
        ]
      },
      "expected": [
        1,
        2,
        3
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_13_edge_duplicates",
      "input": {
        "args": [
          [
            1,
            1,
            5
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        5,
        1
      ]
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
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_15_edge_suffix_reverse",
      "input": {
        "args": [
          [
            2,
            3,
            1
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        3,
        1,
        2
      ]
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        1,
        3,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            3,
            2,
            1
          ]
        ]
      },
      "expected": [
        1,
        2,
        3
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_18_edge_duplicates",
      "input": {
        "args": [
          [
            1,
            1,
            5
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        5,
        1
      ]
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
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_20_edge_suffix_reverse",
      "input": {
        "args": [
          [
            2,
            3,
            1
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        3,
        1,
        2
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        1,
        3,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            3,
            2,
            1
          ]
        ]
      },
      "expected": [
        1,
        2,
        3
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_23_edge_duplicates",
      "input": {
        "args": [
          [
            1,
            1,
            5
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        5,
        1
      ]
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
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_25_edge_suffix_reverse",
      "input": {
        "args": [
          [
            2,
            3,
            1
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        3,
        1,
        2
      ]
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        1,
        3,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          [
            3,
            2,
            1
          ]
        ]
      },
      "expected": [
        1,
        2,
        3
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_28_edge_duplicates",
      "input": {
        "args": [
          [
            1,
            1,
            5
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        5,
        1
      ]
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
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_30_edge_suffix_reverse",
      "input": {
        "args": [
          [
            2,
            3,
            1
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        3,
        1,
        2
      ]
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        1,
        3,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          [
            3,
            2,
            1
          ]
        ]
      },
      "expected": [
        1,
        2,
        3
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_33_edge_duplicates",
      "input": {
        "args": [
          [
            1,
            1,
            5
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        5,
        1
      ]
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
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_35_edge_suffix_reverse",
      "input": {
        "args": [
          [
            2,
            3,
            1
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        3,
        1,
        2
      ]
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        1,
        3,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            3,
            2,
            1
          ]
        ]
      },
      "expected": [
        1,
        2,
        3
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_38_edge_duplicates",
      "input": {
        "args": [
          [
            1,
            1,
            5
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        5,
        1
      ]
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
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_40_edge_suffix_reverse",
      "input": {
        "args": [
          [
            2,
            3,
            1
          ]
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        3,
        1,
        2
      ]
    }
  ]
}
```
