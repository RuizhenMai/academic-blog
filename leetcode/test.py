def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    
    BST on column then BST in row
    Reference: 
    """
    if len(matrix) == 0 or len(matrix[0])==0: return False
    
    M, N = len(matrix), len(matrix[0])
    
    # first BST
    lo, hi = 0, M - 1 # this must accompany lo< hi not lo<=hi 
    mid = (lo+hi) // 2
    while lo < hi:
        if target == matrix[mid][N-1]:
            break 
        elif target < matrix[mid][N-1]:
            hi = mid-1
        else:
            lo = mid+1
        mid = (lo+hi) // 2


    if target > matrix[mid][N-1] and mid < M-1 or mid == -1: Y = mid + 1
    else: Y = mid 

    print('passed first bst')
    # second BST 
    lo, hi = 0, N-1
    mid = (lo+hi) //2
    while lo < hi:
        if target == matrix[Y][mid]:
            break
        elif target < matrix[Y][mid]:
            hi = mid-1
        else:
            lo = mid+1
        
        mid = (lo+hi) // 2
        print(mid)
    X = mid
    print(Y,X,matrix[Y][X])
    
    return matrix[Y][X] == target

matrix = [
  [2,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

target = 2
print(searchMatrix(matrix, target))