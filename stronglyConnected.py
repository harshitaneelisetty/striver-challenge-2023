#https://www.codingninjas.com/codestudio/problems/strongly-connected-components-tarjan-s-algorithm_8230789?challengeSlug=striver-sde-challenge

def dfs(graph, node, disc, low, in_stack, node_stack, ans):
    global discovery_time
    disc[node] = discovery_time
    low[node] = discovery_time

    discovery_time += 1

    node_stack.append(node)
    in_stack[node] = True

    for v in graph[node]:
        if disc[v] == -1:
            dfs(graph, v, disc, low, in_stack, node_stack, ans)
            low[node] = min(low[node], low[v])
        elif in_stack[v]:
            low[node] = min(low[node], disc[v])

    if low[node] == disc[node]:
        component = []
        u = 0
        while node_stack[-1] != node:
            u = node_stack[-1]
            del node_stack[-1]
            in_stack[u] = False
            component.append(u)

        u = node_stack[-1]
        del node_stack[-1]
        in_stack[u] = False
        component.append(u)
        ans.append(component)


def stronglyConnectedComponents(num_vertices, edges):
    graph = [[] for _ in range(num_vertices)]

    for edge in edges:
        graph[edge[0]].append(edge[1])

    disc = [-1] * num_vertices
    low = [-1] * num_vertices
    node_stack = []
    in_stack = [False] * num_vertices

    ans = []
    for i in range(num_vertices):
        if disc[i] == -1:
            dfs(graph, i, disc, low, in_stack, node_stack, ans)

    return ans
  
  #i implemented Tarjan's algorithm to find strongly connected components in a directed graph
  #i performed DFS traversal on the graph by keeping track of the discovery time and low value for each node
  #i added nodes to a stack as they are visited
  #and when a strongly connected component is identified
  #i extracted from the stack and added to the res
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
