   #https://www.codingninjas.com/codestudio/problems/day-12-longest-palindromic-substring_8230702?challengeSlug=striver-sde-challenge

   def longestPalinSubstring(s):
        length = len(s)
        def expandPalindrome(i,j):            
            while 0 <= i <= j < length and s[i]==s[j]:
                i -= 1
                j += 1                            
            return (i + 1, j)
        
        result = (0,0)
        for i in range(length):
            b1 = expandPalindrome(i,i)
            b2 = expandPalindrome(i,i + 1)            
            result = max(result, b1, b2, key = lambda x: x[1] - x[0] + 1)
                    
        return s[result[0]:result[1]] 
      
  #firstly i expanded seperately for even length and odd length palindrome
  #for each character in string i expanded that letter for even length and odd length palindrome
  #i took max of even and odd lengths
  #for even length i took two pointers pointing same letter
  #for odd length i took two pointer pointing ith letter and (i + 1)th letter
      
      
      
      
      
      
      
      
      
      
      
      
      
      
