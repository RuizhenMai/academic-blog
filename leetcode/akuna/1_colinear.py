from collections import defaultdict
# three points colinear 
def colinear(x1, y1, x2, y2, x3, y3):
    '''
    calculate the area of the triangle(or parallelagram) 
    composed by these three points by forming vectors, 
    and see if it is zero 
    '''
    area = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    if area == 0:
        return False
    else:
        return True



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

print(nColinear([(3,5),(2,4),(1,2),(3,6)])) # expect true
