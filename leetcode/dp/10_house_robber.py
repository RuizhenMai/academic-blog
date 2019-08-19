class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        if Brute Force, then it's O(2^n), each time 
        choose rob or not
        """
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        rob = [0] * len(nums)
        rob[0] = nums[0]
        rob[1] = max(nums[1], nums[0]) # we don't have rob[-1] to consider
        
        for i in range(2,len(nums)):
            rob[i] = max(rob[i-2] + nums[i],rob[i-1])
        
        return rob[-1]