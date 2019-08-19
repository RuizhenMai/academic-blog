'''
Knapsack Problem:
Given N items, w[i] is the weight of the i-th item and v[i] is value of the i-th item. 
Given a knapsack with capacity W. Maximize the total value. Each item can be use 0 or 1 time.
'''

def knapsack01(w, v, W):
    '''
    Params
        w: array ints - w[i] is the weights of an item
        v: array ints - v[i] is the value of an item
        W: int        - maximum weight that can be used
    '''
    N = len(w)
    v.insert(0,0)
    w.insert(0,0)
    # dp[i][j]: maximum value achieved by using first i items
    # and exact total j weights
    # 0 < j < W
    # 0 < i < len(w)
    # init states: 
    # dp[0][*] = 0
    # because using 0 item to achieve 0 weight has at max 0 value
    # and using 0 item to achieve 1 or more weights is invalid 
    # dp[*][0] = 0 
    # because using any items to achieve 0 weight can only have 0 value
    # (no weight can be used)
    dp = [[0]*(W+1) for i in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,W+1):
            temp = 0 if j-w[i] < 0 else dp[i-1][j-w[i]] + v[i]
            dp[i][j] = max(dp[i-1][j], # not use the ith item
                            temp) # use the ith item
                           # use the ith item make we only have j-w[i] weights left
                            

    # take the max values using all the items, but no need to use max values 
    # over all the "exact" weights
    # it may we get max values by using W-1 weights
    return max(dp[N]) 

w = [1,1,2,2]
v= [1,2,4,5]
res = knapsack01(w, v, 4)
print(res)

def knapsack01R(w, v, W):
    N = len(w)
    w.insert(0,0)
    v.insert(0,0)

    dp = [0]*(W+1)

    for i in range(1,N+1):
        tempList = dp[:]
        for j in range(1,W+1):
            temp = 0 if j-w[i] < 0 else tempList[j-w[i]] + v[i]
            dp[j] = max(tempList[j], temp)
    
    return max(dp)

res = knapsack01R(w, v, 4)
print(res)

def knapsack01R2(w, v, W):
    
    dp = [0] * (W+1)
    N = len(w)
    # w.insert(0,0)
    # v.insert(0,0)
    for i in range(N):
        for j in range(W,w[i]-1,-1):
            dp[j] = max(dp[j], dp[j-w[i]] + v[i])
    
    return max(dp)

res = knapsack01R2(w, v, 4)
print(res)