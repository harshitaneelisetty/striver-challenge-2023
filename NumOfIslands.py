#https://www.codingninjas.com/codestudio/problems/find-number-of-islands_8230692?challengeSlug=striver-sde-challenge

def findIslands(grid: List[List[str]], n, m) -> int:
    n = len(grid)
    m = len(grid[0])
    q = []
    count = 0
    vis = [[-1 for _ in range(m)] for i in range(n)]
    
    def bfs(row, col, vis, grid):
        vis[row][col] = 1
        queue = []
        queue.append([row, col])
        n = len(grid)
        m = len(grid[0])
        
        while queue:
            r = queue[0][0]
            c = queue[0][1]
            queue.pop(0)
            delRow = [0, 1, 1, 1, 0, -1, -1, -1]
            delCol = [-1, -1, 0, 1, 1, 1, 0, -1]
            
            for i in range(8):
                row = r + delRow[i]
                col = c + delCol[i]
                
                if row >= 0 and row < n and col >= 0 and col < m and vis[row][col] == -1 and grid[row][col] == '1':
                    print(row, col)
                    vis[row][col] = 1
                    queue.append([row, col])
    
    for i in range(n):
        for j in range(m):
            if vis[i][j] == -1 and grid[i][j] == '1':
                count += 1
                bfs(i, j, vis, grid)
    
    return count
  
  #i created an vis array to update the visited elements in grid
  #i done bfs traversal
  #i started from source and marked it as visited and i explored all its neighbours
  #i checked if those are with in range
  #and i updated queue and vis array
  
  
  
  
  
  
  
  
  
  
