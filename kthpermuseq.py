#https://www.codingninjas.com/codestudio/problems/k-th-permutation-sequence_8230822?challengeSlug=striver-sde-challenge

  def kthPermutation(n, k):
        fact = 1
        num = []
        for i in range(1, n):
            fact *= i
            num.append(i)
        num.append(n)
        k = k - 1
        ans = ""
        while True:
            ans += str(num[k // fact])
            num.pop(k // fact)
            if len(num) == 0:
                break
            k = k % fact
            fact = fact // len(num)
        return ans
      
    #I calculated  the k-th permutation of numbers from 1 to n by generating all permutations in lexicographic order
    #I used factorial based approach to determine the digits of the k-th permutation. 
    #resulting permutation is returned as a string
