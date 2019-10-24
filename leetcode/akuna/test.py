import math
def compressedString(message):
    # Write your code here
    res = [[message[0],1]]
    for i in range(1,len(message)):
        if message[i] == message[i-1]:
            res[-1][1] += 1
        else:
            res.append([message[i],1])
    
    seq = []
    for i in res:
        seq.append(i[0])
        if i[1] > 1:
            seq.append(str(i[1]))
    
    print("".join(seq))
            


def getIdealNums(l, r):
    # Write your code here
    res = []
    for i in range(l, r+1):
        if math.log(i) % math.log(3) == 0 or math.log(i) % math.log(5) == 0:
            res.append(i)
        
        else:
            curr = math.log(i)
            while curr > 0:
                curr = curr - math.log(3) 
                if curr % math.log(5)==0:
                    res.append(i)
                
            
    
    return len(res)

[[1,1,1,1,1],
 [1,1,1,0,1],
 [1,1,1,0,1],
 [1,1,1,0,1],
 [1,1,1,0,1]]




