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

        if i > 0: # decomposed into more than 1 fib num 
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