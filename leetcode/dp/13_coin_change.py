class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        
        dp, O(amount* len(coins))
        intuitive answer, the one on leetcode may have optimization
        """
        
        # dp[i][j] := minimum value achieved 
        # by using first i items(here is coins) and 
        # exact j weights(here is amounts)
        dp = [float('inf')] * (amount+1)
        dp[0] = 0 # using 0 items we can achieve 0 value 
        N = len(coins)
        coins.insert(0,0)
        for i in range(1, N+1):
            for j in range(coins[i], amount+1):
                # temp = float('inf') if j-coins[i] < 0 else dp[j-coins[i]] + 1
                dp[j] = min(dp[j], dp[j-coins[i]] + 1)
            
        
        # we take the last one because we need to use all 
        # the weights unlike 01knapsack we don't need to use 
        # all the weights
        return dp[amount] if dp[amount] != float('inf') else -1
        