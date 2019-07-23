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
        
        Nothing special, first push every number in l1 and l2 into stack and then perform samething as addTwoNumbersI, but adding nodes to the front 
        """
        stack1 = []
        stack2 = []
        
        while l1 != None: 
            stack1.append(l1.val)
            l1 = l1.next
        
        while l2 != None: 
            # Note we use 2 stack here, if we (may not be able to) use recursion
            # we need to two recursion as well
            stack2.append(l2.val)
            l2 = l2.next
        
        currNode = None 
        carry = 0
        while len(stack1) > 0 or len(stack2) > 0:
            currSum = carry
            currSum += stack1.pop() if len(stack1) > 0 else 0
            currSum += stack2.pop() if len(stack2) > 0 else 0
            
            carry = 0
            if currSum >= 10:
                carry = currSum // 10
                currSum = currSum % 10
                
            # here is different
            # we push_left to the linked list
            # instead of pushing right in addTwoNumbersI
            newNode = ListNode(currSum)
            newNode.next = currNode
            currNode = newNode
        
        if carry > 0:
            newNode = ListNode(carry)
            newNode.next = currNode
            currNode = newNode
        
        return currNode
        