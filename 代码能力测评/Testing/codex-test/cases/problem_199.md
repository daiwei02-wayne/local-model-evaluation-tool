# 题目199 二叉树的右视图

来源：LeetCode 热题 100（https://leetcode.cn/studyplan/top-100-liked/）

```json
{
  "id": 199,
  "title": "二叉树的右视图",
  "difficulty": "中等",
  "method": "question_199",
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
              null,
              5,
              null,
              4
            ]
          }
        ]
      },
      "expected": [
        1,
        3,
        4
      ]
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              null,
              3
            ]
          }
        ]
      },
      "expected": [
        1,
        3
      ]
    },
    {
      "name": "case_03_base",
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_05_edge_left_only",
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
        2,
        3
      ]
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
              3,
              null,
              5,
              null,
              4
            ]
          }
        ]
      },
      "expected": [
        1,
        3,
        4
      ]
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              null,
              3
            ]
          }
        ]
      },
      "expected": [
        1,
        3
      ]
    },
    {
      "name": "case_08_base",
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_10_edge_left_only",
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
        2,
        3
      ]
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
              3,
              null,
              5,
              null,
              4
            ]
          }
        ]
      },
      "expected": [
        1,
        3,
        4
      ]
    },
    {
      "name": "case_12_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              null,
              3
            ]
          }
        ]
      },
      "expected": [
        1,
        3
      ]
    },
    {
      "name": "case_13_base",
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_15_edge_left_only",
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
        2,
        3
      ]
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
              3,
              null,
              5,
              null,
              4
            ]
          }
        ]
      },
      "expected": [
        1,
        3,
        4
      ]
    },
    {
      "name": "case_17_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              null,
              3
            ]
          }
        ]
      },
      "expected": [
        1,
        3
      ]
    },
    {
      "name": "case_18_base",
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
        1
      ]
    },
    {
      "name": "case_20_edge_left_only",
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
        2,
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
              1,
              2,
              3,
              null,
              5,
              null,
              4
            ]
          }
        ]
      },
      "expected": [
        1,
        3,
        4
      ]
    },
    {
      "name": "case_22_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              null,
              3
            ]
          }
        ]
      },
      "expected": [
        1,
        3
      ]
    },
    {
      "name": "case_23_base",
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_25_edge_left_only",
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
        2,
        3
      ]
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
              3,
              null,
              5,
              null,
              4
            ]
          }
        ]
      },
      "expected": [
        1,
        3,
        4
      ]
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              null,
              3
            ]
          }
        ]
      },
      "expected": [
        1,
        3
      ]
    },
    {
      "name": "case_28_base",
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_30_edge_left_only",
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
        2,
        3
      ]
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
              3,
              null,
              5,
              null,
              4
            ]
          }
        ]
      },
      "expected": [
        1,
        3,
        4
      ]
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              null,
              3
            ]
          }
        ]
      },
      "expected": [
        1,
        3
      ]
    },
    {
      "name": "case_33_base",
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
      "expected": [
        1
      ]
    },
    {
      "name": "case_35_edge_left_only",
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
        2,
        3
      ]
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
              3,
              null,
              5,
              null,
              4
            ]
          }
        ]
      },
      "expected": [
        1,
        3,
        4
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          {
            "__type__": "TreeNode",
            "value": [
              1,
              null,
              3
            ]
          }
        ]
      },
      "expected": [
        1,
        3
      ]
    },
    {
      "name": "case_38_base",
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
        1
      ]
    },
    {
      "name": "case_40_edge_left_only",
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
        2,
        3
      ]
    }
  ]
}
```
