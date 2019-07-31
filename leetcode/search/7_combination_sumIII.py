class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1,10)]
        def dfs(nums, d, k, s, cur, ans):
            if d == k:
                if sum(cur) == n:
                    ans.append(cur[:])
                return 
                
            for i in range(s, len(nums)):
                cur.append(nums[i])
                dfs(nums, d+1, k, i+1, cur, ans)
                cur.pop()
            
        
        ans = []
        dfs(nums, 0, k, 0, [], ans)
        return ans