# 题目437 路径总和 III

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一个二叉树的根节点 `root` ，和一个整数 `targetSum` ，求该二叉树里节点值之和等于 `targetSum` 的 路径 的数目。
路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
示例 1：
题目配图：
输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8输出：3解释：和等于 8 的路径有 3 条，如图所示。
示例 2：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22输出：3
提示:
二叉树的节点个数的范围是 `[0,1000]`
-10<sup>9</sup> <= Node.val <= 10<sup>9</sup>
`-1000 <= targetSum <= 1000`

```json
{
  "id": 437,
  "title": "路径总和 III",
  "difficulty": "中等",
  "method": "question_437",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              10,
              5,
              -3,
              3,
              2,
              null,
              11,
              3,
              -2,
              null,
              1
            ]
          },
          8
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
          },
          0
        ]
      },
      "expected": 0
    },
    {
      "name": "case_03_edge_single_hit",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1
            ]
          },
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_04_edge_negative_paths",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              -2,
              -3,
              1,
              3,
              -2,
              null,
              -1
            ]
          },
          -1
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
              10,
              5,
              -3,
              3,
              2,
              null,
              11,
              3,
              -2,
              null,
              1
            ]
          },
          8
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
          },
          0
        ]
      },
      "expected": 0
    },
    {
      "name": "case_07_edge_single_hit",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1
            ]
          },
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_08_edge_negative_paths",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              -2,
              -3,
              1,
              3,
              -2,
              null,
              -1
            ]
          },
          -1
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
              10,
              5,
              -3,
              3,
              2,
              null,
              11,
              3,
              -2,
              null,
              1
            ]
          },
          8
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
          },
          0
        ]
      },
      "expected": 0
    },
    {
      "name": "case_11_edge_single_hit",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1
            ]
          },
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_12_edge_negative_paths",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              -2,
              -3,
              1,
              3,
              -2,
              null,
              -1
            ]
          },
          -1
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
              10,
              5,
              -3,
              3,
              2,
              null,
              11,
              3,
              -2,
              null,
              1
            ]
          },
          8
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
          },
          0
        ]
      },
      "expected": 0
    },
    {
      "name": "case_15_edge_single_hit",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1
            ]
          },
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_16_edge_negative_paths",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              -2,
              -3,
              1,
              3,
              -2,
              null,
              -1
            ]
          },
          -1
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
              10,
              5,
              -3,
              3,
              2,
              null,
              11,
              3,
              -2,
              null,
              1
            ]
          },
          8
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
          },
          0
        ]
      },
      "expected": 0
    },
    {
      "name": "case_19_edge_single_hit",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1
            ]
          },
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_20_edge_negative_paths",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              -2,
              -3,
              1,
              3,
              -2,
              null,
              -1
            ]
          },
          -1
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
              10,
              5,
              -3,
              3,
              2,
              null,
              11,
              3,
              -2,
              null,
              1
            ]
          },
          8
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
          },
          0
        ]
      },
      "expected": 0
    },
    {
      "name": "case_23_edge_single_hit",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1
            ]
          },
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_24_edge_negative_paths",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              -2,
              -3,
              1,
              3,
              -2,
              null,
              -1
            ]
          },
          -1
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
              10,
              5,
              -3,
              3,
              2,
              null,
              11,
              3,
              -2,
              null,
              1
            ]
          },
          8
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
          },
          0
        ]
      },
      "expected": 0
    },
    {
      "name": "case_27_edge_single_hit",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1
            ]
          },
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_28_edge_negative_paths",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              -2,
              -3,
              1,
              3,
              -2,
              null,
              -1
            ]
          },
          -1
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
              10,
              5,
              -3,
              3,
              2,
              null,
              11,
              3,
              -2,
              null,
              1
            ]
          },
          8
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
          },
          0
        ]
      },
      "expected": 0
    },
    {
      "name": "case_31_edge_single_hit",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1
            ]
          },
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_32_edge_negative_paths",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              -2,
              -3,
              1,
              3,
              -2,
              null,
              -1
            ]
          },
          -1
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
              10,
              5,
              -3,
              3,
              2,
              null,
              11,
              3,
              -2,
              null,
              1
            ]
          },
          8
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
          },
          0
        ]
      },
      "expected": 0
    },
    {
      "name": "case_35_edge_single_hit",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1
            ]
          },
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_36_edge_negative_paths",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              -2,
              -3,
              1,
              3,
              -2,
              null,
              -1
            ]
          },
          -1
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
              10,
              5,
              -3,
              3,
              2,
              null,
              11,
              3,
              -2,
              null,
              1
            ]
          },
          8
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
          },
          0
        ]
      },
      "expected": 0
    },
    {
      "name": "case_39_edge_single_hit",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1
            ]
          },
          1
        ]
      },
      "expected": 1
    },
    {
      "name": "case_40_edge_negative_paths",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              -2,
              -3,
              1,
              3,
              -2,
              null,
              -1
            ]
          },
          -1
        ]
      },
      "expected": 4
    }
  ]
}
```
