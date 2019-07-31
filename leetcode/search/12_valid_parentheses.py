class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map = {"(":")","[":"]","{":"}"}
        stack = []
        for token in s:
            if token in map:
                stack.append(token)
            else:
                # if len(stack) == 0
                # we have more right parentheses
                if len(stack) == 0 or token != map[stack.pop()]: return False
        
        
        # if len(stack) > 0 we have more left parentheses
        return len(stack) == 0