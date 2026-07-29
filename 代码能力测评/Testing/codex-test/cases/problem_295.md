# 题目295 数据流的中位数

来源：LeetCode 热题 100（https://leetcode.cn/studyplan/top-100-liked/）

```json
{
  "id": 295,
  "title": "数据流的中位数",
  "difficulty": "困难",
  "method": "question_295",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "findMedian",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              1
            ],
            [
              2
            ],
            [],
            [
              3
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        1.5,
        null,
        2.0
      ]
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              -1
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        -1.0
      ]
    },
    {
      "name": "case_03_edge_negative_even",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              -1
            ],
            [
              -2
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        -1.5
      ]
    },
    {
      "name": "case_04_edge_odd",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              5
            ],
            [
              15
            ],
            [
              1
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        5.0
      ]
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "findMedian",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              1
            ],
            [
              2
            ],
            [],
            [
              3
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        1.5,
        null,
        2.0
      ]
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              -1
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        -1.0
      ]
    },
    {
      "name": "case_07_edge_negative_even",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              -1
            ],
            [
              -2
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        -1.5
      ]
    },
    {
      "name": "case_08_edge_odd",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              5
            ],
            [
              15
            ],
            [
              1
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        5.0
      ]
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "findMedian",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              1
            ],
            [
              2
            ],
            [],
            [
              3
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        1.5,
        null,
        2.0
      ]
    },
    {
      "name": "case_10_base",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              -1
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        -1.0
      ]
    },
    {
      "name": "case_11_edge_negative_even",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              -1
            ],
            [
              -2
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        -1.5
      ]
    },
    {
      "name": "case_12_edge_odd",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              5
            ],
            [
              15
            ],
            [
              1
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        5.0
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "findMedian",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              1
            ],
            [
              2
            ],
            [],
            [
              3
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        1.5,
        null,
        2.0
      ]
    },
    {
      "name": "case_14_base",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              -1
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        -1.0
      ]
    },
    {
      "name": "case_15_edge_negative_even",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              -1
            ],
            [
              -2
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        -1.5
      ]
    },
    {
      "name": "case_16_edge_odd",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              5
            ],
            [
              15
            ],
            [
              1
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        5.0
      ]
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "findMedian",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              1
            ],
            [
              2
            ],
            [],
            [
              3
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        1.5,
        null,
        2.0
      ]
    },
    {
      "name": "case_18_base",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              -1
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        -1.0
      ]
    },
    {
      "name": "case_19_edge_negative_even",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              -1
            ],
            [
              -2
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        -1.5
      ]
    },
    {
      "name": "case_20_edge_odd",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              5
            ],
            [
              15
            ],
            [
              1
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        5.0
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "findMedian",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              1
            ],
            [
              2
            ],
            [],
            [
              3
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        1.5,
        null,
        2.0
      ]
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              -1
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        -1.0
      ]
    },
    {
      "name": "case_23_edge_negative_even",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              -1
            ],
            [
              -2
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        -1.5
      ]
    },
    {
      "name": "case_24_edge_odd",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              5
            ],
            [
              15
            ],
            [
              1
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        5.0
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "findMedian",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              1
            ],
            [
              2
            ],
            [],
            [
              3
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        1.5,
        null,
        2.0
      ]
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              -1
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        -1.0
      ]
    },
    {
      "name": "case_27_edge_negative_even",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              -1
            ],
            [
              -2
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        -1.5
      ]
    },
    {
      "name": "case_28_edge_odd",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              5
            ],
            [
              15
            ],
            [
              1
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        5.0
      ]
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "findMedian",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              1
            ],
            [
              2
            ],
            [],
            [
              3
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        1.5,
        null,
        2.0
      ]
    },
    {
      "name": "case_30_base",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              -1
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        -1.0
      ]
    },
    {
      "name": "case_31_edge_negative_even",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              -1
            ],
            [
              -2
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        -1.5
      ]
    },
    {
      "name": "case_32_edge_odd",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              5
            ],
            [
              15
            ],
            [
              1
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        5.0
      ]
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "findMedian",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              1
            ],
            [
              2
            ],
            [],
            [
              3
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        1.5,
        null,
        2.0
      ]
    },
    {
      "name": "case_34_base",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              -1
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        -1.0
      ]
    },
    {
      "name": "case_35_edge_negative_even",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              -1
            ],
            [
              -2
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        -1.5
      ]
    },
    {
      "name": "case_36_edge_odd",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              5
            ],
            [
              15
            ],
            [
              1
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        5.0
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "findMedian",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              1
            ],
            [
              2
            ],
            [],
            [
              3
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        1.5,
        null,
        2.0
      ]
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              -1
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        -1.0
      ]
    },
    {
      "name": "case_39_edge_negative_even",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              -1
            ],
            [
              -2
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        -1.5
      ]
    },
    {
      "name": "case_40_edge_odd",
      "input": {
        "args": [
          [
            "MedianFinder",
            "addNum",
            "addNum",
            "addNum",
            "findMedian"
          ],
          [
            [],
            [
              5
            ],
            [
              15
            ],
            [
              1
            ],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        5.0
      ]
    }
  ]
}
```
