def hasThreeOfKind(cards):
    return True if cards[0] == cards[1] == cards[2] else False

def hasPair(cards):
    return True if cards[0] == cards[1] or cards[1] == cards[2] or cards[0] == cards[2] else False

def pokerGame(p1,p2):
    '''
    p1 (array) - three cards from 0-9 assigend to p1
    p2 (array) - assigned to p2
    '''
    p1.sort(reverse = True)
    p2.sort(reverse = True)

    rankp1 = 0 
    rankp2 = 0
    
    if hasPair(p1):
        rankp1 = 1
    
    if hasPair(p2):
        rankp2 = 1

    if hasThreeOfKind(p1):
        rankp1 = 2
    
    if hasThreeOfKind(p2):
        rankp2 = 2
    

    if rankp1 == rankp2 == 1:
        flag1 = 0 if p1[0] == p1[1] else 1
        flag2 = 0 if p2[0] == p2[1] else 1

        if p1[flag1] == p2[flag2]:
            flag1 = flag1 + 2 if flag1 == 0 else flag1 - 1
            flag2 = flag2 + 2 if flag2 == 0 else flag2 - 1

        return 1 if p1[flag1] > p2[flag2] else 2

    elif rankp1 == rankp2: # 0 or 2 rank
        i = 0
        while p1[i] == p2[i]:
            i+=1
        
        if i==len(p1): # all same cards, draw new card
            pass 
        
        return 1 if p1[i] > p2[i] else 2

    return 1 if rankp1 > rankp2 else 2

print('Player')
print(pokerGame([1,2,3],[0,2,3])) # expect player 1 win
print('win')