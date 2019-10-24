import math

def waitingTickets(tickets, p):
    counter = 0
    alex = tickets[p]

    for iters in range(alex):
        for i in range(len(tickets)):
            if iters == alex -1 and i>p:
                break
            tickets[i] -=1
            counter+=1



    # right now tickets[p] = 0
    for i in range(len(tickets)):
        if tickets[i] < 0:
            counter += tickets[i]
        # if i>p:
        #     counter-=1

    print(tickets)
    return counter

tickets = [2,6,3,4,5] #[3,5,1,6,1]
tickets = [3,5,1,6,1]
p = 1
print(waitingTickets(tickets,p))