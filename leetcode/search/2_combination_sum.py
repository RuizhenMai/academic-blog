class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        
        DFS
        reference: https://www.youtube.com/watch?v=zIY2BWdsbFs
        """
        def dfs(candidates, target, s, cur, ans):
            '''
            s (int) - starting index(of candidates) of this time of  recursion
            target 
            
            Time: refer to https://github.com/Deadbeef-ECE/Interview/blob/master/Leetcode/BackTracking/039_Combination_Sum.java
            '''
            if target == 0:
                ans.append(cur[:])# deep copy, otherwise cur will become empty
                return
            
            # the loop starting at s
            for i in range(s,len(candidates)):
                # Note here break means adding candidates[i] 
                # is not useful IN the previous recursion
                # probably shall try candidates[i+1]
                # and also b/c after i pos is larger line 43
                # if we don't sort, we probably need to check
                # the condition by division and do something doesn't look very intuitive
                if candidates[i] > target: break
                cur.append(candidates[i])
                # we're using candidates[i] so we take 
                # target - candidates[i]
                # we can reuse candidates[i] so we do not 
                # make i+1
                dfs(candidates, target-candidates[i], i, cur, ans)
                cur.pop()

        
        cur = []
        ans = []
        dfs(sorted(candidates), target, 0, cur, ans)
        return ans