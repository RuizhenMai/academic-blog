class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        
        DFS 
        Time: O(m*n*4^l)
        search is 4^l for len(word) = l
        m*n for every starting point
        Space: O(m*n + l) 
        m*n is the input, recursion depth is l
        """
        
        def outOfBound(x,y):
            '''
            global:
                board (2d array str) - the board passed by the question
            params:
                x,y (int) - the x y coordinate
            
            check if the coordinate is out of the bound of board
            '''
            return y >= len(board) or y < 0 or x >= len(board[0]) or x<0
        
        
        def dfs(x, y, s):
            '''
            global:
                board
                word
            params:  
                s (int) – starting position of word in current recursion
            return:
                (Bool) - if current recursion can find the char at word[s]
            '''

            if outOfBound(x,y): return False
            if board[y][x]!= word[s]: return False
            # since we already check the word[s] = board[y][x]
            if s == len(word) - 1: return True
            # move the current char here
            # in case it's going backward
            temp,board[y][x] = board[y][x], ""
            found =dfs(x+1,y,s+1) or\
                   dfs(x-1,y,s+1) or\
                   dfs(x,y-1,s+1) or\
                   dfs(x,y+1,s+1)
            
            # restore 
            board[y][x] = temp
            return found
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                # be careful here dfs signature is x,y
                if dfs(x,y,0): return True
                
        return False