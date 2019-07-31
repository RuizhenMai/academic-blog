class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        
        DFS
        """
        def dfs(n, d, k, s, cur,ans):
            '''
            d (int) - depth of recursion
            s (int) - starting position of current loop, different than d
            k (int) - required length of solution, this can be mixed with d certain conditions met, but don't mix s with d

            Time: O(n choose k)*k. Imagine a tree with empty node, and firt level 1,2,3,4,
            next level, below 1 is 2,3,4, below 2 is 3,4, below 3 is 4, below 4 is nothing
            we're doing DFS on this tree, and the tree has total c(n,k) leaves

            Space: O(k)
            '''
            if d == k:
                # this operation requires O(k)
                ans.append(cur[:])
                return 
            
            for i in range(s,n+1):
                cur.append(i)
                dfs(n, d+1, k, i+1, cur, ans)
                cur.pop()
        
        cur = []
        ans = []
        dfs(n, 0, k, 1, cur, ans)
        return ans