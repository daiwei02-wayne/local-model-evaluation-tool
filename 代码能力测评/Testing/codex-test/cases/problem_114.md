# 题目114 二叉树展开为链表

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你二叉树的根结点 `root` ，请你将它展开为一个单链表：
展开后的单链表应该同样使用 `TreeNode` ，其中 `right` 子指针指向链表中下一个结点，而左子指针始终为 `null` 。
展开后的单链表应该与二叉树 顺序相同。
示例 1：
题目配图：
输入：root = [1,2,5,3,4,null,6]输出：[1,null,2,null,3,null,4,null,5,null,6]
示例 2：
输入：root = []输出：[]
示例 3：
输入：root = [0]输出：[0]
提示：
树中结点数在范围 `[0, 2000]` 内
`-100 <= Node.val <= 100`
进阶：你可以使用原地算法（`O(1)` 额外空间）展开这棵树吗？

```json
{
  "id": 114,
  "title": "二叉树展开为链表",
  "difficulty": "中等",
  "method": "question_114",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              5,
              3,
              4,
              null,
              6
            ]
          }
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          1,
          null,
          2,
          null,
          3,
          null,
          4,
          null,
          5,
          null,
          6
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_02_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": []
          }
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": null
    },
    {
      "name": "case_03_edge_single",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1
            ]
          }
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
      "name": "case_04_edge_balanced",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              5,
              3,
              4,
              null,
              6
            ]
          }
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        null,
        2,
        null,
        3,
        null,
        4,
        null,
        5,
        null,
        6
      ]
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              5,
              3,
              4,
              null,
              6
            ]
          }
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          1,
          null,
          2,
          null,
          3,
          null,
          4,
          null,
          5,
          null,
          6
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_06_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": []
          }
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": null
    },
    {
      "name": "case_07_edge_single",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1
            ]
          }
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
      "name": "case_08_edge_balanced",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              5,
              3,
              4,
              null,
              6
            ]
          }
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        null,
        2,
        null,
        3,
        null,
        4,
        null,
        5,
        null,
        6
      ]
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              5,
              3,
              4,
              null,
              6
            ]
          }
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          1,
          null,
          2,
          null,
          3,
          null,
          4,
          null,
          5,
          null,
          6
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_10_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": []
          }
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": null
    },
    {
      "name": "case_11_edge_single",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1
            ]
          }
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
      "name": "case_12_edge_balanced",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              5,
              3,
              4,
              null,
              6
            ]
          }
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        null,
        2,
        null,
        3,
        null,
        4,
        null,
        5,
        null,
        6
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              5,
              3,
              4,
              null,
              6
            ]
          }
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          1,
          null,
          2,
          null,
          3,
          null,
          4,
          null,
          5,
          null,
          6
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_14_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": []
          }
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": null
    },
    {
      "name": "case_15_edge_single",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1
            ]
          }
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
      "name": "case_16_edge_balanced",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              5,
              3,
              4,
              null,
              6
            ]
          }
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        null,
        2,
        null,
        3,
        null,
        4,
        null,
        5,
        null,
        6
      ]
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              5,
              3,
              4,
              null,
              6
            ]
          }
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          1,
          null,
          2,
          null,
          3,
          null,
          4,
          null,
          5,
          null,
          6
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_18_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": []
          }
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": null
    },
    {
      "name": "case_19_edge_single",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1
            ]
          }
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
      "name": "case_20_edge_balanced",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              5,
              3,
              4,
              null,
              6
            ]
          }
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        null,
        2,
        null,
        3,
        null,
        4,
        null,
        5,
        null,
        6
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              5,
              3,
              4,
              null,
              6
            ]
          }
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          1,
          null,
          2,
          null,
          3,
          null,
          4,
          null,
          5,
          null,
          6
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_22_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": []
          }
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": null
    },
    {
      "name": "case_23_edge_single",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1
            ]
          }
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
      "name": "case_24_edge_balanced",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              5,
              3,
              4,
              null,
              6
            ]
          }
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        null,
        2,
        null,
        3,
        null,
        4,
        null,
        5,
        null,
        6
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              5,
              3,
              4,
              null,
              6
            ]
          }
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          1,
          null,
          2,
          null,
          3,
          null,
          4,
          null,
          5,
          null,
          6
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_26_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": []
          }
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": null
    },
    {
      "name": "case_27_edge_single",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1
            ]
          }
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
      "name": "case_28_edge_balanced",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              5,
              3,
              4,
              null,
              6
            ]
          }
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        null,
        2,
        null,
        3,
        null,
        4,
        null,
        5,
        null,
        6
      ]
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              5,
              3,
              4,
              null,
              6
            ]
          }
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          1,
          null,
          2,
          null,
          3,
          null,
          4,
          null,
          5,
          null,
          6
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_30_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": []
          }
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": null
    },
    {
      "name": "case_31_edge_single",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1
            ]
          }
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
      "name": "case_32_edge_balanced",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              5,
              3,
              4,
              null,
              6
            ]
          }
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        null,
        2,
        null,
        3,
        null,
        4,
        null,
        5,
        null,
        6
      ]
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              5,
              3,
              4,
              null,
              6
            ]
          }
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          1,
          null,
          2,
          null,
          3,
          null,
          4,
          null,
          5,
          null,
          6
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_34_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": []
          }
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": null
    },
    {
      "name": "case_35_edge_single",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1
            ]
          }
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
      "name": "case_36_edge_balanced",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              5,
              3,
              4,
              null,
              6
            ]
          }
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        null,
        2,
        null,
        3,
        null,
        4,
        null,
        5,
        null,
        6
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              5,
              3,
              4,
              null,
              6
            ]
          }
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          1,
          null,
          2,
          null,
          3,
          null,
          4,
          null,
          5,
          null,
          6
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      }
    },
    {
      "name": "case_38_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": []
          }
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": null
    },
    {
      "name": "case_39_edge_single",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1
            ]
          }
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
      "name": "case_40_edge_balanced",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              5,
              3,
              4,
              null,
              6
            ]
          }
        ]
      },
      "expectation": {
        "source": "arg",
        "index": 0
      },
      "expected": [
        1,
        null,
        2,
        null,
        3,
        null,
        4,
        null,
        5,
        null,
        6
      ]
    }
  ]
}
```
