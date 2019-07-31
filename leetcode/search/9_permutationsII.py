class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Of course this can also be solved by deleting duplicates with set
        """
        def dfs(nums, d, used, cur, ans):
            if d == len(nums):
                ans.append(cur[:])
                return
            
            for i in range(len(nums)):
                if used[i] == 1: continue
                # 判断 not used[i-1] 是因为例如，我们碰到的第一个1，
                # 即便他的位置不是0，nums[i-1] == nums[i] 是肯定不对
                # 的，第三个条件也不对，所以可以过
                # 但是碰到的第二个或者后续的1就不能过，因为当cur
                # 跑完之后，前面的1又会被设置成used[i] = 0
                
                # 相反，如果是判断 used[i-1] == 1也能过，因为这个
                # condition会在开始了1的第一层递归后，在第二层递归
                # 永远是false，如果后续有1（相同的数）的话
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]: continue
                used[i] = 1
                cur.append(nums[i])
                dfs(nums, d+1, used, cur,ans)
                cur.pop()
                used[i] = 0
            
        
        ans = []
        dfs(sorted(nums), 0, [0]*len(nums), [],ans)
        return ans