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

print(colinear(1,2,2,4,3,5))