#https://www.codingninjas.com/codestudio/problems/find-pattern-in-string-kmp-algorithm_8230819?challengeSlug=striver-sde-challenge

def findPattern(s:str, p:str):
    return "YES" if p.find(s) != -1 else "NO"
 
#just i simply found wheather s is present in p or not using find function
