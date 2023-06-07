#https://www.codingninjas.com/codestudio/problems/longest-substring-without-repeating-characters_8230684?challengeSlug=striver-sde-challenge

def uniqueSubstrings(s):
      i = 0
      j = 0
      mx = 0
      charDict = {}
      while j < len(s):
          charDict[s[j]] = charDict.get(s[j], 0) + 1

          if len(charDict) == j - i + 1:
              mx = max(mx, j - i + 1)
          elif len(charDict) < j - i + 1:
              while len(charDict) < j - i + 1:
                  charDict[s[i]] -= 1
                  if charDict[s[i]] <= 0:
                      del charDict[s[i]]
                  i += 1

          j += 1

      return mx
#I used  two pointers i and j to maintain a sliding window and an unordered map charDict to keep track of character frequencies within the window.
#inside the loop, the code updated the frequency of the current character s[j] in charDict
#if the size of charDict is equal to the length of the window (j - i + 1) i updated mx
#if size of char dict is less than window length,  it enters another while loop that moves the i pointer and adjusts charDict until the size matches the length of the window
#It decreases the frequency of s[i] in charDict and removes it from the dictionary if its frequency becomes 0 or less. It then increments i to move the window.
#and i expanded the j value
