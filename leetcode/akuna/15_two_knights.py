from collections import defaultdict
class cell:
    # a cell on the chess board
    def __init__(self, x, y, step = 0, parent = None):
        self.x = x
        self.y = y
        self.step = step # minimum steps to reach this position
        self.parent = parent 
    
def isInside(x,y,N):
    return True if x>=0 and x<N and y>=0 and y<N else False

def minStepToTargetByKnight(N, white_knight, black_knight, white_do_capture):
    # by BFS
    dx = [-1, -2, -2, -1, 1, 2, 2, 1] # From lower left counterclockwise
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    
    queue = [cell(*white_knight)]

    visited_white = [[False]*N for i in range(N)]
    visited_white[white_knight[0]][white_knight[1]] = True

    res = defaultdict(int) # storing all meet points 
    steps = 0
    while len(queue) > 0:
        c = queue.pop(0)
        visited_white[c.x][c.y] = True

        # reach destination
        if c.x == black_knight[0] and c.y == black_knight[1]:
            steps = c.step 
            break

        #BFS
        for i in range(8):
            nx = c.x + dx[i]
            ny = c.y + dy[i]

            if isInside(nx,ny,N) and not visited_white[nx][ny]:
                queue.append(cell(nx,ny,c.step+1, c)) # add one more step from old cell 
            

    # Two knights can only meet by odd or even steps at given positions
    # Given positions, it's impossible for them to meet by both odd and even steps
    # at the same time
    if steps % 2 == 0 and white_do_capture == 1:
        return (-1,-1)
    elif steps % 2 == 1 and white_do_capture == 0:
        return (-1,-1)

    # BFS on black knight
    queue = [cell(*black_knight)]
    visited_black = [[False]*N for i in range(N)]
    visited_black[black_knight[0]][black_knight[1]] = True

    
    while len(queue) > 0:
        c = queue.pop(0)
        visited_black[c.x][c.y] = True        

        if visited_white[c.x][c.y] == 1:
            if steps % 2 == 0 and c.step == steps / 2:
                res[(c.x,c.y)] += 1
            elif steps % 2 == 1 and c.step == (steps - 1) / 2:
                res[(c.x,c.y)] += 1
        # last round
        if c.step > steps // 2: # right now c.step is black's move
            break

        for i in range(8):
            nx = c.x + dx[i]
            ny = c.y + dy[i]

            if isInside(nx,ny,N) and not visited_black[nx][ny]:
                queue.append(cell(nx,ny,c.step+1, c)) # add one more step from old cell 
        
    
    if len(res) > 0:
        print(res)
        return (steps,len(res.keys()))

    print('Too small')
    return (-1,-1) # this probably only happens when it's really small like 3*3 one in corner one in middle

# print(minStepToTargetByKnight(8,(7,2),(0,1),False)) # expect (4,5)
# print(minStepToTargetByKnight(8,(7,2),(0,1),True)) # expect (-1,-1)
# print(minStepToTargetByKnight(8,(0,0),(1,2),True)) # expect (1,1)
# print(minStepToTargetByKnight(3,(0,0),(1,1),True)) # expect (-1,-1) 
# print(minStepToTargetByKnight(3,(0,0),(1,1),False)) # expect (-1,-1) two impossible to reach
