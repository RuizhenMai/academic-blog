class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        
        # hold[i] := maximum cashflow up to i-th day if hold the stock
        # hold[i] = max(cash[i-1] - prices[i],hold[i-1]) 
        # cash[i] := maximum cashflow if sell the stock holding or do nothing
        # cash[i] = max(cash[i-1], hold[i-1] + prices[i]-fee)
        hold = [0] * (len(prices) + 1)
        cash = [0] * (len(prices) + 1)
        hold[0] = -float('inf')
        
        prices.insert(0,0)
        for i in range(1,len(prices)):
            hold[i] = max(cash[i-1] - prices[i], hold[i-1]) if i > 0 else 0
            cash[i] = max(hold[i-1] + prices[i] - fee, cash[i-1])
        
        # print('hold',hold)
        # print('cash',cash)
        
        return cash[-1]
        