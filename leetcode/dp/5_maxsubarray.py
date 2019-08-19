class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        DP
        O(n) Space
        """
        # m[i] := maximum subarray's sum until position i
        # m[i] := m[i-1] > 0 ? nums[i] + m[i-1] : nums[i]
        # since if the subarray before i is negative 
        # then we have no need add m[i-1]
        
        m = [0] * len(nums)
        # at position 0
        # we have no choice
        m[0] = nums[0]
        for i in range(1,len(nums)):
            m[i] = max(nums[i] + m[i-1], nums[i])
        
        return max(m)

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        DP
        O(1) Space
        """
        # m := maximum sum of subarray until position i
        # ans := maximum sum over entire array
        m = nums[0]
        ans = nums[0]

        for i in range(1,len(nums)):
            m = max(nums[i] + m, nums[i])
            if m > ans: ans = m
        
        return ans