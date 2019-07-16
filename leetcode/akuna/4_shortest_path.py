import math
import heapq

def broadcast_delivery_time(source_id, matrix):
    '''
    param:
        source_id (int) - row index of the node that the message sent from
        matrix (array 2d) - adjacency matrix of the graph, [i][j] is from i to j
    return:
        (int) - minimum time taken to broadcast the information, if cannot, return -1
    '''
    dists = {} # distance dictionary storing shortest path from source_id node to all nodes
    pq = [(0,source_id)] # priority queue

    while pq: # while there's still nodes in it
        if len(dists) == len(matrix):
            break
        
        dist, start = heapq.heappop(pq)
        if start in dists:
            continue
        dists[start] = dist
        for j in range(len(matrix[start])):
            # only go to nodes haven't gone to, and `None` meaning there's no path
            if matrix[start][j] not in dists and matrix[start][j] != None: 
                # note we will add double path, if there's two paths to the same nodes
                # but only kept the shortest one bc of the first(and second maybe) if statement，
                heapq.heappush(pq, (matrix[start][j]+dist, j))

    return max(dists.values()) if len(dists) == len(matrix) else -1

m = [[None, None, 122, None], [None, None, None, 50], [341, None, None, 205], [456, None, 186, None]]
print(broadcast_delivery_time(1,m))