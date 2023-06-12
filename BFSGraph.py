#https://www.codingninjas.com/codestudio/problems/bfs-in-graph_8230763?challengeSlug=striver-sde-challenge

def print_BFS_helper(edges, source, visited):
    queue = []
    visited[source] = True
    queue.append(source)

    while len(queue) != 0:
        front = queue.pop(0)
        result.append(front)

        for i in range(len(edges)):
            if edges[front][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)

def create_adjacency_matrix(vertex, edges):
    adjacency_matrix = [[0] * vertex for _ in range(vertex)]

    for i in range(len(edges[0])):
        adjacency_matrix[edges[0][i]][edges[1][i]] = 1
        adjacency_matrix[edges[1][i]][edges[0][i]] = 1

    return adjacency_matrix


def BFS(vertex, edges):
    adjacency_matrix = create_adjacency_matrix(vertex, edges)
    visited = [False] * len(adjacency_matrix)

    for i in range(len(visited)):
        if not visited[i]:
            print_BFS_helper(adjacency_matrix, i, visited)

    return result
  
  #in print_BFS_helper function i implemented the BFS algorithm by using a queue to visit vertices in a breadth-first manner
  #marked them as visited and enqueued their neighbors
  #i created bfs function created the adjacency matrix from the given edges and initialized a visited list
  #i then iterated through each vertex and if it is not visited called the print_BFS_helper function to perform BFS 
  #from that vertex, collected the traversal order in the result list and returned it
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
