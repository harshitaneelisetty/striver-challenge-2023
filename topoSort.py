#https://www.codingninjas.com/codestudio/problems/topological-sort_8230784?challengeSlug=striver-sde-challenge

def topologicalSort(edges, numVertices, numEdges):
    adjacencyList = defaultdict(list)
    
    for i in range(numEdges):
        adjacencyList[edges[i][0]].append(edges[i][1])
    
    indegree = [0] * numVertices
    
    for i in range(numEdges):
        indegree[edges[i][1]] += 1
    
    queue = []
    
    for i in range(numVertices):
        if indegree[i] == 0:
            queue.append(i)
    
    result = []
    
    while len(queue) != 0:
        src = queue.pop(0)
        result.append(src)
        
        for node in adjacencyList[src]:
            indegree[node] -= 1
            if indegree[node] == 0:
                queue.append(node)

    return result
  
  #i implemented topo sort in bfs fashion
  #first i calculated indegree of all nodes
  #then i iterated over nodes and appended node into queue if its indegree is 0
  #then i iterated until queue is empty
  #i appended first node into res list
  #i poped the first node and iterated over the adjacent node of first node and decremented its indegree
  #if the indegree is 0 i appended to queue
  #i returned res list
  
  
  
  
  
