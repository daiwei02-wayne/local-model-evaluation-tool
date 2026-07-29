# 题目234 回文链表

来源文档：LeetCode_HOT100_题目汇总_含Java接口Demo_测试用例统一版.docx

给你一个单链表的头节点 `head` ，请你判断该链表是否为回文链表。如果是，返回 `true` ；否则，返回 `false` 。
示例 1：
题目配图：
输入：head = [1,2,2,1]输出：true
示例 2：
题目配图：
输入：head = [1,2]输出：false
提示：
链表中节点数目在范围[1, 10<sup>5</sup>] 内
`0 <= Node.val <= 9`
进阶：你能否用 `O(n)` 时间复杂度和 `O(1)` 空间复杂度解决此题？

```json
{
  "id": 234,
  "title": "回文链表",
  "difficulty": "简单",
  "method": "question_234",
  "cases": [
    {
      "name": "case_01_base",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              2,
              1
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
            "__type__": "ListNode",
            "value": [
              1,
              2
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
            "__type__": "ListNode",
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
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_05_edge_odd_true",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              2,
              1
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
            "__type__": "ListNode",
            "value": [
              1,
              2,
              2,
              1
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
            "__type__": "ListNode",
            "value": [
              1,
              2
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
            "__type__": "ListNode",
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
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_10_edge_odd_true",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              2,
              1
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
            "__type__": "ListNode",
            "value": [
              1,
              2,
              2,
              1
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
            "__type__": "ListNode",
            "value": [
              1,
              2
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
            "__type__": "ListNode",
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
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_15_edge_odd_true",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              2,
              1
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
            "__type__": "ListNode",
            "value": [
              1,
              2,
              2,
              1
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
            "__type__": "ListNode",
            "value": [
              1,
              2
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
            "__type__": "ListNode",
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
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_20_edge_odd_true",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              2,
              1
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
            "__type__": "ListNode",
            "value": [
              1,
              2,
              2,
              1
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
            "__type__": "ListNode",
            "value": [
              1,
              2
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
            "__type__": "ListNode",
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
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_25_edge_odd_true",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              2,
              1
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
            "__type__": "ListNode",
            "value": [
              1,
              2,
              2,
              1
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
            "__type__": "ListNode",
            "value": [
              1,
              2
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
            "__type__": "ListNode",
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
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_30_edge_odd_true",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              2,
              1
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
            "__type__": "ListNode",
            "value": [
              1,
              2,
              2,
              1
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
            "__type__": "ListNode",
            "value": [
              1,
              2
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
            "__type__": "ListNode",
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
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_35_edge_odd_true",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              2,
              1
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
            "__type__": "ListNode",
            "value": [
              1,
              2,
              2,
              1
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
            "__type__": "ListNode",
            "value": [
              1,
              2
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
            "__type__": "ListNode",
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
            "__type__": "ListNode",
            "value": [
              1
            ]
          }
        ]
      },
      "expected": true
    },
    {
      "name": "case_40_edge_odd_true",
      "input": {
        "args": [
          {
            "__type__": "ListNode",
            "value": [
              1,
              2,
              3,
              2,
              1
            ]
          }
        ]
      },
      "expected": true
    }
  ]
}
```
