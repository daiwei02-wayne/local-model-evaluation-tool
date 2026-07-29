# 题目236 二叉树的最近公共祖先

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
示例 1：
题目配图：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1输出：3解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
示例 2：
题目配图：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4输出：5解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
示例 3：
输入：root = [1,2], p = 1, q = 2输出：1
提示：
树中节点数目在范围 [2, 10<sup>5</sup>] 内。
-10<sup>9</sup> <= Node.val <= 10<sup>9</sup>
所有 `Node.val` `互不相同` 。
`p != q`
`p` 和 `q` 均存在于给定的二叉树中。

```json
{
  "id": 236,
  "title": "二叉树的最近公共祖先",
  "difficulty": "中等",
  "method": "question_236",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 5
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 1
          }
        ]
      },
      "expected": 3,
      "expectation": {
        "source": "return_node_value"
      }
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 5
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 4
          }
        ]
      },
      "expected": 5,
      "expectation": {
        "source": "return_node_value"
      }
    },
    {
      "name": "case_03_edge_root_lca",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 1
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 2
          }
        ]
      },
      "expectation": {
        "source": "return_node_value"
      },
      "expected": 1
    },
    {
      "name": "case_04_edge_deep_lca",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 7
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 4
          }
        ]
      },
      "expectation": {
        "source": "return_node_value"
      },
      "expected": 2
    },
    {
      "name": "case_05_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 5
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 1
          }
        ]
      },
      "expected": 3,
      "expectation": {
        "source": "return_node_value"
      }
    },
    {
      "name": "case_06_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 5
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 4
          }
        ]
      },
      "expected": 5,
      "expectation": {
        "source": "return_node_value"
      }
    },
    {
      "name": "case_07_edge_root_lca",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 1
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 2
          }
        ]
      },
      "expectation": {
        "source": "return_node_value"
      },
      "expected": 1
    },
    {
      "name": "case_08_edge_deep_lca",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 7
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 4
          }
        ]
      },
      "expectation": {
        "source": "return_node_value"
      },
      "expected": 2
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 5
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 1
          }
        ]
      },
      "expected": 3,
      "expectation": {
        "source": "return_node_value"
      }
    },
    {
      "name": "case_10_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 5
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 4
          }
        ]
      },
      "expected": 5,
      "expectation": {
        "source": "return_node_value"
      }
    },
    {
      "name": "case_11_edge_root_lca",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 1
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 2
          }
        ]
      },
      "expectation": {
        "source": "return_node_value"
      },
      "expected": 1
    },
    {
      "name": "case_12_edge_deep_lca",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 7
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 4
          }
        ]
      },
      "expectation": {
        "source": "return_node_value"
      },
      "expected": 2
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 5
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 1
          }
        ]
      },
      "expected": 3,
      "expectation": {
        "source": "return_node_value"
      }
    },
    {
      "name": "case_14_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 5
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 4
          }
        ]
      },
      "expected": 5,
      "expectation": {
        "source": "return_node_value"
      }
    },
    {
      "name": "case_15_edge_root_lca",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 1
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 2
          }
        ]
      },
      "expectation": {
        "source": "return_node_value"
      },
      "expected": 1
    },
    {
      "name": "case_16_edge_deep_lca",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 7
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 4
          }
        ]
      },
      "expectation": {
        "source": "return_node_value"
      },
      "expected": 2
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 5
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 1
          }
        ]
      },
      "expected": 3,
      "expectation": {
        "source": "return_node_value"
      }
    },
    {
      "name": "case_18_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 5
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 4
          }
        ]
      },
      "expected": 5,
      "expectation": {
        "source": "return_node_value"
      }
    },
    {
      "name": "case_19_edge_root_lca",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 1
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 2
          }
        ]
      },
      "expectation": {
        "source": "return_node_value"
      },
      "expected": 1
    },
    {
      "name": "case_20_edge_deep_lca",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 7
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 4
          }
        ]
      },
      "expectation": {
        "source": "return_node_value"
      },
      "expected": 2
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 5
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 1
          }
        ]
      },
      "expected": 3,
      "expectation": {
        "source": "return_node_value"
      }
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 5
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 4
          }
        ]
      },
      "expected": 5,
      "expectation": {
        "source": "return_node_value"
      }
    },
    {
      "name": "case_23_edge_root_lca",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 1
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 2
          }
        ]
      },
      "expectation": {
        "source": "return_node_value"
      },
      "expected": 1
    },
    {
      "name": "case_24_edge_deep_lca",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 7
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 4
          }
        ]
      },
      "expectation": {
        "source": "return_node_value"
      },
      "expected": 2
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 5
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 1
          }
        ]
      },
      "expected": 3,
      "expectation": {
        "source": "return_node_value"
      }
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 5
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 4
          }
        ]
      },
      "expected": 5,
      "expectation": {
        "source": "return_node_value"
      }
    },
    {
      "name": "case_27_edge_root_lca",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 1
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 2
          }
        ]
      },
      "expectation": {
        "source": "return_node_value"
      },
      "expected": 1
    },
    {
      "name": "case_28_edge_deep_lca",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 7
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 4
          }
        ]
      },
      "expectation": {
        "source": "return_node_value"
      },
      "expected": 2
    },
    {
      "name": "case_29_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 5
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 1
          }
        ]
      },
      "expected": 3,
      "expectation": {
        "source": "return_node_value"
      }
    },
    {
      "name": "case_30_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 5
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 4
          }
        ]
      },
      "expected": 5,
      "expectation": {
        "source": "return_node_value"
      }
    },
    {
      "name": "case_31_edge_root_lca",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 1
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 2
          }
        ]
      },
      "expectation": {
        "source": "return_node_value"
      },
      "expected": 1
    },
    {
      "name": "case_32_edge_deep_lca",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 7
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 4
          }
        ]
      },
      "expectation": {
        "source": "return_node_value"
      },
      "expected": 2
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 5
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 1
          }
        ]
      },
      "expected": 3,
      "expectation": {
        "source": "return_node_value"
      }
    },
    {
      "name": "case_34_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 5
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 4
          }
        ]
      },
      "expected": 5,
      "expectation": {
        "source": "return_node_value"
      }
    },
    {
      "name": "case_35_edge_root_lca",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 1
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 2
          }
        ]
      },
      "expectation": {
        "source": "return_node_value"
      },
      "expected": 1
    },
    {
      "name": "case_36_edge_deep_lca",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 7
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 4
          }
        ]
      },
      "expectation": {
        "source": "return_node_value"
      },
      "expected": 2
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 5
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 1
          }
        ]
      },
      "expected": 3,
      "expectation": {
        "source": "return_node_value"
      }
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 5
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 4
          }
        ]
      },
      "expected": 5,
      "expectation": {
        "source": "return_node_value"
      }
    },
    {
      "name": "case_39_edge_root_lca",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 1
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 2
          }
        ]
      },
      "expectation": {
        "source": "return_node_value"
      },
      "expected": 1
    },
    {
      "name": "case_40_edge_deep_lca",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              3,
              5,
              1,
              6,
              2,
              0,
              8,
              null,
              null,
              7,
              4
            ]
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 7
          },
          {
            "__type__": "TreeNodeRef",
            "tree_arg": 0,
            "value": 4
          }
        ]
      },
      "expectation": {
        "source": "return_node_value"
      },
      "expected": 2
    }
  ]
}
```
