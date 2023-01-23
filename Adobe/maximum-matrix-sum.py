# https://leetcode.com/problems/maximum-matrix-sum/description/

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        zero = 0
        neg = 0
        mini = float('inf')
        total = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                val = matrix[i][j]
                if val < 0:
                    neg += 1
                if val == 0:
                    zero += 1
                val = abs(val)
                total += val
                mini = min(val, mini)
        while zero > 0 and neg % 2 != 0:
            zero -= 1
            neg += 1
        if neg % 2 != 0:
            return total - 2 * mini
        return total
      
      # first I calculated number of zeros and number of negative numbers and min, total values
      #then i multiplited zero and a negative number by 1 ie i decreased coun of 0 and increased count of neg numbers
      # if neg is even we can simply retun total else we subtract min from total
