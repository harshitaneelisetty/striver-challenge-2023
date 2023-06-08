#https://www.codingninjas.com/codestudio/problems/number-of-distinct-substring_8230842?challengeSlug=striver-sde-challenge

def distinctSubstring(s):
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])
    return len(substrings)

  #i just used bruteforce approach to solve
  #kept 2 for loops to generate all sub strings and i appended each substring in a set to avoid dupilactes
