#https://www.codingninjas.com/codestudio/problems/pascal-s-triangle_8230805?challengeSlug=striver-sde-challenge

def print_pascal(n):
    triangle = []
    for i in range(1, n+1):
        coefficient = 1
        temp = []
        for j in range(1, i+1):
            temp.append(coefficient)
            coefficient = coefficient * (i - j) // j

        triangle.append(temp)
    return triangle
 
#I generated Pascal's triangle by iteratively,
# Next by calculating the coefficients for each row and storing them in a nested list, representing each row of the triangle.
