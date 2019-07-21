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
