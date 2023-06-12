#https://www.codingninjas.com/codestudio/problems/cycle-detection-in-undirected-graph_8230798?challengeSlug=striver-sde-challenge

def find_parent(i, parent):
    if i == parent[i]:
        return i
    parent[i] = find_parent(parent[i], parent)
    return parent[i]


def cycleDetection(edges, num_vertices, num_edges):
    parent = [0] * (num_vertices + 1)
    rank = [0] * (num_vertices + 1)

    for i in range(num_vertices + 1):
        rank[i] = 1
        parent[i] = i

    for ar in edges:
        u = ar[0]
        v = ar[1]

        p1 = find_parent(u, parent)
        p2 = find_parent(v, parent)

        if p1 != p2:
            if rank[p1] < rank[p2]:
                parent[p1] = p2
            elif rank[p1] > rank[p1]:
                parent[p2] = p1
            else:
                parent[p1] = p2
                rank[p2] += 1
        else:
            return "Yes"

    return "No"
  
#i implemented a cycle detection algorithm using the disjoint-set union (DSU) data structure
#i created find_parent function to recursively finds the parent of a given element in the set and performed path compression for optimization
#i created cycleDetection function to initialize the parent and rank arrays for each vertex
#i iterated through the edges and checked if the vertices are already connected or not
#if they are not connected, i performed a union operation by updating the parent and rank arrays
#if a cycle is detected during this process i returned Yes
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

  
  
  
  
  
  
  
