#https://www.codingninjas.com/codestudio/problems/dfs-traversal_8230690?challengeSlug=striver-sde-challenge

def helper(vertex, visited, single_component, graph):
    visited[vertex] = True
    single_component.append(vertex)

    for child in graph[vertex]:
        if not visited[child]:
            helper(child, visited, single_component, graph)


def depthFirstSearch(V, E, edges):
    graph = [[] for _ in range(V + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    components = []
    visited = [False for _ in range(V + 1)]

    for vertex in range(V):
        if not visited[vertex]:
            single_component = []
            helper(vertex, visited, single_component, graph)
            single_component.sort()
            components.append(single_component)

    return components

  #i used helper function to perform dfs starting from a given vertex
  #i marked the vertex as visited, and i appended it to the single_component list
  #then i recursively called function itself for all unvisited neighboring vertices
  #in depthFirstSearch i created an adjacency list representation of the graph using the edges input
  #i maintained a visited list to keep track of visited vertices
  #then, for each vertex in the graph, if it is not visited, i called the helper function to perform DFS and collected all the vertices in that connected component
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
