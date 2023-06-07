#https://www.codingninjas.com/codestudio/problems/day-13-print-permutations-string_8230703?challengeSlug=striver-sde-challenge

def findPermutations(s):
    ans = []
    string = list(s)
    permu = permutations(string, len(string))
    for i in list(permu):
        ans.append("".join(i))
    return ans
  
  #I used inbuilt permutation function to generate all permutations
  #then i started iterating in that list
