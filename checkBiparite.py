#https://www.codingninjas.com/codestudio/problems/check-bipartite-graph_8230761?challengeSlug=striver-sde-challenge

from collections import deque

def isGraphBipartite(edges):
    n = len(edges)

    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if edges[i][j]:
                graph[i].append(j)
                graph[j].append(i)

    color = [-1] * n

    for i in range(n):
        if color[i] != -1:
            continue
        color[i] = 0

        queue = deque()
        queue.append(i)

        while queue:
            node = queue.popleft()

            for nbr in graph[node]:
                if color[nbr] != -1 and color[nbr] == color[node]:
                    return False
                elif color[nbr] == -1:
                    color[nbr] = 1 - color[node]
                    queue.append(nbr)

    return True
  
#i checked whether a given graph is bipartite by performing a breadth-first search traversal
#and assigned colors to the nodes
#if there is an edge between two nodes of the same color, the graph is not bipartite
  
  
  
  
  
  
  
  
  
  
  
  
  
