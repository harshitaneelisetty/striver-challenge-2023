#https://www.codingninjas.com/codestudio/problems/rabin-carp_8230831?challengeSlug=striver-sde-challenge

def stringMatch(a, b):
    ans = []
    for i in range(len(a) - len(b) + 1):
        if a[i : i + len(b)] == b:
            ans.append(i)
    return ans
  
  #i simply checked all substrings in a with length b with b
  #if it matches i appended to ans
