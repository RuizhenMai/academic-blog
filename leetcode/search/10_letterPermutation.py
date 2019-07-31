class Solution(object):
    def letterCasePermutationDFS(self, S):
        """
        :type S: str
        :rtype: List[str]

        Time: O(n * 2^l) l is the # of letters. ...
        Space: O(n) stack + O(n*2^l) ans there're maximum 2^l solutions, each solution has n length
        """
        def dfs(S, s, ans):
            '''
            S (lst) - the string S passed by the question converted to lst
            s (int) – starting position
            '''
            if s == len(S):
                ans.append("".join(S))
                return
            
            dfs(S, s+1, ans)
            # if it's int then not do the "flipped" version
            # of dfs
            # if it's char it has two branch of 
            # dfs 
            if not S[s].isalpha(): return 
            # toggle between uppercase and lower case
            # since 'A'- 'a' = 32 = 1<<5
            S[s] = chr(ord(S[s]) ^ (1 << 5)) 
            dfs(S, s+1, ans)
            S[s] = chr(ord(S[s]) ^ (1 << 5))
        
        ans = []
        dfs(list(S), 0, ans)
        return ans
            
    