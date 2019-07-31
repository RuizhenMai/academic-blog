# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def array2List(arr):
    head = dummy = ListNode(None)
    for e in arr:
        head.next = ListNode(e)
        head = head.next
    
    return dummy.next

class Solution(object):
    def naive_reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        while head is not None:
            stack.append(head)
            head = head.next
        

        res = dummy = ListNode(None)
        while len(stack) > 0:
            res.next = stack.pop()
            res = res.next
        
        res.next = None # otherwise 1->2 2->1, the last node is first in the original linked 
        return dummy.next

    def recur_reverseList(self,head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        p = self.reverseList(head.next) # only for returning the last node, every recursion doesn't modify this variable
        head.next.next = head
        head.next = None
        
        
        return p


    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """        
        if head == None: #edge case
            return None
        
        
        prev = curr = head
        curr = curr.next # clear the first next 
        prev.next = None
        while curr != None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev
        
        
# lst = array2List([1,2,3,4,5])
# print(Solution().naive_reverseList(lst).val)
    