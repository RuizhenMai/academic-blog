

# ballots = [[1,4,3,-1,-1],[2,1,-1,-1,-1],[1,3,2,0,-1],[3,1,4,0,2],[2,3,4,0,-1],[2,-1,-1,-1,-1,-1]]
ballots = [[1,4,3,-1,-1],[2,1,-1,-1,-1],[1,3,2,0,-1],[3,2,4,0,1],[2,3,4,0,-1]]

def rankedVoting(num_candidates, num_ballots, ballots):
    '''
    ballots shape: (nums_ballots x num_candidates)
    '''
    candidates = [0] * num_candidates # how many votes each candidate they receive, changing every round
    deleted = [0] * num_candidates
    rounds = [0] * num_ballots # rounds for each ballot 


    majority = [0.0] * num_candidates # this is the ans and will be the percentage the second place accounting for 
    
    iters = 0
    while sum(deleted) != 1 * num_candidates: # all candidates deleted
        candidates = [0] * num_candidates 
        print("rounds",rounds)
        for i in range(num_ballots):
            votedIdx = ballots[i][rounds[i]]
             # 999 is invalid
            if votedIdx != -1 and deleted[votedIdx] != 1:
                candidates[votedIdx] += 1

        print("candidates", candidates)
        
        majority = [i/num_ballots for i in candidates]
        print("majority",majority)
        # find the second largest
        maxi = second = nonzero = 0
        for elem in majority:
            if elem != 0:
                nonzero += 1

            if elem > maxi:
                second = maxi
                maxi = elem
            elif elem > second: # original algo should have elem != maxi
                second = elem 

        if maxi > second and nonzero == 2:
            print(second, majority.index(maxi))
            return second 


        # only needed to be performed in the first round
        for j in range(num_candidates):
            if candidates[j] == 0:
                candidates[j] = 999 # so min(candidates) will return the approriate one 
                deleted[j] = 1
    
        leasteVotes = min(candidates)
        for j in range(num_candidates):
            if candidates[j] == leasteVotes:
                candidates[j] = 999 # so min(candidates) will return the approriate one 
                deleted[j] = 1

        
        # move the ballots whose voted candidates is deleted
        for i in range(num_ballots):
            votedIdx = ballots[i][rounds[i]] 
            if deleted[votedIdx] == 1:
                rounds[i] += 1 # if ballots[i][rounds[i]] 
        
        iters+=1 

    print(-1)
    return -1


            


rankedVoting(5,len(ballots),ballots)