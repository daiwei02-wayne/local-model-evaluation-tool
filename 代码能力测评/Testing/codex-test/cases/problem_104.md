# 题目104 二叉树的最大深度

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。
示例：
给定二叉树 `[3,9,20,null,null,15,7]`，
3   / \  9  20    /  \   15   7
返回它的最大深度 3 。

```json
{
  "id": 104,
  "title": "二叉树的最大深度",
  "difficulty": "简单",
  "method": "question_104",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          {
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
      "expected": 1
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
      "expected": 4
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          {
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
      "expected": 1
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
      "expected": 4
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          {
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
      "expected": 1
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
      "expected": 4
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          {
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
      "expected": 1
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
      "expected": 4
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          {
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
      "expected": 1
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
      "expected": 4
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          {
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
      "expected": 1
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
      "expected": 4
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          {
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
      "expected": 1
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
      "expected": 4
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          {
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
      "expected": 1
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
      "expected": 4
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          {
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
      "expected": 1
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
      "expected": 4
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          {
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
      "expected": 1
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
      "expected": 4
    }
  ]
}
```
