---
layout: post
title: Akuna Capital Quant Trader 面经
---

1. Given three points in two-dimensional plane, determine if they exist on one line
   ```python
   def colinear(x1, y1, x2, y2, x3, y3):
    '''
    calculate the area of the triangle(or parallelagram) 
    composed by these three points by forming vectors, 
    and see the area is zero 
    '''
    area = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    if area == 0:
        return False
    else:
        return True
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