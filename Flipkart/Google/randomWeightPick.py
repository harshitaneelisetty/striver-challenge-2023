# https://leetcode.com/problems/random-pick-with-weight/description/

class Solution:
    def __init__(self, w: List[int]):
        s = sum(w)
        self.weight = [w[0] / s]
        for i in range(1, len(w)):            
            self.weight.append(self.weight[-1] + w[i] / s)

    def pickIndex(self) -> int:
        ran = random.random()
        return bisect.bisect_left(self.weight, ran)
      
      #  here first I found the probability of each weight and appended to the self.weight
      # then I found the random number between 0, 1 and I searched the index of that random number in self.weight
      # I used bisect_left function which return index 
