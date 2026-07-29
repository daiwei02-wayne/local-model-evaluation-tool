# 题目124 二叉树中的最大路径和

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
路径和 是路径中各节点值的总和。
给你一个二叉树的根节点 `root` ，返回其 最大路径和 。
示例 1：
题目配图：
输入：root = [1,2,3]输出：6解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
示例 2：
题目配图：
输入：root = [-10,9,20,null,null,15,7]输出：42解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
提示：
树中节点数目范围是 [1, 3 * 10<sup>4</sup>]
`-1000 <= Node.val <= 1000`

```json
{
  "id": 124,
  "title": "二叉树中的最大路径和",
  "difficulty": "困难",
  "method": "question_124",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -10,
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
      "expected": 42
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              3
            ]
          }
        ]
      },
      "expected": 6
    },
    {
      "name": "case_03_edge_single_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -3
            ]
          }
        ]
      },
      "expected": -3
    },
    {
      "name": "case_04_edge_ignore_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              -1
            ]
          }
        ]
      },
      "expected": 2
    },
    {
      "name": "case_05_edge_all_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -2,
              -1
            ]
          }
        ]
      },
      "expected": -1
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -10,
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
      "expected": 42
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              3
            ]
          }
        ]
      },
      "expected": 6
    },
    {
      "name": "case_08_edge_single_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -3
            ]
          }
        ]
      },
      "expected": -3
    },
    {
      "name": "case_09_edge_ignore_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              -1
            ]
          }
        ]
      },
      "expected": 2
    },
    {
      "name": "case_10_edge_all_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -2,
              -1
            ]
          }
        ]
      },
      "expected": -1
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -10,
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
      "expected": 42
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              3
            ]
          }
        ]
      },
      "expected": 6
    },
    {
      "name": "case_13_edge_single_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -3
            ]
          }
        ]
      },
      "expected": -3
    },
    {
      "name": "case_14_edge_ignore_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              -1
            ]
          }
        ]
      },
      "expected": 2
    },
    {
      "name": "case_15_edge_all_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -2,
              -1
            ]
          }
        ]
      },
      "expected": -1
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -10,
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
      "expected": 42
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
              3
            ]
          }
        ]
      },
      "expected": 6
    },
    {
      "name": "case_18_edge_single_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -3
            ]
          }
        ]
      },
      "expected": -3
    },
    {
      "name": "case_19_edge_ignore_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              -1
            ]
          }
        ]
      },
      "expected": 2
    },
    {
      "name": "case_20_edge_all_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -2,
              -1
            ]
          }
        ]
      },
      "expected": -1
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -10,
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
      "expected": 42
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              3
            ]
          }
        ]
      },
      "expected": 6
    },
    {
      "name": "case_23_edge_single_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -3
            ]
          }
        ]
      },
      "expected": -3
    },
    {
      "name": "case_24_edge_ignore_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              -1
            ]
          }
        ]
      },
      "expected": 2
    },
    {
      "name": "case_25_edge_all_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -2,
              -1
            ]
          }
        ]
      },
      "expected": -1
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -10,
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
      "expected": 42
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              3
            ]
          }
        ]
      },
      "expected": 6
    },
    {
      "name": "case_28_edge_single_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -3
            ]
          }
        ]
      },
      "expected": -3
    },
    {
      "name": "case_29_edge_ignore_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              -1
            ]
          }
        ]
      },
      "expected": 2
    },
    {
      "name": "case_30_edge_all_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -2,
              -1
            ]
          }
        ]
      },
      "expected": -1
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -10,
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
      "expected": 42
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              3
            ]
          }
        ]
      },
      "expected": 6
    },
    {
      "name": "case_33_edge_single_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -3
            ]
          }
        ]
      },
      "expected": -3
    },
    {
      "name": "case_34_edge_ignore_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              -1
            ]
          }
        ]
      },
      "expected": 2
    },
    {
      "name": "case_35_edge_all_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -2,
              -1
            ]
          }
        ]
      },
      "expected": -1
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -10,
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
      "expected": 42
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
              3
            ]
          }
        ]
      },
      "expected": 6
    },
    {
      "name": "case_38_edge_single_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -3
            ]
          }
        ]
      },
      "expected": -3
    },
    {
      "name": "case_39_edge_ignore_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              -1
            ]
          }
        ]
      },
      "expected": 2
    },
    {
      "name": "case_40_edge_all_negative",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              -2,
              -1
            ]
          }
        ]
      },
      "expected": -1
    }
  ]
}
```
