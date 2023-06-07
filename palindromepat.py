#https://www.codingninjas.com/codestudio/problems/palindrome-partitioning_8230726?challengeSlug=striver-sde-challenge

  def partition(s):
        result = []
        
        def helper(s,rsofar):
            if len(s) == 0:
                result.append(rsofar)
                return
            #print(rsofar)
            for i in range(len(s)):
                subString = s[ : i + 1]
                if subString == subString[ :: -1]:
                   # print(rsofar + [subString])
                    helper(s[i + 1 : ], rsofar + [subString])
                
        helper(s, [])
        return result
      
   #I recursively partitioned the input string s  into all possible palindrome substrings
   #I checked if a substring is a palindrome by comparing it with its reverse
  
