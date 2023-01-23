# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance = [[float('inf') for i in range(n + 1)] for j in range(n + 1)]
        for i in edges:
            distance[i[0]][i[1]] = i[2]
            distance[i[1]][i[0]] = i[2]
        for i in range(n):
            distance[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if distance[i][k] == float('inf') or distance[k][j] == float('inf'):
                        continue
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        cntCity = n
        ciyNo = -1
        for city in range(n):
            count = 0
            for adjCity in range(n):
                if distance[city][adjCity] <= distanceThreshold:
                    count += 1
            if count <= cntCity:
                cntCity = count
                cityNo = city
        return cityNo
      
      # Used Hloyd Warshal Algorithm ( Multi souce shortest path algorithm, it also used to detect negative cycles)
      # values computed by using previous values
      # After generating the 2D matrix using the Floyd Warshall algorithm, 
      #for each node, we will count the number of nodes with a distance lesser or equal to the distanceThreshold by iterating each row of that matrix.
      # finally, I choosen the node with the minimum number of adjacent cities whose distance is at the most distanceThreshold and with the largest value.
