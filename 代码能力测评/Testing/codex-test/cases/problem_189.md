# 题目189 轮转数组

来源：LeetCode 热题 100（https://leetcode.cn/studyplan/top-100-liked/）

```json
{
  "id": 189,
  "title": "轮转数组",
  "difficulty": "中等",
  "method": "question_189",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            4,
            5,
            6,
            7
          ],
          3
        ]
      },
      "expected": [
        5,
        6,
        7,
        1,
        2,
        3,
        4
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
            -1,
            -100,
            3,
            99
          ],
          2
        ]
      },
      "expected": [
        3,
        99,
        -1,
        -100
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_03_base",
      "input": {
        "args": [
          [
            1,
            2
          ],
          0
        ]
      },
      "expected": [
        1,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_04_base",
      "input": {
        "args": [
          [
            1
          ],
          10
        ]
      },
      "expected": [
        1
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_05_edge_k_equal_n",
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
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_06_edge_k_gt_n",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ],
          4
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
      "name": "case_07_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          99
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
      "name": "case_08_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            4,
            5,
            6,
            7
          ],
          3
        ]
      },
      "expected": [
        5,
        6,
        7,
        1,
        2,
        3,
        4
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          [
            -1,
            -100,
            3,
            99
          ],
          2
        ]
      },
      "expected": [
        3,
        99,
        -1,
        -100
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_10_base",
      "input": {
        "args": [
          [
            1,
            2
          ],
          0
        ]
      },
      "expected": [
        1,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          [
            1
          ],
          10
        ]
      },
      "expected": [
        1
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_12_edge_k_equal_n",
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
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_13_edge_k_gt_n",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ],
          4
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
      "name": "case_14_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          99
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
      "name": "case_15_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            4,
            5,
            6,
            7
          ],
          3
        ]
      },
      "expected": [
        5,
        6,
        7,
        1,
        2,
        3,
        4
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            -1,
            -100,
            3,
            99
          ],
          2
        ]
      },
      "expected": [
        3,
        99,
        -1,
        -100
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
            1,
            2
          ],
          0
        ]
      },
      "expected": [
        1,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_18_base",
      "input": {
        "args": [
          [
            1
          ],
          10
        ]
      },
      "expected": [
        1
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_19_edge_k_equal_n",
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
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_20_edge_k_gt_n",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ],
          4
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
      "name": "case_21_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          99
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
      "name": "case_22_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            4,
            5,
            6,
            7
          ],
          3
        ]
      },
      "expected": [
        5,
        6,
        7,
        1,
        2,
        3,
        4
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_23_base",
      "input": {
        "args": [
          [
            -1,
            -100,
            3,
            99
          ],
          2
        ]
      },
      "expected": [
        3,
        99,
        -1,
        -100
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_24_base",
      "input": {
        "args": [
          [
            1,
            2
          ],
          0
        ]
      },
      "expected": [
        1,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            1
          ],
          10
        ]
      },
      "expected": [
        1
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_26_edge_k_equal_n",
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
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_27_edge_k_gt_n",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ],
          4
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
      "name": "case_28_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          99
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
      "name": "case_29_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            4,
            5,
            6,
            7
          ],
          3
        ]
      },
      "expected": [
        5,
        6,
        7,
        1,
        2,
        3,
        4
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_30_base",
      "input": {
        "args": [
          [
            -1,
            -100,
            3,
            99
          ],
          2
        ]
      },
      "expected": [
        3,
        99,
        -1,
        -100
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            1,
            2
          ],
          0
        ]
      },
      "expected": [
        1,
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
            1
          ],
          10
        ]
      },
      "expected": [
        1
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_33_edge_k_equal_n",
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
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        2,
        3
      ]
    },
    {
      "name": "case_34_edge_k_gt_n",
      "input": {
        "args": [
          [
            1,
            2,
            3
          ],
          4
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
      "name": "case_35_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          99
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
      "name": "case_36_base",
      "input": {
        "args": [
          [
            1,
            2,
            3,
            4,
            5,
            6,
            7
          ],
          3
        ]
      },
      "expected": [
        5,
        6,
        7,
        1,
        2,
        3,
        4
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
            -1,
            -100,
            3,
            99
          ],
          2
        ]
      },
      "expected": [
        3,
        99,
        -1,
        -100
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          [
            1,
            2
          ],
          0
        ]
      },
      "expected": [
        1,
        2
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_39_base",
      "input": {
        "args": [
          [
            1
          ],
          10
        ]
      },
      "expected": [
        1
      ],
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_40_edge_k_equal_n",
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
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        2,
        3
      ]
    }
  ]
}
```
