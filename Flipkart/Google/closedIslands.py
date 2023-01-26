# https://leetcode.com/problems/number-of-closed-islands/description/

class Solution:
    def inMatrix(self, x, y, m, n):
        if x < 0 or y < 0:
            return False
        if x >= m or y >= n:
            return False
        return True
        
    def bfs(self, grid, visited, start):
        queue = [start]
        visited[start[0]][start[1]] = True
        dX = [0, 0, -1, 1]
        dY = [-1, 1, 0, 0]
        close = True 
        while queue:
            curr = queue.pop(0)
            for i in range(4):
                x = curr[0] + dX[i]
                y = curr[1] + dY[i]
                if not self.inMatrix(x, y, len(grid), len(grid[0])): 
                    close = False
                elif not visited[x][y]:
                    visited[x][y] = True			
                    if not grid[x][y]:
                        queue.append([x, y])
        return close

    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = [[False] * len(grid[0]) for i in range(len(grid))]
        closedIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j]:
                    visited[i][j] = True
                    if not grid[i][j]:
                        if self.bfs(grid, visited, [i,j]):
                            closedIslands += 1
        return closedIslands 
      
      #used bfs to solve
