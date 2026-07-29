# 题目543 二叉树的直径

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
示例 :
给定二叉树
1         / \        2   3       / \      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
注意：两结点之间的路径长度是以它们之间边的数目表示。

```json
{
  "id": 543,
  "title": "二叉树的直径",
  "difficulty": "简单",
  "method": "question_543",
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
              3,
              4,
              5
            ]
          }
        ]
      },
      "expected": 3
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
      "expected": 0
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
      "expected": 0
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
              3,
              null,
              4
            ]
          }
        ]
      },
      "expected": 3
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
              3,
              4,
              5
            ]
          }
        ]
      },
      "expected": 3
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
      "expected": 0
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
      "expected": 0
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
              3,
              null,
              4
            ]
          }
        ]
      },
      "expected": 3
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
              3,
              4,
              5
            ]
          }
        ]
      },
      "expected": 3
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
      "expected": 0
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
      "expected": 0
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
              3,
              null,
              4
            ]
          }
        ]
      },
      "expected": 3
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
              3,
              4,
              5
            ]
          }
        ]
      },
      "expected": 3
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
      "expected": 0
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
      "expected": 0
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
              3,
              null,
              4
            ]
          }
        ]
      },
      "expected": 3
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
              3,
              4,
              5
            ]
          }
        ]
      },
      "expected": 3
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
      "expected": 0
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
      "expected": 0
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
              3,
              null,
              4
            ]
          }
        ]
      },
      "expected": 3
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
              3,
              4,
              5
            ]
          }
        ]
      },
      "expected": 3
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
      "expected": 0
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
      "expected": 0
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
              3,
              null,
              4
            ]
          }
        ]
      },
      "expected": 3
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
              3,
              4,
              5
            ]
          }
        ]
      },
      "expected": 3
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
      "expected": 0
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
      "expected": 0
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
              3,
              null,
              4
            ]
          }
        ]
      },
      "expected": 3
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
              3,
              4,
              5
            ]
          }
        ]
      },
      "expected": 3
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
      "expected": 0
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
      "expected": 0
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
              3,
              null,
              4
            ]
          }
        ]
      },
      "expected": 3
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
              3,
              4,
              5
            ]
          }
        ]
      },
      "expected": 3
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
      "expected": 0
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
      "expected": 0
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
              3,
              null,
              4
            ]
          }
        ]
      },
      "expected": 3
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
              3,
              4,
              5
            ]
          }
        ]
      },
      "expected": 3
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
      "expected": 0
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
      "expected": 0
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
              3,
              null,
              4
            ]
          }
        ]
      },
      "expected": 3
    }
  ]
}
```
