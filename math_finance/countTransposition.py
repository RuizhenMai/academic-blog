def mergesort(lst):
    # divide
    mid = len(lst)//2
    L = lst[:mid]
    R = lst[mid:]
    if len(lst) > 2:
        mergesort(L)
        mergesort(R)

    # merge 
    Lindex = 0
    Rindex = 0
    i = 0
    while Lindex != len(L) and Rindex != len(R):
        if L[Lindex] < R[Rindex]:
            lst[i] = L[Lindex]
            Lindex+=1
        
        else:
            lst[i] = R[Rindex]
            Rindex+=1
        
        i+=1 
    
    while Lindex != len(L):
        lst[i] = L[Lindex]
        Lindex+=1
        i+=1
    
    while Rindex != len(R):
        lst[i] = R[Rindex]
        Rindex+=1
        i+=1
    


lst = [7,5,2,6,9] 
mergesort(lst)
print(lst)
