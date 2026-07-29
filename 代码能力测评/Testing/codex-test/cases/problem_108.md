# 题目108 将有序数组转换为二叉搜索树

来源：LeetCode 热题 100（https://leetcode.cn/studyplan/top-100-liked/）

```json
{
  "id": 108,
  "title": "将有序数组转换为二叉搜索树",
  "difficulty": "简单",
  "method": "question_108",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          [
            -10,
            -3,
            0,
            5,
            9
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          0,
          -10,
          5,
          null,
          -3,
          null,
          9
        ]
      }
    },
    {
      "name": "case_02_base",
      "input": {
        "args": [
          [
            1,
            3
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          1,
          null,
          3
        ]
      }
    },
    {
      "name": "case_03_base",
      "input": {
        "args": [
          []
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": []
      }
    },
    {
      "name": "case_04_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": null
    },
    {
      "name": "case_05_edge_single",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_06_edge_odd_len",
      "input": {
        "args": [
          [
            -3,
            -2,
            -1,
            0,
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        0,
        -2,
        2,
        -3,
        -1,
        1,
        3
      ]
    },
    {
      "name": "case_07_base",
      "input": {
        "args": [
          [
            -10,
            -3,
            0,
            5,
            9
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          0,
          -10,
          5,
          null,
          -3,
          null,
          9
        ]
      }
    },
    {
      "name": "case_08_base",
      "input": {
        "args": [
          [
            1,
            3
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          1,
          null,
          3
        ]
      }
    },
    {
      "name": "case_09_base",
      "input": {
        "args": [
          []
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": []
      }
    },
    {
      "name": "case_10_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": null
    },
    {
      "name": "case_11_edge_single",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_12_edge_odd_len",
      "input": {
        "args": [
          [
            -3,
            -2,
            -1,
            0,
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        0,
        -2,
        2,
        -3,
        -1,
        1,
        3
      ]
    },
    {
      "name": "case_13_base",
      "input": {
        "args": [
          [
            -10,
            -3,
            0,
            5,
            9
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          0,
          -10,
          5,
          null,
          -3,
          null,
          9
        ]
      }
    },
    {
      "name": "case_14_base",
      "input": {
        "args": [
          [
            1,
            3
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          1,
          null,
          3
        ]
      }
    },
    {
      "name": "case_15_base",
      "input": {
        "args": [
          []
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": []
      }
    },
    {
      "name": "case_16_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": null
    },
    {
      "name": "case_17_edge_single",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_18_edge_odd_len",
      "input": {
        "args": [
          [
            -3,
            -2,
            -1,
            0,
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        0,
        -2,
        2,
        -3,
        -1,
        1,
        3
      ]
    },
    {
      "name": "case_19_base",
      "input": {
        "args": [
          [
            -10,
            -3,
            0,
            5,
            9
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          0,
          -10,
          5,
          null,
          -3,
          null,
          9
        ]
      }
    },
    {
      "name": "case_20_base",
      "input": {
        "args": [
          [
            1,
            3
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          1,
          null,
          3
        ]
      }
    },
    {
      "name": "case_21_base",
      "input": {
        "args": [
          []
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": []
      }
    },
    {
      "name": "case_22_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": null
    },
    {
      "name": "case_23_edge_single",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_24_edge_odd_len",
      "input": {
        "args": [
          [
            -3,
            -2,
            -1,
            0,
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        0,
        -2,
        2,
        -3,
        -1,
        1,
        3
      ]
    },
    {
      "name": "case_25_base",
      "input": {
        "args": [
          [
            -10,
            -3,
            0,
            5,
            9
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          0,
          -10,
          5,
          null,
          -3,
          null,
          9
        ]
      }
    },
    {
      "name": "case_26_base",
      "input": {
        "args": [
          [
            1,
            3
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          1,
          null,
          3
        ]
      }
    },
    {
      "name": "case_27_base",
      "input": {
        "args": [
          []
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": []
      }
    },
    {
      "name": "case_28_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": null
    },
    {
      "name": "case_29_edge_single",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_30_edge_odd_len",
      "input": {
        "args": [
          [
            -3,
            -2,
            -1,
            0,
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        0,
        -2,
        2,
        -3,
        -1,
        1,
        3
      ]
    },
    {
      "name": "case_31_base",
      "input": {
        "args": [
          [
            -10,
            -3,
            0,
            5,
            9
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          0,
          -10,
          5,
          null,
          -3,
          null,
          9
        ]
      }
    },
    {
      "name": "case_32_base",
      "input": {
        "args": [
          [
            1,
            3
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          1,
          null,
          3
        ]
      }
    },
    {
      "name": "case_33_base",
      "input": {
        "args": [
          []
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": []
      }
    },
    {
      "name": "case_34_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": null
    },
    {
      "name": "case_35_edge_single",
      "input": {
        "args": [
          [
            1
          ]
        ]
      },
      "expected": [
        1
      ]
    },
    {
      "name": "case_36_edge_odd_len",
      "input": {
        "args": [
          [
            -3,
            -2,
            -1,
            0,
            1,
            2,
            3
          ]
        ]
      },
      "expected": [
        0,
        -2,
        2,
        -3,
        -1,
        1,
        3
      ]
    },
    {
      "name": "case_37_base",
      "input": {
        "args": [
          [
            -10,
            -3,
            0,
            5,
            9
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          0,
          -10,
          5,
          null,
          -3,
          null,
          9
        ]
      }
    },
    {
      "name": "case_38_base",
      "input": {
        "args": [
          [
            1,
            3
          ]
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": [
          1,
          null,
          3
        ]
      }
    },
    {
      "name": "case_39_base",
      "input": {
        "args": [
          []
        ]
      },
      "expected": {
        "__type__": "TreeNode",
        "value": []
      }
    },
    {
      "name": "case_40_edge_empty",
      "input": {
        "args": [
          []
        ]
      },
      "expected": null
    }
  ]
}
```
