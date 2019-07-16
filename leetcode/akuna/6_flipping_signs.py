# Naive Solution with O(n^k)
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


                
                