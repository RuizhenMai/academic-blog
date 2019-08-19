class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # hold[i] := maximum cashflow obtained up to i-th day
        # if I buy or hold a stock
        # hold[i] = max(rest[i-1]-prices[i], hold[i-1]) 

        # rest[i] := maximum cashflow obtained up to i-th day
        # if I  sold a stock on i-1 day or do nothing
        # rest[i] = max(sold[i-1], rest[i-1])
        
        # sold[i] := cashflow obtained if I sold a stock, 
        # when I hold it
        # sold[i] = hold[i-1] + prices[i]
        if len(prices) <= 1:
            return 0
        
        hold = [0] * (len(prices)+1)
        rest = [0] * (len(prices)+1)
        sold = [0] * (len(prices)+1)
        
        # because we have never bought a stock
        # the max cashflow for hold at the beginning
        # is `None`
        hold[0] = -float('inf')
        rest[0] = 0
        sold[0] = 0
        
        # this does not intervene with the forloop nor result, just make the indices right
        prices.insert(0,0) 
        for i in range(1,len(prices)):
            hold[i] = max(rest[i-1]-prices[i],hold[i-1])
            # sold[i] is delayed from hold[i-1]
            # selling at i = 0 day is invalid as we don't 
            # hold any stocks at i=-1 day
            sold[i] = hold[i-1]+prices[i] if i > 0 else 0
            # then rest[i] is also delayed from hold[i-1] (proxied by sold[i-1])
            rest[i] = max(sold[i-1], rest[i-1])
        

        return max(sold[-1], rest[-1])