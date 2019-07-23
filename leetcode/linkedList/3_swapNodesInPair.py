# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(None)
        dummy.next = head.next # it will just be the head
        while head is not None and head.next is not None:
            prev = head
            head = head.next
            nextNode = head.next # store next head to be swapped
            
            print(prev.val,head.val)
            # start swapping
            head.next = prev            
            prev.next = nextNode 
            
            # prev.next is the next next one, because
            # the next next will be swapped to prior one
            # eventually 
            if nextNode and nextNode.next:
                prev.next = nextNode.next
            
            print('after swapped',head.next.val) 
            head = nextNode # move to the next head
            
        return dummy.next