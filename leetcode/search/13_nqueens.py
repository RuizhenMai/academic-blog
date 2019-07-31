class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        
        DFS 
        reference: https://www.youtube.com/watch?v=Xa-yETqFNEQ
        """
        
        def available(x,y):
            '''
            check if this position of the board can be placed
            '''
            return not cols[x] and \
                   not diag1[x+y] and \
                   not diag2[x-y + n - 1]
        
        def updateBoard(x,y,put):
            '''
            update the
            board, 
            columns,
            two diagonal lines
            '''
            board[y][x] = 'Q' if put else '.'
            cols[x] = put
            diag1[x+y] = put
            diag2[x-y+n-1] = put
            
        def dfs(n, y):
            '''
            global:
                cols (array int) - empty status of a column
                diag1 (array int) - normal diagonal 
                diag2 (array int) - reverse diagonal
                ans (2d array int) 
                board (2d array int) - serve as a cur
            params: 
                n (int) - total number of rows, max depth of recursion
                y (int) - current position of row
            '''
            if y == n:
                ans.add(tuple(["".join(x) for x in board]))
                return
            
            # looping for every column position in a row
            for x in range(n):
                if not available(x,y): continue
                updateBoard(x,y,True)
                dfs(n, y+1)
                # this is like the cur 
                # poping out the previous item
                updateBoard(x,y,False)
                    
                
        
        cols = [0] * n
        # for every square on the digaonal lines
        # of the board,
        # there's two diag1 
        diag1 = [0] * (2*n-1) 
        # similar for diag2
        diag2 = [0] * (2*n-1)
        ans = set()
        board = [["."]*n for i in range(n)]
        dfs(n,0)
        return ans
        
        