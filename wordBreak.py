#https://www.codingninjas.com/codestudio/problems/word-break_8230808?challengeSlug=striver-sde-challenge

  def wordBreak(wordDict, n, s):
        dp = [True] + [False] * len(s)
        for i in range(len(s) + 1):
            for word in wordDict:
                if i >= len(word) and s[i - len(word) : i] == word:
                    dp[i] = dp[i - len(word)] or dp[i]
        return dp[-1]
      
#i used dp approach 
#i initialsed dp where dp[i] represents whether the substring ending at index i of s can be segmented into words from wordDict
#i iterated throgh indices of s and the words in wordDict. 
#ichecked if a word can be formed at each index by comparing the substring with the word
#and updated dp array accordingly


