  #https://www.codingninjas.com/codestudio/problems/longest-common-prefix_8230847?challengeSlug=striver-sde-challenge

  def longestCommonPrefix(a, n):
        a.sort()
        c = 0
        prefix = ""
        first = a[0]
        last = a[-1]
        length = min(len(first), len(last))
        while c < length:
            if first[c] != last[c]:
                return prefix
            prefix += first[c]
            c += 1
        return prefix
  
  #first i sorted the words in ascending order based on ascii values
  #i took the min length of all words
  #then i started comparing the letters of the first word and last word until the letters are equal
  #i incremented the count
