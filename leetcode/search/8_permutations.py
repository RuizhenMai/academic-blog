class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        
        DFS, reference: https://www.youtube.com/watch?v=zIY2BWdsbFs
        Time: O(n*n!): https://github.com/Deadbeef-ECE/Interview/blob/master/Leetcode/BackTracking/046_Permutations.java
        """
        def dfs(nums, d, used, cur, ans):
            """
            used (array of int): used positions of nums; this is replaced from "s" starting position in combination's dfs
            """
            if d == len(nums):
                ans.append(cur[:]) # this is O(n)
            
            for i in range(len(nums)):
                if used[i] == 1: continue
                used[i] = 1
                cur.append(nums[i])
                dfs(nums, d+1, used, cur, ans)
                used[i] = 0
                cur.pop()
            
        
        ans = []
        dfs(nums, 0, [0]*len(nums), [], ans)
        return ans
                    
