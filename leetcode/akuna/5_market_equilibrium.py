def market_equilibrium(init_state, markov_matrix):
    '''
    init_state (1d array) - initial state of the population
    markov_matrix (2d array) - probability of staying and moving 
    '''
    state_t = [e for e in init_state] # same dimension as init_state
    for t in range(100):
        # since we update one element of state_t at a time, but we need the old elem for multiplication
        state_t_copied = [e for e in state_t] 
        for i in range(len(init_state)):
            state_t[i] = sum([markov_matrix[j][i] * state_t_copied[j] for j in range(len(init_state))]) # inner product of vector
    
    return state_t

init = [0.4,0.6]
m = [[0.8,0.2],[0.1,0.9]]
print(market_equilibrium(init, m)) # expect 0.333 0.667

