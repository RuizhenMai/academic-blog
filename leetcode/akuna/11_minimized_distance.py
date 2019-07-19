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