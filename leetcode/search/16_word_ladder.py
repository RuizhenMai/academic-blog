class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        
        BFS(since shortest path) 
        Time: O(n*26*l) l = len(beginWord) n = len(wordList)
        n * 26 * 是因为while loop里的每一个step都只会有不超过n数量的word match这个wordList里的， 例如example 1，如果加上“ait”在里面，那么最多也就是2个match第一次，剩下的都是每个match一次，所以是match了6次，如果有“干扰”正确道路的词出现，例如“dit”，实际上并不会干扰，因为在同一个BFS depth里dot已经被用掉了，下一轮BFS里dit并不能找到dot
        
        Space: O(n)
        """
        if endWord not in wordList:
            return 0
        
        from collections import deque
        
        # store all possible words in each step
        # similuate FIFO queue
        q = deque() 

        wordMap = set(wordList)
        beginLst = list(beginWord)
        step = 1 # the begin word itself counted as 1 step
        
        q.appendleft(beginLst)
        while len(q) != 0:
            size = len(q)
            for i in range(size): # pop all elements in queue once to properly increment `step`
                w = q.pop()
                # print('poped word',w,q)
                for j in range(len(w)): # 这个跟下面的for loop一起的时间是26 * l
                    char = w[j] # in case we need to put this back
                    for letter in range(ord('a'),ord('a')+26):
                        w[j] = chr(letter)
                        if ''.join(w) in wordMap:
                            if ''.join(w) == endWord:
                                return step+1
                            q.appendleft(w[:])
                            # deep copy 
                            # print('appended word',q)
                            # remove the new word from set in case  in next round of BFS we will recount it
                            wordMap.remove(''.join(w))
                            
                    # put it back for next 26 letters loop 
                    w[j] = char
                
            step += 1
        
        return 0

    def ladderLengthDoubleBFS(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        
        BFS(since shortest path) 
        Time: O(n*26*l) l = len(beginWord) n = len(wordList)
        Space: O(n)
        """
        if endWord not in wordList:
            return 0
        
        from collections import deque
        
        
        q1 = deque() 
        q2 = deque()

        wordMap = set(wordList)
        beginLst = list(beginWord)
        endLst = list(endWord)
        wordMap.remove(endWord)
        step = 1 # the begin word itself counted as 1 step
        
        q1.appendleft(beginLst)
        q2.appendleft(endLst)
        while len(q1) != 0 and len(q2) != 0:
            print(q1,q2)
            if len(q1) > len(q2): q1,q2 = q2,q1
            
            for i in range(len(q1)): 
                w = q1.pop()
                print(w)
                for j in range(len(w)): # 这个跟下面的for loop一起的时间是26 * l
                    char = w[j] # in case we need to put this back
                    for letter in range(ord('a'),ord('a')+26):
                        w[j] = chr(letter)
                        if w in q2:
                            return step+1
                        
                        if ''.join(w) in wordMap:
                            
                            q1.appendleft(w[:])
                            # deep copy 
                            # remove the new word from set in case  in next round of BFS we will recount it
                            wordMap.remove(''.join(w))
                            
                    # put it back for next 26 letters loop 
                    w[j] = char
            
            step += 1
        
        return 0
        
        
            
            
        
        
            
            