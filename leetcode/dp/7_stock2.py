class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        DP, convert this to max subarray problem, this can be further reduced
        to one pass
        """
        

        profit = [prices[i] - prices[i-1] for i in range(1,len(prices))]
        
        ans = 0
        for p in profit:
            if p > 0:
                ans += p
        
        return ans
        