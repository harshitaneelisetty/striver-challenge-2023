#https://www.codingninjas.com/codestudio/problems/power-set_8230797?challengeSlug=striver-sde-challenge

def pwset(lst):
    powerSet = []
    for r in range(len(lst) + 1):
        subsets = combinations(lst, r)
        powerSet.extend(subsets)
    return list(powerSet)
  
  #i used combination function to generate all combinations
  #and i appended to the set to avoid duplicates
