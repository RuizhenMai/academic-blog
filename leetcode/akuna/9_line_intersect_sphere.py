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
# print(line_intersect_sphere(0,0,0,1.52,3,4,3,1,1,1))