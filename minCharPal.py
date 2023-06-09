#https://www.codingninjas.com/codestudio/problems/minimum-characters-for-palindrome_8230737?challengeSlug=striver-sde-challenge

  def minCharsforPalindrome(str1):
        n = len(str1)
        start = 0
        end = n - 1
        res = 0
        while start < end:  
            if str1[start] == str1[end]: 
                start += 1 
                end -= 1 
            else:
                res += 1  
                start = 0 
                end = n - res - 1  
        return count
      
  #i iterated until start idx is less than end idx
  #in each iteration i checked if the character at index start is equal to the character at index end
  #if they are equal, it means that the current substring is already a palindrome
  #so then incremented the start idx and decremented end idx
  #if the characters are not equal, it means that the substring is not a palindrome
  #in this case i incremented res variable by 1 which indicates that one character needs to be added to make the string a palindrome
  #and resetted start idx 0 to start checking from the beginning of the string again
  #and setted end idx to n - res - 1
  #then i again started iterating.
  
 
