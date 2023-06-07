#https://www.codingninjas.com/codestudio/problems/n-queens_8230707?challengeSlug=striver-sde-challenge

def addSolution(n, result, row):
    currentSolution = []
    for i in range(n):
        for j in range(n):
            if row[j] == i:
                currentSolution.append(1)
            else:
                currentSolution.append(0)
    result.append(currentSolution)

def solve(col, n, result, row, d1, d2):
    if col == n:
        addSolution(n, result, row)
        return
    for i in range(n):
        if row[i] == -1 and d1[col - i + n - 1] == -1 and d2[col + i] == -1:
            row[i] = d1[col - i + n - 1] = d2[col + i] = col
            solve(col + 1, n, result, row, d1, d2)
            row[i] = d1[col - i + n - 1] = d2[col + i] = -1

def solveNQueens(n):
    result = []
    row = [-1] * 30
    d1 = [-1] * 30
    d2 = [-1] * 30
    solve(0, n, result, row, d1, d2)
    return result
  
  #I used mplements a backtracking algorithm, which finds all possible solutions for placing N queens on an NxN chessboard without attacking each other.
  #i used  recursion and maintained arrays to track the positions of queens in each row and diagonal to ensure valid placements
  #i stored solutions in a list
  
