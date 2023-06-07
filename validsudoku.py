#https://www.codingninjas.com/codestudio/problems/valid-sudoku_8230704?challengeSlug=striver-sde-challenge

def isValid(matrix, row, col, num):
    for i in range(9):
        if matrix[row][i] == num or matrix[i][col] == num or matrix[(row//3)*3 + i//3][(col//3)*3 + i%3] == num:
            return False
    return True

def solveSudoku(matrix):
    for row in range(9):
        for col in range(9):
            if matrix[row][col] == 0:
                for num in range(1, 10):
                    if isValid(matrix, row, col, num):
                        matrix[row][col] = num
                        if solveSudoku(matrix):
                            return True
                        matrix[row][col] = 0
                return False
    return True

def isItSudoku(matrix):
    matrix_copy = [row[:] for row in matrix]
    return solveSudoku(matrix_copy)
  
#I implemented a recursive backtracking algorithm by filling in empty cells with valid numbers.
#i checked validity of each number placement in the current cell 
#and recursively explores the possibilities until a valid solution is found or all possibilities are completed
#I created isItSudoku function used a copy of the input matrix to preserve the original values and called solveSudoku to determine if a valid Sudoku solution exists.

  
  
  
  
  
