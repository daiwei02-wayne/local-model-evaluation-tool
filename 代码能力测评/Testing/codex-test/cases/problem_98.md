# 题目98 验证二叉搜索树

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个二叉树的根节点 `root` ，判断其是否是一个有效的二叉搜索树。
有效 二叉搜索树定义如下：
节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1：
题目配图：
输入：root = [2,1,3]输出：true
示例 2：
题目配图：
输入：root = [5,1,4,null,null,3,6]输出：false解释：根节点的值是 5 ，但是右子节点的值是 4 。
提示：
树中节点数目范围在[1, 10<sup>4</sup>] 内
-2<sup>31</sup> <= Node.val <= 2<sup>31</sup> - 1

```json
{
  "id": 98,
  "title": "验证二叉搜索树",
  "difficulty": "中等",
  "method": "question_98",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              1,
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
              5,
              1,
              4,
              null,
              null,
              3,
              6
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
      "name": "case_04_edge_duplicate_invalid",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              1
            ]
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_05_edge_all_duplicate",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              2,
              2
            ]
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              1,
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
              5,
              1,
              4,
              null,
              null,
              3,
              6
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
      "name": "case_09_edge_duplicate_invalid",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              1
            ]
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_10_edge_all_duplicate",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              2,
              2
            ]
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_11_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              1,
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
              5,
              1,
              4,
              null,
              null,
              3,
              6
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
      "name": "case_14_edge_duplicate_invalid",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              1
            ]
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_15_edge_all_duplicate",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              2,
              2
            ]
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_16_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              1,
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
              5,
              1,
              4,
              null,
              null,
              3,
              6
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
      "name": "case_19_edge_duplicate_invalid",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              1
            ]
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_20_edge_all_duplicate",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              2,
              2
            ]
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              1,
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
              5,
              1,
              4,
              null,
              null,
              3,
              6
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
      "name": "case_24_edge_duplicate_invalid",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              1
            ]
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_25_edge_all_duplicate",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              2,
              2
            ]
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              1,
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
              5,
              1,
              4,
              null,
              null,
              3,
              6
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
      "name": "case_29_edge_duplicate_invalid",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              1
            ]
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_30_edge_all_duplicate",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              2,
              2
            ]
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              1,
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
              5,
              1,
              4,
              null,
              null,
              3,
              6
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
      "name": "case_34_edge_duplicate_invalid",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              1
            ]
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_35_edge_all_duplicate",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              2,
              2
            ]
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_36_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              1,
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
              5,
              1,
              4,
              null,
              null,
              3,
              6
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
      "name": "case_39_edge_duplicate_invalid",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              1
            ]
          }
        ]
      },
      "expected": false
    },
    {
      "name": "case_40_edge_all_duplicate",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              2,
              2,
              2
            ]
          }
        ]
      },
      "expected": false
    }
  ]
}
```
