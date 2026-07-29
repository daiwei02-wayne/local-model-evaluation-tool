# 题目155 最小栈

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

设计一个支持 `push` ，`pop` ，`top` 操作，并能在常数时间内检索到最小元素的栈。
实现 `MinStack` 类:
`MinStack()` 初始化堆栈对象。
`void push(int val)` 将元素val推入堆栈。
`void pop()` 删除堆栈顶部的元素。
`int top()` 获取堆栈顶部的元素。
`int getMin()` 获取堆栈中的最小元素。
示例 1:
输入：["MinStack","push","push","push","getMin","pop","top","getMin"][[],[-2],[0],[-3],[],[],[],[]]输出：[null,null,null,null,-3,null,0,-2]解释：MinStack minStack = new MinStack();minStack.push(-2);minStack.push(0);minStack.push(-3);minStack.getMin();   --> 返回 -3.minStack.pop();minStack.top();      --> 返回 0.minStack.getMin();   --> 返回 -2.
提示：
-2<sup>31</sup> <= val <= 2<sup>31</sup> - 1
`pop`、`top` 和 `getMin` 操作总是在 非空栈 上调用
`push`, `pop`, `top`, and `getMin`最多被调用 3 * 10<sup>4</sup> 次

```json
{
  "id": 155,
  "title": "最小栈",
  "difficulty": "中等",
  "method": "question_155",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "push",
            "getMin",
            "pop",
            "top",
            "getMin"
          ],
          [
            [],
            [
              -2
            ],
            [
              0
            ],
            [
              -3
            ],
            [],
            [],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        -3,
        null,
        0,
        -2
      ]
    },
    {
      "name": "case_02_edge_single",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "getMin",
            "top"
          ],
          [
            [],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        1,
        1
      ]
    },
    {
      "name": "case_03_edge_pop_min",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "pop",
            "getMin"
          ],
          [
            [],
            [
              2
            ],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        2
      ]
    },
    {
      "name": "case_04_base",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "push",
            "getMin",
            "pop",
            "top",
            "getMin"
          ],
          [
            [],
            [
              -2
            ],
            [
              0
            ],
            [
              -3
            ],
            [],
            [],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        -3,
        null,
        0,
        -2
      ]
    },
    {
      "name": "case_05_edge_single",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "getMin",
            "top"
          ],
          [
            [],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        1,
        1
      ]
    },
    {
      "name": "case_06_edge_pop_min",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "pop",
            "getMin"
          ],
          [
            [],
            [
              2
            ],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        2
      ]
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "push",
            "getMin",
            "pop",
            "top",
            "getMin"
          ],
          [
            [],
            [
              -2
            ],
            [
              0
            ],
            [
              -3
            ],
            [],
            [],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        -3,
        null,
        0,
        -2
      ]
    },
    {
      "name": "case_08_edge_single",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "getMin",
            "top"
          ],
          [
            [],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        1,
        1
      ]
    },
    {
      "name": "case_09_edge_pop_min",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "pop",
            "getMin"
          ],
          [
            [],
            [
              2
            ],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        2
      ]
    },
    {
      "name": "case_10_base",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "push",
            "getMin",
            "pop",
            "top",
            "getMin"
          ],
          [
            [],
            [
              -2
            ],
            [
              0
            ],
            [
              -3
            ],
            [],
            [],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        -3,
        null,
        0,
        -2
      ]
    },
    {
      "name": "case_11_edge_single",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "getMin",
            "top"
          ],
          [
            [],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        1,
        1
      ]
    },
    {
      "name": "case_12_edge_pop_min",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "pop",
            "getMin"
          ],
          [
            [],
            [
              2
            ],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        2
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "push",
            "getMin",
            "pop",
            "top",
            "getMin"
          ],
          [
            [],
            [
              -2
            ],
            [
              0
            ],
            [
              -3
            ],
            [],
            [],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        -3,
        null,
        0,
        -2
      ]
    },
    {
      "name": "case_14_edge_single",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "getMin",
            "top"
          ],
          [
            [],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        1,
        1
      ]
    },
    {
      "name": "case_15_edge_pop_min",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "pop",
            "getMin"
          ],
          [
            [],
            [
              2
            ],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        2
      ]
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "push",
            "getMin",
            "pop",
            "top",
            "getMin"
          ],
          [
            [],
            [
              -2
            ],
            [
              0
            ],
            [
              -3
            ],
            [],
            [],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        -3,
        null,
        0,
        -2
      ]
    },
    {
      "name": "case_17_edge_single",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "getMin",
            "top"
          ],
          [
            [],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        1,
        1
      ]
    },
    {
      "name": "case_18_edge_pop_min",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "pop",
            "getMin"
          ],
          [
            [],
            [
              2
            ],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        2
      ]
    },
    {
      "name": "case_19_base",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "push",
            "getMin",
            "pop",
            "top",
            "getMin"
          ],
          [
            [],
            [
              -2
            ],
            [
              0
            ],
            [
              -3
            ],
            [],
            [],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        -3,
        null,
        0,
        -2
      ]
    },
    {
      "name": "case_20_edge_single",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "getMin",
            "top"
          ],
          [
            [],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        1,
        1
      ]
    },
    {
      "name": "case_21_edge_pop_min",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "pop",
            "getMin"
          ],
          [
            [],
            [
              2
            ],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        2
      ]
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "push",
            "getMin",
            "pop",
            "top",
            "getMin"
          ],
          [
            [],
            [
              -2
            ],
            [
              0
            ],
            [
              -3
            ],
            [],
            [],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        -3,
        null,
        0,
        -2
      ]
    },
    {
      "name": "case_23_edge_single",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "getMin",
            "top"
          ],
          [
            [],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        1,
        1
      ]
    },
    {
      "name": "case_24_edge_pop_min",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "pop",
            "getMin"
          ],
          [
            [],
            [
              2
            ],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        2
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "push",
            "getMin",
            "pop",
            "top",
            "getMin"
          ],
          [
            [],
            [
              -2
            ],
            [
              0
            ],
            [
              -3
            ],
            [],
            [],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        -3,
        null,
        0,
        -2
      ]
    },
    {
      "name": "case_26_edge_single",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "getMin",
            "top"
          ],
          [
            [],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        1,
        1
      ]
    },
    {
      "name": "case_27_edge_pop_min",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "pop",
            "getMin"
          ],
          [
            [],
            [
              2
            ],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        2
      ]
    },
    {
      "name": "case_28_base",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "push",
            "getMin",
            "pop",
            "top",
            "getMin"
          ],
          [
            [],
            [
              -2
            ],
            [
              0
            ],
            [
              -3
            ],
            [],
            [],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        -3,
        null,
        0,
        -2
      ]
    },
    {
      "name": "case_29_edge_single",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "getMin",
            "top"
          ],
          [
            [],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        1,
        1
      ]
    },
    {
      "name": "case_30_edge_pop_min",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "pop",
            "getMin"
          ],
          [
            [],
            [
              2
            ],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        2
      ]
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "push",
            "getMin",
            "pop",
            "top",
            "getMin"
          ],
          [
            [],
            [
              -2
            ],
            [
              0
            ],
            [
              -3
            ],
            [],
            [],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        -3,
        null,
        0,
        -2
      ]
    },
    {
      "name": "case_32_edge_single",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "getMin",
            "top"
          ],
          [
            [],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        1,
        1
      ]
    },
    {
      "name": "case_33_edge_pop_min",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "pop",
            "getMin"
          ],
          [
            [],
            [
              2
            ],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        2
      ]
    },
    {
      "name": "case_34_base",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "push",
            "getMin",
            "pop",
            "top",
            "getMin"
          ],
          [
            [],
            [
              -2
            ],
            [
              0
            ],
            [
              -3
            ],
            [],
            [],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        -3,
        null,
        0,
        -2
      ]
    },
    {
      "name": "case_35_edge_single",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "getMin",
            "top"
          ],
          [
            [],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        1,
        1
      ]
    },
    {
      "name": "case_36_edge_pop_min",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "pop",
            "getMin"
          ],
          [
            [],
            [
              2
            ],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        2
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "push",
            "getMin",
            "pop",
            "top",
            "getMin"
          ],
          [
            [],
            [
              -2
            ],
            [
              0
            ],
            [
              -3
            ],
            [],
            [],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        -3,
        null,
        0,
        -2
      ]
    },
    {
      "name": "case_38_edge_single",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "getMin",
            "top"
          ],
          [
            [],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        1,
        1
      ]
    },
    {
      "name": "case_39_edge_pop_min",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "pop",
            "getMin"
          ],
          [
            [],
            [
              2
            ],
            [
              1
            ],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        2
      ]
    },
    {
      "name": "case_40_base",
      "input": {
        "args": [
          [
            "MinStack",
            "push",
            "push",
            "push",
            "getMin",
            "pop",
            "top",
            "getMin"
          ],
          [
            [],
            [
              -2
            ],
            [
              0
            ],
            [
              -3
            ],
            [],
            [],
            [],
            []
          ]
        ]
      },
      "expected": [
        null,
        null,
        null,
        null,
        -3,
        null,
        0,
        -2
      ]
    }
  ]
}
```
