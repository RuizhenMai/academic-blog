---
layout: post
title: Linked List
---
<span class = "newthought">This page</span> contains question about the linked list interview quesions

```python
def array2List(arr):
    head = dummy = ListNode(None)
    for e in arr:
        head.next = ListNode(e)
        head = head.next
    
    return dummy.next
```

1. 2-addTwoNumber
2. 445-addTwoNumberII
3. 24-Swap Nodes in Pair
4. 141-Linked List Cycle
5. 142-Linked List CycleII
6. 206-Reverse Linked List 
7. 92-Reversed Linked ListII