# 题目105 从前序与中序遍历序列构造二叉树

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定两个整数数组 `preorder` 和 `inorder` ，其中 `preorder` 是二叉树的先序遍历， `inorder` 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
示例 1:
题目配图：
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]输出: [3,9,20,null,null,15,7]
示例 2:
输入: preorder = [-1], inorder = [-1]输出: [-1]
提示:
`1 <= preorder.length <= 3000`
`inorder.length == preorder.length`
`-3000 <= preorder[i], inorder[i] <= 3000`
`preorder` 和 `inorder` 均 无重复 元素
`inorder` 均出现在 `preorder`
`preorder` 保证 为二叉树的前序遍历序列
`inorder` 保证 为二叉树的中序遍历序列

```json
{
  "id": 105,
  "title": "从前序与中序遍历序列构造二叉树",
  "difficulty": "中等",
  "method": "question_105",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            3,
            9,
            20,
            15,
            7
          ],
          [
            9,
            3,
            15,
            20,
            7
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          3,
          9,
          20,
          null,
          null,
          15,
          7
        ]
      }
    },
    {
      "name": "case_02_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          [
            1
          ]
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_03_edge_left_child",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            1
          ]
        ]
      },
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_04_edge_right_child",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            1,
            2
          ]
        ]
      },
      "expected": [
        1,
        null,
        2
      ]
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          [
            3,
            9,
            20,
            15,
            7
          ],
          [
            9,
            3,
            15,
            20,
            7
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          3,
          9,
          20,
          null,
          null,
          15,
          7
        ]
      }
    },
    {
      "name": "case_06_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          [
            1
          ]
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_07_edge_left_child",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            1
          ]
        ]
      },
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_08_edge_right_child",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            1,
            2
          ]
        ]
      },
      "expected": [
        1,
        null,
        2
      ]
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          [
            3,
            9,
            20,
            15,
            7
          ],
          [
            9,
            3,
            15,
            20,
            7
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          3,
          9,
          20,
          null,
          null,
          15,
          7
        ]
      }
    },
    {
      "name": "case_10_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          [
            1
          ]
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_11_edge_left_child",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            1
          ]
        ]
      },
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_12_edge_right_child",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            1,
            2
          ]
        ]
      },
      "expected": [
        1,
        null,
        2
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [
            3,
            9,
            20,
            15,
            7
          ],
          [
            9,
            3,
            15,
            20,
            7
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          3,
          9,
          20,
          null,
          null,
          15,
          7
        ]
      }
    },
    {
      "name": "case_14_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          [
            1
          ]
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_15_edge_left_child",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            1
          ]
        ]
      },
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_16_edge_right_child",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            1,
            2
          ]
        ]
      },
      "expected": [
        1,
        null,
        2
      ]
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          [
            3,
            9,
            20,
            15,
            7
          ],
          [
            9,
            3,
            15,
            20,
            7
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          3,
          9,
          20,
          null,
          null,
          15,
          7
        ]
      }
    },
    {
      "name": "case_18_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          [
            1
          ]
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_19_edge_left_child",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            1
          ]
        ]
      },
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_20_edge_right_child",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            1,
            2
          ]
        ]
      },
      "expected": [
        1,
        null,
        2
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          [
            3,
            9,
            20,
            15,
            7
          ],
          [
            9,
            3,
            15,
            20,
            7
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          3,
          9,
          20,
          null,
          null,
          15,
          7
        ]
      }
    },
    {
      "name": "case_22_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          [
            1
          ]
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_23_edge_left_child",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            1
          ]
        ]
      },
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_24_edge_right_child",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            1,
            2
          ]
        ]
      },
      "expected": [
        1,
        null,
        2
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            3,
            9,
            20,
            15,
            7
          ],
          [
            9,
            3,
            15,
            20,
            7
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          3,
          9,
          20,
          null,
          null,
          15,
          7
        ]
      }
    },
    {
      "name": "case_26_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          [
            1
          ]
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_27_edge_left_child",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            1
          ]
        ]
      },
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_28_edge_right_child",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            1,
            2
          ]
        ]
      },
      "expected": [
        1,
        null,
        2
      ]
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          [
            3,
            9,
            20,
            15,
            7
          ],
          [
            9,
            3,
            15,
            20,
            7
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          3,
          9,
          20,
          null,
          null,
          15,
          7
        ]
      }
    },
    {
      "name": "case_30_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          [
            1
          ]
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_31_edge_left_child",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            1
          ]
        ]
      },
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_32_edge_right_child",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            1,
            2
          ]
        ]
      },
      "expected": [
        1,
        null,
        2
      ]
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          [
            3,
            9,
            20,
            15,
            7
          ],
          [
            9,
            3,
            15,
            20,
            7
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          3,
          9,
          20,
          null,
          null,
          15,
          7
        ]
      }
    },
    {
      "name": "case_34_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          [
            1
          ]
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_35_edge_left_child",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            1
          ]
        ]
      },
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_36_edge_right_child",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            1,
            2
          ]
        ]
      },
      "expected": [
        1,
        null,
        2
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            3,
            9,
            20,
            15,
            7
          ],
          [
            9,
            3,
            15,
            20,
            7
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          3,
          9,
          20,
          null,
          null,
          15,
          7
        ]
      }
    },
    {
      "name": "case_38_edge_single",
      "input": {
        "args": [
          [
            1
          ],
          [
            1
          ]
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_39_edge_left_child",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            1
          ]
        ]
      },
      "expected": [
        1,
        2
      ]
    },
    {
      "name": "case_40_edge_right_child",
      "input": {
        "args": [
          [
            1,
            2
          ],
          [
            1,
            2
          ]
        ]
      },
      "expected": [
        1,
        null,
        2
      ]
    }
  ]
}
```
