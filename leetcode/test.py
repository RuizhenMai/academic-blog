def substringk(s, k):
    '''
    Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.
    
    sliding window
    '''

    if len(s) == 0 or len(s) < k or k == 0:
        return []


    ans = set()
    letter = {}

    start = 0 # start index of the window
    for i,c in enumerate(s):
        if c in letter and letter[c] >= start:
            start = letter[c] + 1 # update the start position
        
        letter[c] = i # record the position
        if i - start + 1 == k:
            ans.add(s[start:i+1])
            start += 1 

    return ans 

# s = "awaglknagawunagwkwagl"; k = 4
# print(substringk(s,k))

def MaxMinAltitudes(matrix):
    '''
    Given a matrix with r rows and c columns, 
    find the maximum score of a path starting at [0, 0] and ending at [r-1, c-1]. 
    The score of a path is the minimum value in that path. 
    For example, the score of the path 8 → 4 → 5 → 9 is 4.

    '''

    if len(matrix) == 0:
        return -1
    
    M,N = len(matrix), len(matrix[0])

    # dp[i][j] = max score at i j, where score is the minimum on the path
    dp = [[-float('inf')] * (N+1) for _ in range(M+1)] # to account for boundaries

    dp[1][1] = matrix[0][0]
    dp[1][2] = matrix[0][1]
    dp[2][1] = matrix[1][0]

    for i in range(1,M+1):
        for j in range(1,N+1):
            if (i == 2 and j == 1) or \
                (i == 1 and j == 2) or \
                (i == 1 and j == 1) or \
                (i == M and j == N):
                continue 
            score1 = min(matrix[i-1][j-1], dp[i-1][j]) # up
            score2 = min(matrix[i-1][j-1], dp[i][j-1]) # left 
            dp[i][j] = max(score1, score2)
        
    return max(dp[M-1][N], dp[M][N-1])
    
# matrix = [[1, 2, 3],[4, 5, 1]]
# print(MaxMinAltitudes(matrix))    
            

def shortestRouteToTreasury(matrix):
    '''
    You have a map that marks the location of a treasure island. 
    Some of the map area has jagged rocks and dangerous reefs. 
    Other areas are safe to sail in. There are other explorers trying to find the treasure. 
    So you must figure out a shortest route to the treasure island.

    Assume the map area is a two dimensional grid, represented by a matrix of characters.
     You must start from the top-left corner of the map and can move one block up, down, left or right at a time. The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe. 
    Output the minimum number of steps to get to the treasure.
    '''

    if len(matrix) == 0 or len(matrix[0]) == 0: 
        return -1

    M,N = len(matrix),len(matrix[0])
    # bfs
    q = [(0,0)] # (y,x)
    ans = 0

    while q:
        print(q)
        tempQ = []
        for y,x in q:
            for dy, dx in [[0,1],[1,0],[-1,0],[0,-1]]:
                if 0<=y+dy<M and 0<=x+dx<N:
                    if matrix[y+dy][x+dx] == 'X':
                        return ans + 1
                    elif matrix[y+dy][x+dx] == 'O':
                        tempQ.append((y+dy, x+dx))
                        matrix[y+dy][x+dx] = 'D' # mark as visited 
        ans += 1
        q = tempQ 

    return -1 

matrix = [['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]
print(shortestRouteToTreasury(matrix))





