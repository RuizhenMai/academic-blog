import numpy as np # numpy just make it much faster 
import math

def local_minima_np(matrix): # not quite sure if we need to check bounds
    return ((matrix <= np.roll(matrix,1,0)) & # using bitwise and maybe faster, compare the above
            (matrix <= np.roll(matrix,-1,0)) & # compare the bottom
            (matrix <= np.roll(matrix,1,1)) & # compare the left
            (matrix <= np.roll(matrix,-1,1))) # compare the right


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

m = [[5,5,5,5,5],
    [5,1,5,5,5],
    [5,5,5,4,5],
    [5,5,4,0,3],
    [2,5,5,3,1]]

print(local_minima(m)) # output 0,1,2
# print(local_minima_np(m))