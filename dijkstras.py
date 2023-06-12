#https://www.codingninjas.com/codestudio/problems/dijkstra-s-shortest-path_8230755?challengeSlug=striver-sde-challenge

def dijkstraHelper(adjacencyList, vertices, source):
    pq = []
    distance = [2147483647 for _ in range(vertices)]
    pq.append([0, source])
    distance[source] = 0
    visited = [False for _ in range(vertices)]

    while len(pq) > 0:
        pair = heapq.heappop(pq)
        u = pair[1]
        visited[u] = True

        for it in adjacencyList[u]:
            v = it[0]
            dist = it[1]

            if not visited[v] and distance[v] > distance[u] + dist:
                distance[v] = distance[u] + dist
                heapq.heappush(pq, (distance[v], v))

    return distance

def dijkstra(vec, vertices, edges, source):
    adjacencyList = [[] for _ in range(vertices)]
    for i in range(len(vec)):
        adjacencyList[vec[i][0]].append([vec[i][1], vec[i][2]])
        adjacencyList[vec[i][1]].append([vec[i][0], vec[i][2]])

    return dijkstraHelper(adjacencyList, vertices, 0)
  
  #i created dijkstraHelper function to perform the actual Dijkstra's algorithm using a priority queue (pq) to store nodes with their distances from the source
  #i iteratively selected the node with the minimum distance, updated the distances of its neighbors if a shorter path is found
  #and marked the node as visited.
  #in dijkstra function i created an adjacency list and called dijkstraHelper function to perform the algorithm
  #i returned array of distances where each element represents the shortest distance from the source
  
  
  
  
  
  
  
  
  
  
  
  
