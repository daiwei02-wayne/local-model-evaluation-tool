# 题目102 二叉树的层序遍历

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你二叉树的根节点 `root` ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
示例 1：
题目配图：
输入：root = [3,9,20,null,null,15,7]输出：[[3],[9,20],[15,7]]
示例 2：
输入：root = [1]输出：[[1]]
示例 3：
输入：root = []输出：[]
提示：
树中节点数目在范围 `[0, 2000]` 内
`-1000 <= Node.val <= 1000`

```json
{
  "id": 102,
  "title": "二叉树的层序遍历",
  "difficulty": "中等",
  "method": "question_102",
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
      "expected": [
        [
          3
        ],
        [
          9,
          20
        ],
        [
          15,
          7
        ]
      ]
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
      "expected": []
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
        [
          1
        ]
      ]
    },
    {
      "name": "case_04_edge_sparse",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              3,
              4,
              null,
              null,
              5
            ]
          }
        ]
      },
      "expected": [
        [
          1
        ],
        [
          2,
          3
        ],
        [
          4,
          5
        ]
      ]
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
      "expected": [
        [
          3
        ],
        [
          9,
          20
        ],
        [
          15,
          7
        ]
      ]
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
      "expected": []
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
        [
          1
        ]
      ]
    },
    {
      "name": "case_08_edge_sparse",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              3,
              4,
              null,
              null,
              5
            ]
          }
        ]
      },
      "expected": [
        [
          1
        ],
        [
          2,
          3
        ],
        [
          4,
          5
        ]
      ]
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
      "expected": [
        [
          3
        ],
        [
          9,
          20
        ],
        [
          15,
          7
        ]
      ]
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
      "expected": []
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
        [
          1
        ]
      ]
    },
    {
      "name": "case_12_edge_sparse",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              3,
              4,
              null,
              null,
              5
            ]
          }
        ]
      },
      "expected": [
        [
          1
        ],
        [
          2,
          3
        ],
        [
          4,
          5
        ]
      ]
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
      "expected": [
        [
          3
        ],
        [
          9,
          20
        ],
        [
          15,
          7
        ]
      ]
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
      "expected": []
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
        [
          1
        ]
      ]
    },
    {
      "name": "case_16_edge_sparse",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              3,
              4,
              null,
              null,
              5
            ]
          }
        ]
      },
      "expected": [
        [
          1
        ],
        [
          2,
          3
        ],
        [
          4,
          5
        ]
      ]
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
      "expected": [
        [
          3
        ],
        [
          9,
          20
        ],
        [
          15,
          7
        ]
      ]
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
      "expected": []
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
        [
          1
        ]
      ]
    },
    {
      "name": "case_20_edge_sparse",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              3,
              4,
              null,
              null,
              5
            ]
          }
        ]
      },
      "expected": [
        [
          1
        ],
        [
          2,
          3
        ],
        [
          4,
          5
        ]
      ]
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
      "expected": [
        [
          3
        ],
        [
          9,
          20
        ],
        [
          15,
          7
        ]
      ]
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
      "expected": []
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
        [
          1
        ]
      ]
    },
    {
      "name": "case_24_edge_sparse",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              3,
              4,
              null,
              null,
              5
            ]
          }
        ]
      },
      "expected": [
        [
          1
        ],
        [
          2,
          3
        ],
        [
          4,
          5
        ]
      ]
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
      "expected": [
        [
          3
        ],
        [
          9,
          20
        ],
        [
          15,
          7
        ]
      ]
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
      "expected": []
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
        [
          1
        ]
      ]
    },
    {
      "name": "case_28_edge_sparse",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              3,
              4,
              null,
              null,
              5
            ]
          }
        ]
      },
      "expected": [
        [
          1
        ],
        [
          2,
          3
        ],
        [
          4,
          5
        ]
      ]
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
      "expected": [
        [
          3
        ],
        [
          9,
          20
        ],
        [
          15,
          7
        ]
      ]
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
      "expected": []
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
        [
          1
        ]
      ]
    },
    {
      "name": "case_32_edge_sparse",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              3,
              4,
              null,
              null,
              5
            ]
          }
        ]
      },
      "expected": [
        [
          1
        ],
        [
          2,
          3
        ],
        [
          4,
          5
        ]
      ]
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
      "expected": [
        [
          3
        ],
        [
          9,
          20
        ],
        [
          15,
          7
        ]
      ]
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
      "expected": []
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
        [
          1
        ]
      ]
    },
    {
      "name": "case_36_edge_sparse",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              3,
              4,
              null,
              null,
              5
            ]
          }
        ]
      },
      "expected": [
        [
          1
        ],
        [
          2,
          3
        ],
        [
          4,
          5
        ]
      ]
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
      "expected": [
        [
          3
        ],
        [
          9,
          20
        ],
        [
          15,
          7
        ]
      ]
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
      "expected": []
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
        [
          1
        ]
      ]
    },
    {
      "name": "case_40_edge_sparse",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              2,
              3,
              4,
              null,
              null,
              5
            ]
          }
        ]
      },
      "expected": [
        [
          1
        ],
        [
          2,
          3
        ],
        [
          4,
          5
        ]
      ]
    }
  ]
}
```
