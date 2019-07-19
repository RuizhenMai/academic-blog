def char2int(c):
    return ord(c) - ord('a')

def constructAdjMatrix(edges):
    '''
    param:
        edges (array of tuples) - consist of a list of directed edges from i[0] to i[1]
    return:
        adjacency matrix (array of array) - [i][j] is edge from i to j
    '''
    res = [[None]*26 for i in range(26)]
    for edge in edges:
        res[char2int(edge[0])][char2int(edge[1])] = 1

    return res

def spellTheWord(words, edges):
    adjMatrix = constructAdjMatrix(edges)
    res = []
    for w in words:
        for i in range(len(w)-1):
            # print(i,char2int(w[i]),char2int(w[i+1]),adjMatrix[char2int(w[i])][char2int(w[i+1])])
            if adjMatrix[char2int(w[i])][char2int(w[i+1])] != 1:
                res.append(0)
                break
        # finished looping all chars in a word
        if len(res) == 0 or res[-1] != 0: # did not append 0 in the for loop
            res.append(1)
    return res

# print(spellTheWord(['a','b','ab','ba'],[('a','b')])) # expect [1,1,1,0]
print(spellTheWord(['what','who','where'],[('w','h'),('h','a'),('h','o'),('a','t'),('h','e')])) 
