#https://www.codingninjas.com/codestudio/problems/edit-distance_8230685?challengeSlug=striver-sde-challenge

   def editDistance(word1, word2) :
        dp = [
            [-1 for _ in range(len(word2) + 1)]
            for _ in range(len(word1) + 1)
        ]
        
        def helper(idx1, idx2, word1, word2, dp):
            if idx1 < 0:
                return idx2 + 1
            if idx2 < 0:
                return idx1 + 1
            if dp[idx1][idx2] != -1:
                return dp[idx1][idx2]
            if word1[idx1] == word2[idx2]:
                dp[idx1][idx2] = helper(idx1 - 1, idx2 - 1, word1, word2, dp)
                return dp[idx1][idx2]
            else:
                dp[idx1][idx2] = min(1 + helper(idx1, idx2 - 1, word1, word2, dp), 1 + helper(idx1 - 1, idx2, word1, word2, dp),1 + helper(idx1 - 1, idx2 - 1, word1, word2, dp))
                return dp[idx1][idx2]
            
        return helper(len(word1) - 1, len(word2) -1, word1, word2, dp)
      
    #in editDistance i initialized 2d dp table to store the intermediate results
    #then i called helper function recursively to calculate the edit distance between the two input words
    #i considered three possible operations insertion, deletion, and substitution
    #i took min of 3 operations at particular point and stored in dp
   
    
    
    
    
    


