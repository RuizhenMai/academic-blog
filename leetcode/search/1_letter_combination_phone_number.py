class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        
        BFS: time: O(4^n), space: O(4^n * 2) since we have a temp on 18, its asymptotic length is 
        also O(4^n) in the final round 
        reference: https://www.youtube.com/watch?v=fLy8t33M1qQ
        """
        if len(digits) == 0:
            return []
    
        # a map mapping from digits to its char output
        d = ["", "", "abc","def","ghi","jkl","mno",
             "pqrs","tuv","wxyz"]
        
        ans = [""] # note ans is not empty 
        for digit in digits:
            temp = []
            for s in ans: # s implies string, 
                for c in d[int(digit)]:# c implies this can only be char
                    temp.append(s + c)
            
            ans = temp # since temp include newly added chars
        
        
        return ans 

    def letterCombinationsDFS(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        
        DFS, Time O(4^n), Space O(4^n + n)
        reference: https://www.youtube.com/watch?v=fLy8t33M1qQ
        """
        if len(digits) == 0:
            return []
    
        # a map mapping from digits to its char output
        d = ["", "", "abc","def","ghi","jkl","mno",
             "pqrs","tuv","wxyz"]
        
        def dfs(digits, d, length, cur, ans):
            '''
            digits - digits given by the question
            d      - the map 
            length (int)            - length of  already added string; also represent the depth of recursion
            cur (array of char)     - 
            ans (array of strings)  - for lastly append one solution like ('ab')
            '''
            if length == len(digits):
                ans.append("".join(cur))
                return
            
            for c in d[int(digits[length])]:
                cur[length] = c
                dfs(digits, d, length+1, cur, ans)
                # we're supposed to pop out what's in cur,
                # which acts like a stack, after dfs,
                # but we just overwrite it 
                
        cur = ["" for _ in range(len(digits))]
        ans = []
        dfs(digits, d, 0, cur, ans)
        
        return ans