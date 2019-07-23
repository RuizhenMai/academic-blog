# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first = l1 
        second = l2
        carry = 0 # the next digit 
        dummy = curr = ListNode(None) # in python, storer of object it's like a pointer
        # dummy = curr
        while first is not None or second is not None:
            
            currSum = carry
            currSum += first.val if first else 0 
            currSum += second.val if second else 0
            # clear the next digit
            carry = 0
            if currSum >= 10:
                carry = currSum // 10
                currSum = currSum % 10
            
            first = first.next if first else None
            second = second.next if second else None
            curr.next = ListNode(currSum) # do not reassign curr, we will not be able to return dummy.next
            curr = curr.next

        if carry > 0:
            curr.next = ListNode(carry)
        
        return dummy.next