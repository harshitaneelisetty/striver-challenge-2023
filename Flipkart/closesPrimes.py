# https://leetcode.com/problems/closest-prime-numbers-in-range/description/

class Solution:
    def getPrimes(self, left, right):
        lst = []
        right = right + 1
        prime = [True for i in range(right + 1)]
     
        p = 2
        while(p * p <= right):
            if (prime[p] == True):
                for i in range(p * p, right + 1, p):
                    prime[i] = False
            p += 1
        c = 0
        for p in range(2, right):
            if prime[p]:
                c += 1
                lst.append(p)
        return lst
    
    def closestPrimes(self, left: int, right: int) -> List[int]:
        #dic = defaultdict(list)
        primes = self.getPrimes(left, right)
        mn = float('inf')
        for i in range(1, len(primes)):
            c = primes[i] - primes[i - 1] 
            if c < mn and primes[i - 1] >= left:
                ans = [primes[i - 1], primes[i]]
                mn = c
            #dic[primes[i] - primes[i - 1]].append([primes[i - 1], primes[i]])
            #mn = min(mn, primes[i] - primes[i - 1])
        try:
            if ans:
                return ans
        except:
            return [-1, -1]
          
          # generated all primes using sieve method(optimal approach to find prime numbers in range)
          # then from starting checked the difference between the pairs and stored the minimum value and pair in ans 
