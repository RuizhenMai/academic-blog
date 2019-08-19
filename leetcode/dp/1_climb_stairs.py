class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        
        Fibonacci Number, this is slightly different 
        since there's no f(0) = 0 step to climb a 0 step
        stairs, in fact N steps stair needs F(n+1) = F(n) + F(n-1)
        steps, one step further than a fib number 
        """
        if n <= 1:
            return 1
        
        fnm2 = 0 # f(0)
        fnm1 = 1 # f(1)
        fn = 0 # f(2)
        
        for i in range(2,n+1):
            fn = fnm1 + fnm2
            fnm2 = fnm1
            fnm1 = fn
        
        
        return fnm2+fnm1