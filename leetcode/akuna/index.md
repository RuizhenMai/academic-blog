---
layout: post
title: Akuna Capital Quant Trader 面经
---

1. Given three points in two-dimensional plane, determine if they exist on one line
   ```python
    def slope(x1,y1,x2,y2):
        if (x2-x1) == 0:
            return float('inf')
        return (y2-y1) / (x2-x1)

    # in n points check if there're three points lie on a straight line 
    def nColinear(pts):
        '''
        pts (array of tuples) - an array of sized-2 tuples for coordinates of the point
        '''
        for i in range(len(pts)):
            slopes = defaultdict(int)
            for j in range(i+1,len(pts)): 
                slopes[slope(*pts[i],*pts[j])] += 1
            for count in slopes.values():
                if count >= 2: # 2 same slopes mean there're 3 points on same line
                    return True

        return False

    print(nColinear([(1,2),(2,4),(3,5),(3,7)])) # expect false
    ```

2. Given a n by n matrix, find all local minima. A local minima is where it is smaller than its neighbors(left, right, above, bottom)
   
   For loop each i,j location in the matrix and then compare the element at i,j to its above, bottom, left and right
   ```python
    def local_minima(matrix):
        ans = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                # check if this location is smaller than left right up bottom 
                a = i - 1
                b = i + 1
                l = j - 1
                r = j + 1

                elem_a = matrix[a][j]  if a >= 0 else math.inf
                elem_b = matrix[b][j] if b < len(matrix) else math.inf
                elem_l = matrix[i][l] if l >=0 else math.inf
                elem_r = matrix[i][r] if r< len(matrix[i]) else math.inf

                center = matrix[i][j]
                if center < elem_a and center < elem_b and center < elem_l and center < elem_r:
                    ans.append(center)

                
        return sorted(ans)[:3]
   ```
   
3. Given a year, find all palindrome date (7 or 8 digits) in MM/DD/YYYY format of the century the year is in
   ```python
    from calendar import monthrange 

    def generate_palindrome_date(year):
        '''
        param:
            year (string)
        return:
            number of palindrome date of the century the year is in(int)
        '''
        century_start = year // 100 * 100 + 1 # 2001 is the start of 21st century
        century_end = century_start + 99
        count = 0

        for yyyy in range(century_start, century_end):
            for mm in range(1,13):
                num_days = monthrange(yyyy,mm)[1] # 28 days or 30 days in a month etc 
                for dd in range(1,num_days+1):
                    if dd < 10:
                        dd = "0" + str(dd)
                    else:
                        dd = str(dd)
                    
                    date = str(mm) + dd + str(yyyy)

                    # check if 7 digits palindrome
                    if date == date[::-1]:
                        count+=1

                    # check if exist 8 digits palindrome 
                    if mm < 10:
                        date_prime = "0" + str(mm) + dd + str(yyyy)
                        if date_prime == date_prime[::-1]:
                            count += 1

        
        return count
   ```
4. Given a graph and source, find the shortest path to all nodes, and take the largest path
   ```python
    import math
    import heapq

    def broadcast_delivery_time(source_id, matrix):
        '''
        param:
            source_id (int) - row index of the node that the message sent from
            matrix (array 2d) - adjacency matrix of the graph, [i][j] is from i to j
        return:
            (int) - minimum time taken to broadcast the information, if cannot, return -1
        '''
        dists = {} # distance dictionary storing shortest path from source_id node to all nodes
        pq = [(0,source_id)] # priority queue

        while pq: # while there's still nodes in it
            if len(dists) == len(matrix):
                break
            
            dist, start = heapq.heappop(pq)
            if start in dists:
                continue
            dists[start] = dist
            for j in range(len(matrix[start])):
                # only go to nodes haven't gone to, and `None` meaning there's no path
                if matrix[start][j] not in dists and matrix[start][j] != None: 
                    # note we will add double path, if there's two paths to the same nodes
                    # but only kept the shortest one bc of the first(and second maybe) if statement，
                    heapq.heappush(pq, (matrix[start][j]+dist, j))

        return max(dists.values()) if len(dists) == len(matrix) else -1
   ```

5. Given an array of initial distribution, `[m1,m2]` ,which sums up to 1, and a markov matrix of switching probability like `[[.8, .2],[.1,.9]]`, output the final distribution. 
   This is in fact a markov matrix question. Given a markov matrix of moving probablity, and differential equation s.t. 
   
   $$
    \begin{bmatrix}
    share_{1}\\
    share_{2}\\
    \end{bmatrix}_{t=k+1}=\begin{bmatrix}
    .8 & .1 \\
    .2 & .9 \\
    \end{bmatrix}\begin{bmatrix}
    share_{1}\\
    share_{2}
    \end{bmatrix}_{t=k}
   $$

   and initial state s.t. $$\begin{bmatrix}
       .4\\.6
   \end{bmatrix}_{t=0}$$ and then we need to solve for the final steady state when $t\rightarrow \infty$. There're two ways to solve the differential equation, one is the analytical one by solving A's eigenvalues and eigenvectors, this is doable in 2 by 2 case, but not in n by n since it's hard to programme a function to calculate determinant in n by n. Then we solve it analytically. 
   ```python
    def market_equilibrium(init_state, markov_matrix):
        '''
        init_state (1d array) - initial state of the population
        markov_matrix (2d array) - probability of staying and moving 
        '''
        state_t = [e for e in init_state] # same dimension as init_state
        for t in range(100):
            # since we update one element of state_t at a time, but we need the old elem for multiplication
            state_t_copied = [e for e in state_t] 
            for i in range(len(init_state)):
                state_t[i] = sum([markov_matrix[j][i] * state_t_copied[j] for j in range(len(init_state))]) # inner product of vector
        
        return state_t
   ```
6. Flipping signs: In an array A containing only 0s and 1s, a K-bit flip consists of choosing a (contiguous) subarray of length K and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.
    Return the minimum number of K-bit flips required so that there is no 0 in the array.  If it is not possible, return -1.
    The question was given originally in plus minus signs, just parse them into one and zero 
    ```python
    def minKBitFlips_naive(A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # if K longer than A, 
        # if A contains any 0 than return -1
        if K > len(A):
            return -1 if 0 in A else 0
        
        cnt = 0
        # loop only until -K position
        # then check the if remaining has zero
        # if so then it's not solvable 
        for i in range(len(A)-K+1):
            if A[i] == 0:
                # kbit flips
                for j in range(i,i+K):
                    A[j] = int(not A[j])
                cnt+=1
        
        return -1 if 0 in A[-K:] else cnt



        
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        
        this method is instead of literally flipping the sighs 
        putting symbols on the flipped location 
        """
        
        # flipped ^ A[i] == 0 then the location needs to be flipped
        # flipped = 0 and A[i] = 0 is normal situation 
        # flipped = 1 and A[i] = 0 is i location is flipped by previous flipping on locations <i 
        # flipped = 0 and A[i] = 1 is i location is not flipped but no need to (normal)
        # flipped = 1 and A[i] = 1 is i location is flipped by previous flipping but incorrectly 1->0
        
        # flipped ^ is_flipped_at[i-K] is reseting the flipped flag
        # flipped = 1 and is_flipped_at[i-K] = 1 means flipped from i-K shall not affect i
        # flipped = 1 and is_flipped_at[i-K]=0 nothing shall change
        # flipped = 0 and is_flipped_at[i-K]=1 idk, this won't happen i think
        # flipped = 0 and is_flipped_at[i-K]=0 nothing shall change
        flipped = 0
        cnt = 0
        is_flipped_at = [0]*len(A)
        # print(is_flipped_at)
        for i in range(len(A)): # need to iterate all
            if i>=K: # need to reset the flipped flag
                flipped ^= is_flipped_at[i-K]
            if flipped ^ A[i] == 0:
                # cannot flip the rest
                if i + K > len(A):
                    print(is_flipped_at)
                    return -1
                cnt+=1
                flipped ^= 1 # if we enter as 1, then become 1 meaning it's flipped twice(then back to not flipped)
                is_flipped_at[i] = 1
        
        
        return cnt
    ```
7. Classify the trade with three features and two labels. Use KNN since the problem says it's not necessarily linearly seperable
   ```python
    def knn(train_trades, labels, test_trades): # just 1nn
        res = []
        for test_x in test_trades:# for each testing subject
            distances = []
            for train_x in train_trades: # for each training data  
                distance = 0 # distances to all training data
                for j in range(len(train_x)): # for each feature
                    distance += abs(train_x[j]-test_x[j])
                distances.append(distance)
            argmin = distances.index(min(distances))
            res.append(labels[argmin])
        return res
   ```

8. Parse lines into counts of words and counts of characters
   ```python
    import sys, re, string
    from collections import defaultdict

    def parse_words(lines):
        # lines is list !!
        # first parse words
        res_words = defaultdict(int)
        for line in lines:
            char_list = []
            findNonWord = False
            for char in line:
                if re.match("[a-z]", char) and not findNonWord:
                    char_list.append(char)
                # finished parsing one word
                elif re.match("\s",char):
                    # only add if that's a word length > 0
                    # check the next comment
                    if not findNonWord and len(char_list) > 0:
                        res_words[''.join(char_list)] += 1
                    char_list = []
                    findNonWord = False
                # not char nor whitespace 
                # wait until finding a whitespace
                # meaning that a new word is to begin
                else:
                    findNonWord = True
                    char_list = []
                
                # the end of line is also a whitespace, but not listed as \n as we're parsing it in str obj
                if char == line[-1] and not findNonWord and len(char_list) > 0:
                    res_words[''.join(char_list)] += 1
                    char_list = []
        
        res = []
        for key in sorted(res_words.keys()):
            res.append(key+" "+str(res_words[key]))

        return res

    def parse_letters(lines):
        letters = dict(zip(string.ascii_lowercase, [0]*26))
        for line in lines:
            for char in line:
                if char in string.ascii_lowercase:
                    letters[char] += 1

            res = []
        for key in sorted(letters.keys()):
            res.append(key+" "+str(letters[key]))

        return res

    lines = sys.stdin.readlines()
    print('words\n'+'\n'.join(parse_words(lines)))
    print('letters\n'+'\n'.join(parse_letters(lines)))
   ```
9. Given a line and a sphere, find their intersection points and their distances to origin (the line has starting point so make sure the intersection points are not off) 
    Since the points on a sphere with center $(c_x,c_y,c_z)$ and radius $r$ has equation:

    $$
    (x-c_x)^2+(y-c_y)^2+(z-c_z)^2=r^2
    $$

    As two-point form, a line in two-dimension can be written as $\displaystyle \frac{y_2-y_1}{x_2-x_1}=\frac{y_1-y}{x_1-x}$, parametrize $x$ as $x=x_1+(x_2-x_1)t$, we can obtain $y=y_1+(y_2-y_1)t$, extend this to three dimension, we have equations of a line:

    $$
    x=x_1+(x_2-x_1)t\\y=y_1+(y_2-y_1)t\\ z=z_1+(z_2-z_1)t
    $$

    Since we're looking for intersection points, we can plug in the parametric equations into the sphere one and obtain
    
    $$
    (x_1+(x_2-x_1)t-c_x)^2+(y_1+(y_2-y_1)t-y)^2+(z_1+(z_2-z_1)t-z)^2=r^2
    $$

    Then we can expand this equation and get a quardractic equation of $t$, s.t.
    
    $$
    \begin{aligned}
    &t^2*[(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2]-\\
    &t*2[(x_2-x_1)(c_x-x_1)+(y_2-y_1)(c_y-y_1)+(z_2-z_1)(c_z-z_1)]+\\
    &[(c_x-x_1)^2+(c_y-y_1)^2+(c_z)^2-r^2]=0
    \end{aligned}
    $$

    and the solution will be given by
    
    $$
    t^*=\frac{-b\pm \sqrt{b^2-4ac}}{2a}
    $$

    and 

    $$
    \begin{aligned}
    a &=(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2\\
    b &=(x_2-x_1)(c_x-x_1)+(y_2-y_1)(c_y-y_1)+(z_2-z_1)(c_z-z_1)\\
    c &=(c_x-x_1)^2+(c_y-y_1)^2+(c_z-z_1)^2-r^2
    \end{aligned}
    $$
    The python program will be:
    ```python
    def inInterval(x,a,b):
        return True if (x > a and x < b) or (x < a and x > b ) else False

    def line_intersect_sphere(cx,cy,cz,radius,x1,y1,z1,x2,y2,z2):
        a = (x2-x1)**2+(y2-y1)**2+(z2-z1)**2
        b = ((x2-x1)*(cx-x1)+(y2-y1)*(cy-y1)+(z2-z1)*(cz-z1))*-2
        c = (cx-x1)**2+(cy-y1)**2+(cz-z1)**2-radius**2

        delta = (b**2-4*a*c)**(1/2)
        if delta < 0:
            return 0.0

        t1 = (-b + delta) / (2*a)
        t2 = (-b - delta) / (2*a)

        x_res1 = x1+(x2-x1)*t1
        y_res1 = y1+(y2-y1)*t1
        z_res1 = z1+(z2-z1)*t1

        dx1 = (x_res1-x1)**2
        dy1 = (y_res1-y1)**2
        dz1 = (z_res1-z1)**2

        if not inInterval(x_res1,x1,x2) or not inInterval(y_res1,y1,y2) or not inInterval(z_res1,z1,z2):
            distance1 = 0.0
        else:
            distance1 = dx1+dy1+dz1

        x_res2 = x1+(x2-x1)*t2
        y_res2 = y1+(y2-y1)*t2
        z_res2 = z1+(z2-z1)*t2

        dx2 = (x_res2-x1)**2
        dy2 = (y_res2-y1)**2
        dz2 = (z_res2-z1)**2


        if not inInterval(x_res2,x1,x2) or not inInterval(y_res2,y1,y2) or not inInterval(z_res2,z1,z2):
            distance2 = 0.0
        else:
            distance2 = dx2+dy2+dz2
        
        return sorted([distance1,distance2])

    print(line_intersect_sphere(1,4,0,4,1,2,3,2,2,1))

    ```
10. Given a number `x`, see if it can be represented as a sum of `n` unique Fibonacci numbers.
    My thought is every odd position $F_i$ can be decomposed into maximum $(i+1)/2$ fib numbers and even $i$ is $i/2$. If a number is not a fib number, but composed by several, then we expand each of its composing $F_i$'s. 
    ```python
    def nearestSmallerFib(x):
        # in the case of small x, no need to use closed form solution?
        fn = 1 # f1
        fnplus1 = 1 #f2
        fnplus2 = 2 #f3
        idx = 3 # ith fib number
        while fnplus2 <= x:
            fn = fnplus1
            fnplus1 = fnplus2
            fnplus2 = fn + fnplus1
            idx += 1

        return fnplus1, idx-1

    def nFibRepresentation(x, n):
        xx = x
        nums = []
        while x > 0:
            f,loc = nearestSmallerFib(x)
            x = x - f
            nums.append((f,loc))
        
        print("greedy result is:",nums)
        if len(nums) > n:
            return False
        
        if len(nums) == n:
            return True
        
        # find the maximum possible n fib nums that can compose this number
        count = 0
        for i in range(len(nums)):
            summand = 0
            if nums[i][1] % 2 == 0: # even ith fib location
                summand = nums[i][1] / 2
            else: #  odd 
                summand = (nums[i][1]+1) / 2 - 1 # minus 1 is because the question does not allow f1 =1 f2=1 at the same time

            count += summand

            if i > 0:
                if nums[i-1][1] % 2 == nums[i][1] % 2:
                    count -= summand
                else:
                    count -= 1
        
        print("max fib nums of",xx,"can be decomposed into:",count)
        if count > n:
            return True
        else:
            return False
        
    x, n = 110, 3
    # print("Fibonacci Representation of",x,"is")
    print(nFibRepresentation(x,n)) # expect true and stdout 8 fib numbers
    ```
11. Find a point with integer coordinate inside a triangle(or on the boundary) that minimize the distance to three vertices 
    ```python
    def triangleArea(x1,y1,x2,y2,x3,y3):
        return abs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))/2

    def isInTriangle(x,y,x1,y1,x2,y2,x3,y3):
        A = triangleArea(x1,y1,x2,y2,x3,y3)
        A1 = triangleArea(x,y,x2,y2,x3,y3)
        A2 = triangleArea(x1,y1,x,y,x3,y3)
        A3 = triangleArea(x1,y1,x2,y2,x,y)

        # print(x,y,A,A1,A2,A3)


        if A != (A1+A2+A3):
            return False
        

        return True

    def sqDistance2ThreeVertices(x,y,x1,y1,x2,y2,x3,y3):
        return (x-x1)**2+(y-y1)**2+(x-x2)**2+(y-y2)**2+(x-x3)**2+(y-y3)**2

    def ptrMinDistance(x1,y1,x2,y2,x3,y3):
        llim = min(x1,x2,x3)
        rlim = max(x1,x2,x3)
        ulim = max(y1,y2,y3) # upper
        blim = min(y1,y2,y3) # bottom

        distances = []
        for i in range(llim, rlim+1):
            for j in range(blim, ulim+1):
                if isInTriangle(i,j,x1,y1,x2,y2,x3,y3):
                    distances.append((sqDistance2ThreeVertices(i,j,x1,y1,x2,y2,x3,y3),(i,j)))


        print(sorted(distances, key = lambda tup: tup[0]))

    ptrMinDistance(0,0,1,0,1,1) # expect [(2, (1, 0)), (3, (0, 0)), (3, (1, 1))]
    ```
12. Two users are assigned to three cards valued 0-9. Three of kinds > Pair > High Card 
    ```python
    def hasThreeOfKind(cards):
        return True if cards[0] == cards[1] == cards[2] else False

    def hasPair(cards):
        return True if cards[0] == cards[1] or cards[1] == cards[2] or cards[0] == cards[2] else False

    def pokerGame(p1,p2):
        '''
        p1 (array) - three cards from 0-9 assigend to p1
        p2 (array) - assigned to p2
        '''
        p1.sort(reverse = True)
        p2.sort(reverse = True)

        rankp1 = 0 
        rankp2 = 0
        
        if hasPair(p1):
            rankp1 = 1
        
        if hasPair(p2):
            rankp2 = 1

        if hasThreeOfKind(p1):
            rankp1 = 2
        
        if hasThreeOfKind(p2):
            rankp2 = 2
        

        if rankp1 == rankp2 == 1:
            flag1 = 0 if p1[0] == p1[1] else 1
            flag2 = 0 if p2[0] == p2[1] else 1

            if p1[flag1] == p2[flag2]:
                flag1 = flag1 + 2 if flag1 == 0 else flag1 - 1
                flag2 = flag2 + 2 if flag2 == 0 else flag2 - 1

            return 1 if p1[flag1] > p2[flag2] else 2

        elif rankp1 == rankp2: # 0 or 2 rank
            i = 0
            while p1[i] == p2[i]:
                i+=1
            
            if i==len(p1): # all same cards, draw new card
                pass 
            
            return 1 if p1[i] > p2[i] else 2

        return 1 if rankp1 > rankp2 else 2

    print('Player')
    print(pokerGame([1,2,3],[0,2,3])) # expect player 1 win
    print('win')

    ```
13. Given a list of words and a list of directed edge from `tup[0]` to `tup[1]` representing if char `tup[0]` to char `tup[1]` can be phrased , return whether the words can be represented 
    ```python
    def char2int(c):
        return ord(c) - ord('a')

    def constructAdjMatrix(edges):
        '''
        param:
            edges (array of tuples) - consist of a list of directed edges from i[0] to i[1]
        return:
            adjacency matrix (array of array) - [i][j] is edge from i to j
        '''
        res = [[None]*26 for i in range(26)]
        for edge in edges:
            res[char2int(edge[0])][char2int(edge[1])] = 1

        return res

    def spellTheWord(words, edges):
        adjMatrix = constructAdjMatrix(edges)
        res = []
        for w in words:
            for i in range(len(w)-1):
                # print(i,char2int(w[i]),char2int(w[i+1]),adjMatrix[char2int(w[i])][char2int(w[i+1])])
                if adjMatrix[char2int(w[i])][char2int(w[i+1])] != 1:
                    res.append(0)
                    break
            # finished looping all chars in a word
            if len(res) == 0 or res[-1] != 0: # did not append 0 in the for loop
                res.append(1)
        return res

    # print(spellTheWord(['a','b','ab','ba'],[('a','b')])) # expect [1,1,1,0]
    print(spellTheWord(['what','who','where'],[('w','h'),('h','a'),('h','o'),('a','t'),('h','e')])) 

    ```

14. escape the lake
15. chess game. Minimum steps for TWO knight to reach and need all possible meeting points 
    ```python
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

    ```
16. ranked election
17. Nearest Sum: Given a list of positive integers and an integer N, return the indices of subarray whose continuous sum is closest to N
    ```python
    def naiveNearestSum(nums, N): # O(n^2)
        currSum = 0
        res = [0,0,abs(N-currSum)] # deviation of sum from N
        for i in range(len(nums)):
            currSum = 0 # clear it for every starting point i 
            for j in range(i,len(nums)):
                currSum += nums[j]
                currDiff = abs(N-currSum)

                if currDiff < res[2]:
                    res = [i,j,currDiff]

                if currDiff == 0:
                    return res
            
        return res

    print(naiveNearestSum([3,4,5,6,7],14)) # expect [1,3,1]


    def posNearestSum(nums, K): # O(n)
        '''
        this method only takes non-negative array of nums
        it utilizes non-neg numbers s.t. if sum[i:j] > K,
        it means we (maybe) add too much (加爆),
        then we need to substract the sum[i:j] by i = i + 1
        '''
        currSum = 0
        res = [0,0, abs(K-currSum)]
        resTemp = [0,0, abs(K-currSum)] # don't let resTemp = res, very easy to get things wrong
        i = j = 0
        currDiff = prevDiff = 0
        # we only need to constrain j < len(nums)
        # because say sum[i:j] = sum[1:4], and 4 is the last position
        # if we still need to increase j (second else condition below)
        # it means the currSum is too small 
        # moving i to the right will no longer be helpful
        while i <= j and j < len(nums): 
            currSum += nums[j]

            prevDiff = currDiff

            currDiff = K - currSum
            
            if currDiff <= 0: # we need to move i right
                if abs(currDiff) < abs(prevDiff): # currDiff is better
                    resTemp = [i,j,abs(currDiff)]
            
                # substracting nums[i] because we're shifting i+=1
                # substraing nums[j] because we will add it back in next iteration
                currSum -= (nums[i]+nums[j]) 
                i += 1
            
            else: # move j
                resTemp = [i,j,abs(currDiff)]
                j += 1
            
            if resTemp[2] < res[2]: # resTemp is just for making this if condition written separately here
                res = resTemp
        
        return res

    print(posNearestSum([3,4,5,6,7],14)) # expect [1,3,1]

    ```