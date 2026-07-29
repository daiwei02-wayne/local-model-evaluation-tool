# 题目207 课程表

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

你这个学期必须选修 `numCourses` 门课程，记为 `0` 到 `numCourses - 1` 。
在选修某些课程之前需要一些先修课程。 先修课程按数组 `prerequisites` 给出，其中 prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>] ，表示如果要学习课程 a<sub>i</sub> 则 必须 先学习课程  b<sub>i</sub>。
例如，先修课程对 `[0, 1]` 表示：想要学习课程 `0` ，你需要先完成课程 `1` 。
请你判断是否可能完成所有课程的学习？如果可以，返回 `true` ；否则，返回 `false` 。
示例 1：
输入：numCourses = 2, prerequisites = [[1,0]]输出：true解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
示例 2：
输入：numCourses = 2, prerequisites = [[1,0],[0,1]]输出：false解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
提示：
1 <= numCourses <= 10<sup>5</sup>
`0 <= prerequisites.length <= 5000`
`prerequisites[i].length == 2`
0 <= a<sub>i</sub>, b<sub>i</sub> < numCourses
`prerequisites[i]` 中的所有课程对 互不相同

```json
{
  "id": 207,
  "title": "课程表",
  "difficulty": "中等",
  "method": "question_207",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          2,
          [
            [
              1,
              0
            ]
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          2,
          [
            [
              1,
              0
            ],
            [
              0,
              1
            ]
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_03_edge_one_course",
      "input": {
        "args": [
          1,
          []
        ]
      },
      "expected": true
    },
    {
      "name": "case_04_edge_chain",
      "input": {
        "args": [
          3,
          [
            [
              1,
              0
            ],
            [
              2,
              1
            ]
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_05_edge_cycle_three",
      "input": {
        "args": [
          3,
          [
            [
              0,
              1
            ],
            [
              1,
              2
            ],
            [
              2,
              0
            ]
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          2,
          [
            [
              1,
              0
            ]
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          2,
          [
            [
              1,
              0
            ],
            [
              0,
              1
            ]
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_08_edge_one_course",
      "input": {
        "args": [
          1,
          []
        ]
      },
      "expected": true
    },
    {
      "name": "case_09_edge_chain",
      "input": {
        "args": [
          3,
          [
            [
              1,
              0
            ],
            [
              2,
              1
            ]
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_10_edge_cycle_three",
      "input": {
        "args": [
          3,
          [
            [
              0,
              1
            ],
            [
              1,
              2
            ],
            [
              2,
              0
            ]
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          2,
          [
            [
              1,
              0
            ]
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          2,
          [
            [
              1,
              0
            ],
            [
              0,
              1
            ]
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_13_edge_one_course",
      "input": {
        "args": [
          1,
          []
        ]
      },
      "expected": true
    },
    {
      "name": "case_14_edge_chain",
      "input": {
        "args": [
          3,
          [
            [
              1,
              0
            ],
            [
              2,
              1
            ]
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_15_edge_cycle_three",
      "input": {
        "args": [
          3,
          [
            [
              0,
              1
            ],
            [
              1,
              2
            ],
            [
              2,
              0
            ]
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          2,
          [
            [
              1,
              0
            ]
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          2,
          [
            [
              1,
              0
            ],
            [
              0,
              1
            ]
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_18_edge_one_course",
      "input": {
        "args": [
          1,
          []
        ]
      },
      "expected": true
    },
    {
      "name": "case_19_edge_chain",
      "input": {
        "args": [
          3,
          [
            [
              1,
              0
            ],
            [
              2,
              1
            ]
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_20_edge_cycle_three",
      "input": {
        "args": [
          3,
          [
            [
              0,
              1
            ],
            [
              1,
              2
            ],
            [
              2,
              0
            ]
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          2,
          [
            [
              1,
              0
            ]
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          2,
          [
            [
              1,
              0
            ],
            [
              0,
              1
            ]
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_23_edge_one_course",
      "input": {
        "args": [
          1,
          []
        ]
      },
      "expected": true
    },
    {
      "name": "case_24_edge_chain",
      "input": {
        "args": [
          3,
          [
            [
              1,
              0
            ],
            [
              2,
              1
            ]
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_25_edge_cycle_three",
      "input": {
        "args": [
          3,
          [
            [
              0,
              1
            ],
            [
              1,
              2
            ],
            [
              2,
              0
            ]
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          2,
          [
            [
              1,
              0
            ]
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          2,
          [
            [
              1,
              0
            ],
            [
              0,
              1
            ]
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_28_edge_one_course",
      "input": {
        "args": [
          1,
          []
        ]
      },
      "expected": true
    },
    {
      "name": "case_29_edge_chain",
      "input": {
        "args": [
          3,
          [
            [
              1,
              0
            ],
            [
              2,
              1
            ]
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_30_edge_cycle_three",
      "input": {
        "args": [
          3,
          [
            [
              0,
              1
            ],
            [
              1,
              2
            ],
            [
              2,
              0
            ]
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          2,
          [
            [
              1,
              0
            ]
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          2,
          [
            [
              1,
              0
            ],
            [
              0,
              1
            ]
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_33_edge_one_course",
      "input": {
        "args": [
          1,
          []
        ]
      },
      "expected": true
    },
    {
      "name": "case_34_edge_chain",
      "input": {
        "args": [
          3,
          [
            [
              1,
              0
            ],
            [
              2,
              1
            ]
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_35_edge_cycle_three",
      "input": {
        "args": [
          3,
          [
            [
              0,
              1
            ],
            [
              1,
              2
            ],
            [
              2,
              0
            ]
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          2,
          [
            [
              1,
              0
            ]
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          2,
          [
            [
              1,
              0
            ],
            [
              0,
              1
            ]
          ]
        ]
      },
      "expected": false
    },
    {
      "name": "case_38_edge_one_course",
      "input": {
        "args": [
          1,
          []
        ]
      },
      "expected": true
    },
    {
      "name": "case_39_edge_chain",
      "input": {
        "args": [
          3,
          [
            [
              1,
              0
            ],
            [
              2,
              1
            ]
          ]
        ]
      },
      "expected": true
    },
    {
      "name": "case_40_edge_cycle_three",
      "input": {
        "args": [
          3,
          [
            [
              0,
              1
            ],
            [
              1,
              2
            ],
            [
              2,
              0
            ]
          ]
        ]
      },
      "expected": false
    }
  ]
}
```
