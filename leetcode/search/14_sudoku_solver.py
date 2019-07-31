class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        
        reference: https://www.youtube.com/watch?v=ucugbKwjtRs
        """
        
        # explained in dfs
        rows = [[0]*10 for i in range(9)]
        cols = [[0]*10 for i in range(9)]
        boxes = [[0]*10 for i in range(9)]
        
        def dfs(x, y):
            '''
            global:
                rows (2d array int) - store for each row, which number is used, used will be marked 1, access index 
                cols (2d array int) - same for rows
                boxes (2d array int) - same for rows, access index [y//3 * 3 + x//3] 
                They all have 10 length just for convenience of storing num 1 in position 1 and so on
                
                board (2d array str) - board passed by the question
            
            params:
                x,y: coordinates
            '''
            
            if y == 9: # since it's 0 to 8
                return True # the sudoku is solvable
            
               
            nextX = (x+1) % 9
            nextY = y + 1 if (x+1) == 9 else y
            
            if board[y][x] != '.': return dfs(nextX, nextY)  
            
            # here is looping for every integer
            # 1 to 9
            
            for i in range(1,10): 
                if not available(i,x,y): continue
                # if not rows[y][i] and not cols[x][i] and not boxes[y//3*3+x//3][i]
                rows[y][i] = 1
                cols[x][i] = 1
                boxes[y//3*3+x//3][i] = 1
                
                # we used index 0 to 8 for storing
                board[y][x] = str(i)
                # if the if conditions seem 
                # confusing
                # just remove it and simply use dfs(·)
                if dfs(nextX, nextY): return True
                rows[y][i] = 0
                cols[x][i] = 0
                boxes[y//3*3+x//3][i] = 0
                board[y][x] = '.'
                    
            return False
        
        def available(i, x, y):
            '''
            check if it's available to put 
            the `i` in the y,x position 
            by checking cols, rows, and boxes
            '''
            return not rows[y][i] and \
                   not cols[x][i] and \
                   not boxes[y//3*3+x//3][i]
        
        
        # Fill the necessary things first 
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    appearNum = int(board[i][j])
                    rows[i][appearNum] = 1
                    cols[j][appearNum] = 1
                    boxes[i//3*3 + j//3][appearNum] = 1
                    print(i//3*3+j//3)
        
        dfs(0,0)
            