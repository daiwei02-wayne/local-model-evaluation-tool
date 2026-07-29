# 题目75 颜色分类

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一个包含红色、白色和蓝色、共 `n`个元素的数组 `nums` ，对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
我们使用整数 `0`、 `1` 和 `2` 分别表示红色、白色和蓝色。
必须在不使用库的sort函数的情况下解决这个问题。
示例 1：
输入：nums = [2,0,2,1,1,0]输出：[0,0,1,1,2,2]
示例 2：
输入：nums = [2,0,1]输出：[0,1,2]
提示：
`n == nums.length`
`1 <= n <= 300`
`nums[i]` 为 `0`、`1` 或 `2`
进阶：
你可以不使用代码库中的排序函数来解决这道题吗？
你能想出一个仅使用常数空间的一趟扫描算法吗？

```json
{
  "id": 75,
  "title": "颜色分类",
  "difficulty": "中等",
  "method": "question_75",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            2,
            0,
            2,
            1,
            1,
            0
          ]
        ]
      },
      "expected": [
        0,
        0,
        1,
        1,
        2,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_02_edge_single",
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
      "name": "case_03_edge_blocks",
      "input": {
        "args": [
          [
            2,
            2,
            1,
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
        0,
        0,
        1,
        1,
        2,
        2
      ]
    },
    {
      "name": "case_04_base",
      "input": {
        "args": [
          [
            2,
            0,
            2,
            1,
            1,
            0
          ]
        ]
      },
      "expected": [
        0,
        0,
        1,
        1,
        2,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_05_edge_single",
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
      "name": "case_06_edge_blocks",
      "input": {
        "args": [
          [
            2,
            2,
            1,
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
        0,
        0,
        1,
        1,
        2,
        2
      ]
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            2,
            0,
            2,
            1,
            1,
            0
          ]
        ]
      },
      "expected": [
        0,
        0,
        1,
        1,
        2,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_08_edge_single",
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
      "name": "case_09_edge_blocks",
      "input": {
        "args": [
          [
            2,
            2,
            1,
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
        0,
        0,
        1,
        1,
        2,
        2
      ]
    },
    {
      "name": "case_10_base",
      "input": {
        "args": [
          [
            2,
            0,
            2,
            1,
            1,
            0
          ]
        ]
      },
      "expected": [
        0,
        0,
        1,
        1,
        2,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_11_edge_single",
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
      "name": "case_12_edge_blocks",
      "input": {
        "args": [
          [
            2,
            2,
            1,
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
        0,
        0,
        1,
        1,
        2,
        2
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [
            2,
            0,
            2,
            1,
            1,
            0
          ]
        ]
      },
      "expected": [
        0,
        0,
        1,
        1,
        2,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_14_edge_single",
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
      "name": "case_15_edge_blocks",
      "input": {
        "args": [
          [
            2,
            2,
            1,
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
        0,
        0,
        1,
        1,
        2,
        2
      ]
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            2,
            0,
            2,
            1,
            1,
            0
          ]
        ]
      },
      "expected": [
        0,
        0,
        1,
        1,
        2,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_17_edge_single",
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
      "name": "case_18_edge_blocks",
      "input": {
        "args": [
          [
            2,
            2,
            1,
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
        0,
        0,
        1,
        1,
        2,
        2
      ]
    },
    {
      "name": "case_19_base",
      "input": {
        "args": [
          [
            2,
            0,
            2,
            1,
            1,
            0
          ]
        ]
      },
      "expected": [
        0,
        0,
        1,
        1,
        2,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_20_edge_single",
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
      "name": "case_21_edge_blocks",
      "input": {
        "args": [
          [
            2,
            2,
            1,
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
        0,
        0,
        1,
        1,
        2,
        2
      ]
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            2,
            0,
            2,
            1,
            1,
            0
          ]
        ]
      },
      "expected": [
        0,
        0,
        1,
        1,
        2,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_23_edge_single",
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
      "name": "case_24_edge_blocks",
      "input": {
        "args": [
          [
            2,
            2,
            1,
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
        0,
        0,
        1,
        1,
        2,
        2
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            2,
            0,
            2,
            1,
            1,
            0
          ]
        ]
      },
      "expected": [
        0,
        0,
        1,
        1,
        2,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_26_edge_single",
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
      "name": "case_27_edge_blocks",
      "input": {
        "args": [
          [
            2,
            2,
            1,
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
        0,
        0,
        1,
        1,
        2,
        2
      ]
    },
    {
      "name": "case_28_base",
      "input": {
        "args": [
          [
            2,
            0,
            2,
            1,
            1,
            0
          ]
        ]
      },
      "expected": [
        0,
        0,
        1,
        1,
        2,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_29_edge_single",
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
      "name": "case_30_edge_blocks",
      "input": {
        "args": [
          [
            2,
            2,
            1,
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
        0,
        0,
        1,
        1,
        2,
        2
      ]
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            2,
            0,
            2,
            1,
            1,
            0
          ]
        ]
      },
      "expected": [
        0,
        0,
        1,
        1,
        2,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_32_edge_single",
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
      "name": "case_33_edge_blocks",
      "input": {
        "args": [
          [
            2,
            2,
            1,
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
        0,
        0,
        1,
        1,
        2,
        2
      ]
    },
    {
      "name": "case_34_base",
      "input": {
        "args": [
          [
            2,
            0,
            2,
            1,
            1,
            0
          ]
        ]
      },
      "expected": [
        0,
        0,
        1,
        1,
        2,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_35_edge_single",
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
      "name": "case_36_edge_blocks",
      "input": {
        "args": [
          [
            2,
            2,
            1,
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
        0,
        0,
        1,
        1,
        2,
        2
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            2,
            0,
            2,
            1,
            1,
            0
          ]
        ]
      },
      "expected": [
        0,
        0,
        1,
        1,
        2,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_38_edge_single",
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
      "name": "case_39_edge_blocks",
      "input": {
        "args": [
          [
            2,
            2,
            1,
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
        0,
        0,
        1,
        1,
        2,
        2
      ]
    },
    {
      "name": "case_40_base",
      "input": {
        "args": [
          [
            2,
            0,
            2,
            1,
            1,
            0
          ]
        ]
      },
      "expected": [
        0,
        0,
        1,
        1,
        2,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    }
  ]
}
```
