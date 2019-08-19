class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        DP O(n) space, can be reduced to O(1)
        """
        
        # L[i] := lowest price up to the i-th day
        # L[i] = min(prices[i], L[i-1])
        # P[i] := maximum profit up to the i-th day
        # P[i] = max(prices[i] - L[i], P[i-1])
        if len(prices) == 0:
            return 0
        
        L = [0] * len(prices)
        P = [0] * len(prices)
        L[0] = prices[0]
        P[0] = 0
        
        for i in range(1,len(prices)):
            L[i] = min(prices[i], L[i-1])
            P[i] = max(prices[i] - L[i], P[i-1])
        
        return max(P) # max(P) == P[-1]

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        DP in terms of max subarray sum
        """
        
        # profit[i] := profit if buy on i-1-th day and sell on i-th day
        # profit[i] = prices[i] - prices[i-1] (*)
        # therefore profit[i+1] + profit[i] = prices[i+1] - prices[i] - (*)
        # => prices[i+1] - prices[i-1]
        # similarly profit[i+2] + profit[i+1] + profit[i] = prices[i+2] - prices[i] 
        # the sum of subarray becomes the profit over days
        
        if len(prices) <= 1:
            return 0
        
        profit = [prices[i] - prices[i-1] for i in range(1,len(prices))]
        
        m = profit[0] # m:= maximum profit up to day i-th
        ans = max(profit[0], 0) # since in fact we can buy and sell on the same day
        
        for i in range(1,len(profit)):
            m = max(profit[i] + m, profit[i])
            if m > ans:
                ans = m
        
        return ans