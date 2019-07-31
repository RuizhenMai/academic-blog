
class Solution(object):
    def naive_hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool

        O(n) space complexity
        """
        visited = {}
        while head is not None:
            if head in visited:
                return True
            
            visited[head] = 1
            head = head.next
        
        return False

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool

        proof: https://stackoverflow.com/questions/3952805/proof-of-detecting-the-start-of-cycle-in-linked-list
        """
        faster = slow = head
        while faster != None and faster.next != None:
            faster = faster.next.next
            slow = slow.next
            if faster == slow:
                return True
        
        return False