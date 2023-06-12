#https://www.codingninjas.com/codestudio/problems/floyd-warshall_8230846?challengeSlug=striver-sde-challenge

def floydWarshall(n, m, src, dest, edges):
    d = [[0 if i == j else float('inf') for j in range(n + 1)] for i in range(n + 1)]
    
    for i in range(m):
        u, v, w = edges[i]
        d[u][v] = w
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if d[i][k] != float('inf') and d[k][j] != float('inf'):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    
    return d[src][dest]
  
  #i initialezed a 2D matrix d of size (n+1) x (n+1) to store the shortest path distances between vertices
  #i setted diagonal elements of d to 0 and remaining elements to float('inf")
  #i then updated the distances in d based on the given edges
  #for each edge (u, v, w), where u and v are vertices and w is the weight, i setted d[u][v] to w
  #i applied the Floyd-Warshall algorithm using three nested loops
  #i considerd each vertex k as an intermediate vertex and checked if the path from vertex i to vertex j can be improved by going through vertex k
  #if so i updated the distance d[i][j] to the minimum of the current distance and the sum of distances d[i][k] and d[k][j]
  
