class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, d, k, s, cur, ans):
            if d == k:
                ans.append(cur[:])
                return

            
            for i in range(s,len(nums)):
                cur.append(nums[i])
                dfs(nums, d+1, k, i+1, cur, ans)
                cur.pop()
                
        
        cur, ans = [],[]
        for i in range(0, len(nums)+1):
            # we need to sort otherwise the ans will contain things like
            # [1,4] and [4,1] which not considered duplicate 
            dfs(sorted(nums),0, i, 0, cur, ans)
        
        
        return list(set([tuple(x) for x in ans]))