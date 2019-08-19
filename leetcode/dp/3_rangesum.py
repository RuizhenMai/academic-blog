class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        np.cumsum/prefix array
        
        self.nums[i] = nums[0]+...+nums[i-2] + nums[i-1] + nums[i]
        self.nums[i-1] = nums[0] +...+nums[i-2] + nums[i-1] 
        self.nums[i-2] =  nums[0] +...+nums[i-2] 
        """

        self.nums = [0] * len(nums)
        if len(nums) > 0:
            self.nums[0] = nums[0]
            for i in range(1,len(nums)):
                self.nums[i] = self.nums[i-1] + nums[i]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            # in case self.nums[i-1] goes to the last one
            # of array
            return self.nums[j]
        
        # see __init__
        return self.nums[j] - self.nums[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)