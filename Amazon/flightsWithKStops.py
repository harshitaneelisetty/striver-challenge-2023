# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for i in flights:
            adj[i[0]].append([i[1], i[2]])
        distance = [float('inf')] * n
        distance[src] = 0
        queue = []
        queue.append([0, [src, 0]])
        while queue:
            steps = queue[0][0]
            node = queue[0][1][0]
            dist = queue[0][1][1]
            queue.pop(0)
            if steps > k:
                continue
            for i in adj[node]:
                adjNode = i[0]
                edgWeight = i[1]
                if dist + edgWeight < distance[adjNode] and steps <= k:
                    distance[adjNode] = dist + edgWeight
                    queue.append([steps + 1, [adjNode, dist + edgWeight]])
        if distance[dst] == float('inf'):
            return -1
        return distance[dst]
      # used the modified h=version of djkstra algorithm
