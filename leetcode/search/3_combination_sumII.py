class Solution(object):
    def combinationSum2Set(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        
        Time O(2^n) because for n numbers, we have a take or not take option for it
        reference: https://www.youtube.com/watch?v=RSatA4uVBDQ
        also refer to below
        """
        def dfs(candidates, target, s, cur, ans):
            '''
            s (int) - starting index(of candidates) of this time of  recursion
            target 
            
            '''
            if target == 0:
                ans.append(cur[:])# deep copy, otherwise cur will become empty
                return
            
            # the loop starting at s
            for i in range(s,len(candidates)):
                if candidates[i] > target: break
                cur.append(candidates[i])
                # since we cannot use duplicate this time,
                # we do i+1
                dfs(candidates, target-candidates[i], i+1, cur, ans)
                cur.pop()

        
        cur = []
        ans = []
        dfs(sorted(candidates), target, 0, cur, ans)
        # remove duplicates in ans 
        ans = list(set([tuple(x) for x in ans]))
        return ans

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]

        Time: worst worst case is [C(n,0) + ... + C(n,n) ] * k= 2^n * k 
        in the question we can have any length of soluitions, (0 may not be here but for convenience),
        for k-length solution, we can have maximum C(n,k) as such, from a candidates,
        since each number can only be use once. k is the longest solution. But we need to search all 
        the space for the answer in worst case 

        Space: O(k) k is the longest(deepest) solution 
        """
        def dfs(candidates, target, s, cur, ans):
            '''
            s (int) - starting index(of candidates) of this time of  recursion
            target 
            
            '''
            if target == 0:
                ans.append(cur[:])# deep copy, otherwise cur will become empty
                return
            
            # the loop starting at s
            for i in range(s,len(candidates)):
                if candidates[i] > target: break
                # i = s means we're at the starting position
                # and shall not consider i = s, then
                # candidates[i] = candidates[i-1] a duplicate
                # because we're not using i-1 at this for loop
                if i > s and candidates[i] == candidates[i-1]: continue
                cur.append(candidates[i])
                # since we cannot use duplicate this time,
                # we do i+1
                dfs(candidates, target-candidates[i], i+1, cur, ans)
                cur.pop()

        
        cur = []
        ans = []
        dfs(sorted(candidates), target, 0, cur, ans)

        return ans