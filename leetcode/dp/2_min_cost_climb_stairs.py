class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        
        Recursion + Memorization
        """
        
        def dp(cost, m, i):
            '''
            dp:= min cost climb to i-step
            '''
            if i <= 1: return 0
            if m[i] > 0: return m[i]
            m[i] = min(dp(cost, m, i-1) + cost[i-1], 
                         dp(cost, m, i-2) + cost[i-2])
            return m[i]
        
        m = [0] * (len(cost)+1)
        return dp(cost, m, len(cost))

    def minCostClimbingStairsDP(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        
        DP, O(n) space
        """
        
        # dp:= min cost to reach i-th step
        # the cost of reaching 0 and 1 step is 0
        dp = [0] * (len(cost)+1) 
        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], 
                        dp[i-2]+cost[i-2])
        
        return dp[len(cost)]

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        
        DP, O(1) space
        """
        
        # dp:= min cost to reach i-th step
        # the cost of reaching 0 and 1 step is 0

        if len(cost) <= 1:
            return 0
        
        dpmn2 = 0
        dpmn1 = 0
        dp = 0
        for i in range(2,len(cost)+1):
            dp = min(dpmn1 + cost[i-1],
                     dpmn2 + cost[i-2])
            
            dpmn2 = dpmn1
            dpmn1 = dp
        
        return dp