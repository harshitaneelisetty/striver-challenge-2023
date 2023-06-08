#https://www.codingninjas.com/codestudio/problems/rotting-oranges_8230701?challengeSlug=striver-sde-challenge

def minTimeToRot(grid, n, m):
    q = []
    vis = [[0] * m for _ in range(n)]
    countFresh = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                q.append([[i, j], 0])
                vis[i][j] = 2
            else:
                vis[i][j] = 0
            if grid[i][j] == 1:
                countFresh += 1
    time = 0
    drow = [-1, 0, 1, 0]
    dcol = [0, 1, 0, -1]
    count = 0
    while q:
        r = q[0][0][0]
        c = q[0][0][1]
        t = q[0][1]
        time = max(time, t)
        q.pop(0)
        for i in range(4):
            newRow = r + drow[i]
            newCol = c + dcol[i]
            if (
                newRow >= 0
                and newRow < n
                and newCol >= 0
                and newCol < m
                and vis[newRow][newCol] == 0
                and grid[newRow][newCol] == 1
            ):
                q.append([[newRow, newCol], time + 1])
                vis[newRow][newCol] = 2
                count += 1
    if count != countFresh:
        return -1
    return time
  
#here i used bfs taversal. i created a vis array with 0 and queue
#i traversed from starting of the grid, if value of grid[i][j] is 2 it means its an rotten oragne and i appended to queue 
#and i marked it as visited and if grid[i][j] is 1 its a fresh orange and i incremented the fresh count
#then i preceeded with the bfs traversal. i used four direction vectors (drow and dcol) to explore the neighboring cells of each orange
#While the queue q is not empty, i poped the front element, which represents an orange to process
#for each neighboring cell i checked with the grid boundaries, not visited and containes fresh orrange
#If these conditions are met, the neighboring cell's coordinates and the current time plus one popped front of q, and i marked it as visited
#after bfs taversal i checked if the count of frseh oranges is equal to the total count of fresh oranges encountered during the initialization phase
#if they are not equal it means that some fresh oranges were not reached by the bfs traversal







