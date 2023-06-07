#https://www.codingninjas.com/codestudio/problems/rotate-matrix_8230774?challengeSlug=striver-sde-challenge

def rotateMatrix(mat, n, m):
    row = 0
    col = 0

    while (row < n and col < m):
        if (row == n - 1 or col == m - 1):
            break

        previous = mat[row + 1][col]

        for i in range(col, m):
            current = mat[row][i]
            mat[row][i] = previous
            previous = current

        row += 1

        for i in range(row, n):
            current = mat[i][m-1]
            mat[i][m-1] = previous
            previous = current

        m -= 1

        if (row < n):
            for i in range(m-1, col-1, -1):
                current = mat[n-1][i]
                mat[n-1][i] = previous
                previous = current

        n -= 1

        if (col < m):
            for i in range(n-1, row-1, -1):
                current = mat[i][col]
                mat[i][col] = previous
                previous = current

        col += 1
    
    #I used the "In-place Matrix Rotation" algorithm,
    #I first rotated elements of the matrix layer by layer starting from outermost layer towards center
    #I used 4 loops to perform operations on each layer
    #I swpped the elements to achieve the rotation
