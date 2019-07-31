class Solution(object):
    def naive_detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        O(n) space complexity
        same as Linked List Cycle I solution
        """
        visited = {}
        pos = 0
        
        while head is not None:
            if head in visited:
                return head
            
            visited[head] = pos
            # print(pos)
            pos+=1
            head = head.next
        
        return None
    
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        reference: https://leetcode.com/problems/linked-list-cycle-ii/discuss/332344/Python-Floyd-Tortoise-Hare-detail-explanation-with-math-equation
        """
        fast = slow = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        
        if fast == None or fast.next == None:
            return None
        
        slow2 = head
        while slow2 != slow:
            slow2 = slow2.next
            slow = slow.next
        
        return slow2
        
       