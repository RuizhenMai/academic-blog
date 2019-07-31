# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode

        all codes can be thought of using:
        [1,2,3,4,5]
        2
        4
        """
        if head == None:
            return None
        
        cnt = n-m
        startsAtOne = True if m == 1 else False
        dummy = head
        placeholderBF = None # to pick up the reversed head at m
        while m > 1:
            if m == 2: # only when we are not reversing at m = 1 we do pick up
                placeholderBF = head 
                
            head = head.next
                
            m-=1
        
        prev = curr = head 
        curr = curr.next
        placeholder = prev # to pick up the reversed tail at n
        
        while cnt > 0:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            
            if cnt == 1:
                placeholder.next = curr
            
            cnt -= 1
        if placeholderBF and placeholderBF != prev:
             # if there's one node
             # then prev == placeholderBF
             # then it will result in cycle
            placeholderBF.next = prev
            
        if startsAtOne: 
            # when reverse starts at m=1, dummy becomes the tail,
            # so we return prev as regular reverse linkedlist does
            return prev
        
        return dummy