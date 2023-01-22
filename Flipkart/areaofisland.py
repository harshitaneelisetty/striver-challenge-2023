# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = []
        count = 0
        vis = [[-1 for _ in range(m)] for i in range(n)]
        
        def bfs(row, col, vis, grid):
            vis[row][col] = 1
            count = 0
            queue = []
            queue.append([row, col])
            n = len(grid)
            m = len(grid[0])
            while queue:
                r = queue[0][0]
                c = queue[0][1]
                queue.pop(0)
                delRow = [-1, 0, +1, 0] 
                delCol = [0, -1, 0, +1]
                for i in range(4):
                    row = r + delRow[i]
                    col = c + delCol[i]
                    if row >= 0 and row < n and col >= 0 and col < m and vis[row][col] == -1 and grid[row][col] == 1:
                        vis[row][col] = 1
                        queue.append([row, col])
                        count += 1
            return count + 1
        for i in range(n):
            for j in range(m):
                if vis[i][j] == -1 and grid[i][j] == 1:
                    count = max(count, bfs(i, j, vis, grid))
        return count
      
      #here i used bfs technique
      # done bfs if grid[row][col] = 1 and I calculated area and i updated vis array
      # I repeated same process for all the idxes whose value is 1 and it is not visited I done bfs for that element and calculated area
      # updated if area is greater than previous area
