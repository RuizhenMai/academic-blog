class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        
        BFS first build the graph as Word Ladder I does, then DFS from the endword
        """
        if endWord not in wordList:
            return []
        
        from collections import deque, defaultdict
        
        wordMap = set(wordList)
        # used to record the child nodes in the correct graph
        children = defaultdict(list)
        
        q = set() # work as queue, avoid duplicates, when two different parents have same children
        
        # L is same across all words 
        L = len(beginWord)

        # An indicator to whether we found the endword
        # since we do not explicitly return right now
        found = False
        
        
        q.add(beginWord)
        wordMap.discard(beginWord)

        while not found and len(q) > 0:
            nxt = set() # this is used to replace q, in this way we can track what word are in current loop, see the if statement in line 45, if we don't use a temp storer we cannot use that condition
            
            for w in q: # for each word in queue 
                for i in range(L):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = w[:i] + c + w[i+1:]
                        
                        
                        # newWord not in wordMap means this route doesn't exist
                        # newWord in children means we will go back to previous level
                        # newWord in q means we will go back at the same level
                        if newWord not in wordMap or newWord in children or newWord in q: continue
                        

                        children[w].append(newWord)

                        nxt.add(newWord)
                        if newWord == endWord:
                            found = True
            q = nxt
        
        
        
        def dfs(beginWord, endWord, children, cur, ans):
            '''
            endWord (str) - the target 
            '''
            if endWord == beginWord:
                ans.append(cur[:])
            
            for w in children[beginWord]:
                cur.append(w)
                dfs(w, endWord, children, cur, ans)
                cur.pop()
        
                        
        
        ans = []
        if found:
            dfs(beginWord, endWord, children, [beginWord], ans)

        return ans
    

                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        