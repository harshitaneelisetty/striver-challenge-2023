#https://www.codingninjas.com/codestudio/problems/prim-s-mst_8230809?challengeSlug=striver-sde-challenge

def prim_mst(adj_list, num_nodes):
    pq = []
    src = 0
    weight = [sys.maxsize] * num_nodes
    parent = [-1] * num_nodes
    in_mst = [False] * num_nodes
    in_mst[src] = True
    heapq.heappush(pq, (0, -src))
    weight[src] = 0

    while len(pq) > 0:
        u = -heapq.heappop(pq)[1]
        in_mst[u] = True

        for v, wt in adj_list[u]:
            if not in_mst[v] and weight[v] > wt:
                weight[v] = wt
                heapq.heappush(pq, (weight[v], -v))
                parent[v] = u

    result = []
    for i in range(1, num_nodes):
        result.append([(parent[i] + 1), (i + 1), (weight[i])])

    return result

def calculatePrimsMST(num_nodes, num_edges, graph):
    adj_list = [[] for _ in range(num_nodes)]

    for i in range(num_edges):
        adj_list[graph[i][0] - 1].append(((graph[i][1] - 1), graph[i][2]))
        adj_list[graph[i][1] - 1].append(((graph[i][0] - 1), graph[i][2]))

    return prim_mst(adj_list, num_nodes)
