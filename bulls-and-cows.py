# https://leetcode.com/problems/bulls-and-cows/description/

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secretCount = Counter(secret)
        bullsCount = 0
        extraElement = ""
        cowsCount = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bullsCount += 1
                secretCount[secret[i]] -= 1
            else:
                extraElement  += guess[i]
        for i in range(len(extraElement )):
            if secretCount[extraElement [i]] > 0:
               # print(extra[i], secretCount)
                cowsCount += 1
                secretCount[extraElement [i]] -= 1
        #print(bullsCount)
        return str(bullsCount) + "A" + str(cowsCount) + "B" 
  
  # stored the extra element ie, element present in secret but not equal to guess.
  # traversed in extra elements and checked if those are present in guess or not.
