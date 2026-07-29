# 题目226 翻转二叉树

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一棵二叉树的根节点 `root` ，翻转这棵二叉树，并返回其根节点。
示例 1：
题目配图：
输入：root = [4,2,7,1,3,6,9]输出：[4,7,2,9,6,3,1]
示例 2：
题目配图：
输入：root = [2,1,3]输出：[2,3,1]
示例 3：
输入：root = []输出：[]
提示：
树中节点数目范围在 `[0, 100]` 内
`-100 <= Node.val <= 100`

```json
{
  "id": 226,
  "title": "翻转二叉树",
  "difficulty": "简单",
  "method": "question_226",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              4,
              2,
              7,
              1,
              3,
              6,
              9
            ]
          }
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          4,
          7,
          2,
          9,
          6,
          3,
          1
        ]
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_04_edge_chain",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              null,
              3
            ]
          }
        ]
      },
      "expected": [
        1,
        null,
        2,
        null,
        3
      ]
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              4,
              2,
              7,
              1,
              3,
              6,
              9
            ]
          }
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          4,
          7,
          2,
          9,
          6,
          3,
          1
        ]
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_08_edge_chain",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              null,
              3
            ]
          }
        ]
      },
      "expected": [
        1,
        null,
        2,
        null,
        3
      ]
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              4,
              2,
              7,
              1,
              3,
              6,
              9
            ]
          }
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          4,
          7,
          2,
          9,
          6,
          3,
          1
        ]
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_12_edge_chain",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              null,
              3
            ]
          }
        ]
      },
      "expected": [
        1,
        null,
        2,
        null,
        3
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              4,
              2,
              7,
              1,
              3,
              6,
              9
            ]
          }
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          4,
          7,
          2,
          9,
          6,
          3,
          1
        ]
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_16_edge_chain",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              null,
              3
            ]
          }
        ]
      },
      "expected": [
        1,
        null,
        2,
        null,
        3
      ]
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              4,
              2,
              7,
              1,
              3,
              6,
              9
            ]
          }
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          4,
          7,
          2,
          9,
          6,
          3,
          1
        ]
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_20_edge_chain",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              null,
              3
            ]
          }
        ]
      },
      "expected": [
        1,
        null,
        2,
        null,
        3
      ]
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              4,
              2,
              7,
              1,
              3,
              6,
              9
            ]
          }
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          4,
          7,
          2,
          9,
          6,
          3,
          1
        ]
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_24_edge_chain",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              null,
              3
            ]
          }
        ]
      },
      "expected": [
        1,
        null,
        2,
        null,
        3
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              4,
              2,
              7,
              1,
              3,
              6,
              9
            ]
          }
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          4,
          7,
          2,
          9,
          6,
          3,
          1
        ]
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_28_edge_chain",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              null,
              3
            ]
          }
        ]
      },
      "expected": [
        1,
        null,
        2,
        null,
        3
      ]
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              4,
              2,
              7,
              1,
              3,
              6,
              9
            ]
          }
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          4,
          7,
          2,
          9,
          6,
          3,
          1
        ]
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_32_edge_chain",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              null,
              3
            ]
          }
        ]
      },
      "expected": [
        1,
        null,
        2,
        null,
        3
      ]
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              4,
              2,
              7,
              1,
              3,
              6,
              9
            ]
          }
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          4,
          7,
          2,
          9,
          6,
          3,
          1
        ]
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_36_edge_chain",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              null,
              3
            ]
          }
        ]
      },
      "expected": [
        1,
        null,
        2,
        null,
        3
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              4,
              2,
              7,
              1,
              3,
              6,
              9
            ]
          }
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          4,
          7,
          2,
          9,
          6,
          3,
          1
        ]
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_40_edge_chain",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              null,
              3
            ]
          }
        ]
      },
      "expected": [
        1,
        null,
        2,
        null,
        3
      ]
    }
  ]
}
```
