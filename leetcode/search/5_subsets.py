class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Time: 
        T(n) = 0 * C(n,0) + 1 * C(n,1) + ... + n * C(n,n) the constant comes from multiplying
        and we know C(n,k) = C(n,n-k), thus
        T(n) = 0 * C(n,n) + 1 * C(n,n-1) +... + n * C(n,n), adding these two equation 
        2T(n) = n * C(n,n) + n * C(n,n-1) +... 
        = n 2^n 
        T(n) = n/2 2^n = O(n*2^n)

        Space: O(n)
        """
        def dfs(nums, d, k, s, cur, ans):
            if d == k:
                ans.append(cur[:]) # this is O(n) at worst 
                return
            
            for i in range(s, len(nums)):
                cur.append(nums[i])
                dfs(nums, d+1, k, i+1,cur,ans)
                cur.pop()
            
        
        cur = []
        ans = []
        for i in range(0,len(nums)+1):
            dfs(nums, 0, i, 0, cur,ans)
        
        return ans