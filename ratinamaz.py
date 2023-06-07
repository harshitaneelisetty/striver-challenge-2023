#https://www.codingninjas.com/codestudio/problems/rat-in-a-maze-all-paths_8230705?challengeSlug=striver-sde-challenge

def ratInAMaze(maze, n):
    solution = [[0 for j in range(n)] for i in range(n)]
    solveMaze(maze, solution, 0, 0, n)

def solveMaze(maze, solution, x, y, n):
    if x == n - 1 and y == n - 1:
        solution[x][y] = 1
        printSolution(solution, n)
        print("")
        return

    if x > n - 1 or x < 0 or y > n - 1 or y < 0:
        return

    if x > n - 1 or x < 0 or y > n - 1 or y < 0 or maze[x][y] == 0 or solution[x][y] == 1:
        return

    solution[x][y] = 1
    solveMaze(maze, solution, x - 1, y, n)
    solveMaze(maze, solution, x + 1, y, n)
    solveMaze(maze, solution, x, y - 1, n)
    solveMaze(maze, solution, x, y + 1, n)
    solution[x][y] = 0

def printSolution(solution, n):
    for i in range(n):
        for j in range(n):
            print(solution[i][j], end=" ")
        print("")
        
#I used backtracking to solve the problem
#I created ratInAMaze function to initialize a solution matrix and calls the solveMaze function to find all possible paths in the maze.
#In solveMaze function recursively explores all valid paths, 
#and when the destination is reached, I printed the solution
        
        
