#https://www.codingninjas.com/codestudio/problems/bellman-ford_8230845?challengeSlug=striver-sde-challenge

def bellmonFord(num_vertices, num_edges, src, dest, edges):
    distances = [1000000000] * (num_vertices + 1)
    distances[src] = 0

    for _ in range(1, num_vertices):
        for u, v, w in edges:
            if distances[u] != 1000000000 and distances[v] > (distances[u] + w):
                distances[v] = distances[u] + w

    return distances[dest]
#i implemented Bellman-Ford algorithm to find the shortest path from a source node to a destination node
#i initialized an array distances with a large value for all vertices except the source
#i iterated num_vertices - 1 times and relaxed  the edges by updating the distances if a shorter path is found
#i checked for each edge if the distance to the destination vertex v can be improved by going through vertex u
#finall i returned the distance to the destination node dest from the source node src









