# 题目101 对称二叉树

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个二叉树的根节点 `root` ， 检查它是否轴对称。
示例 1：
题目配图：
输入：root = [1,2,2,3,4,4,3]输出：true
示例 2：
题目配图：
输入：root = [1,2,2,null,3,null,3]输出：false
提示：
树中节点数目在范围 `[1, 1000]` 内
`-100 <= Node.val <= 100`
进阶：你可以运用递归和迭代两种方法解决这个问题吗？

```json
{
  "id": 101,
  "title": "对称二叉树",
  "difficulty": "简单",
  "method": "question_101",
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
              2,
              3,
              4,
              4,
              3
            ]
          }
        ]
      },
      "expected": true
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
              2,
              null,
              3,
              null,
              3
            ]
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_03_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": []
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_04_edge_single",
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
      "expected": true
    },
    {
      "name": "case_05_edge_symmetric_shape",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              2,
              3,
              null,
              null,
              3
            ]
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              2,
              3,
              4,
              4,
              3
            ]
          }
        ]
      },
      "expected": true
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
              2,
              null,
              3,
              null,
              3
            ]
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_08_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": []
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_09_edge_single",
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
      "expected": true
    },
    {
      "name": "case_10_edge_symmetric_shape",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              2,
              3,
              null,
              null,
              3
            ]
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              2,
              3,
              4,
              4,
              3
            ]
          }
        ]
      },
      "expected": true
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
              2,
              null,
              3,
              null,
              3
            ]
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_13_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": []
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_14_edge_single",
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
      "expected": true
    },
    {
      "name": "case_15_edge_symmetric_shape",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              2,
              3,
              null,
              null,
              3
            ]
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              2,
              3,
              4,
              4,
              3
            ]
          }
        ]
      },
      "expected": true
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
              2,
              null,
              3,
              null,
              3
            ]
          }
        ]
      },
      "expected": false
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
      "expected": true
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
      "expected": true
    },
    {
      "name": "case_20_edge_symmetric_shape",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              2,
              3,
              null,
              null,
              3
            ]
          }
        ]
      },
      "expected": true
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
              2,
              3,
              4,
              4,
              3
            ]
          }
        ]
      },
      "expected": true
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
              2,
              null,
              3,
              null,
              3
            ]
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_23_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": []
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_24_edge_single",
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
      "expected": true
    },
    {
      "name": "case_25_edge_symmetric_shape",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              2,
              3,
              null,
              null,
              3
            ]
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              2,
              3,
              4,
              4,
              3
            ]
          }
        ]
      },
      "expected": true
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
              2,
              null,
              3,
              null,
              3
            ]
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_28_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": []
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_29_edge_single",
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
      "expected": true
    },
    {
      "name": "case_30_edge_symmetric_shape",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              2,
              3,
              null,
              null,
              3
            ]
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              2,
              3,
              4,
              4,
              3
            ]
          }
        ]
      },
      "expected": true
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
              2,
              null,
              3,
              null,
              3
            ]
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_33_edge_empty",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": []
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_34_edge_single",
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
      "expected": true
    },
    {
      "name": "case_35_edge_symmetric_shape",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              2,
              3,
              null,
              null,
              3
            ]
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              2,
              3,
              4,
              4,
              3
            ]
          }
        ]
      },
      "expected": true
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
              2,
              null,
              3,
              null,
              3
            ]
          }
        ]
      },
      "expected": false
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
      "expected": true
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
      "expected": true
    },
    {
      "name": "case_40_edge_symmetric_shape",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              2,
              3,
              null,
              null,
              3
            ]
          }
        ]
      },
      "expected": true
    }
  ]
}
```
