  #https://www.codingninjas.com/codestudio/problems/valid-parentheses_8230714?challengeSlug=striver-sde-challenge

  def isValidParenthesis(s):
        sizeOfS = len(s)
        t = [0]*len(s)
        top = -1
        loopUp = {")": "(", "}": "{", "]": "["}
        if(sizeOfS % 2 != 0):
            return False
        else:
            for i in range(0, sizeOfS):
                if (s[i] in ('(', '{', '[')):
                    top += 1
                    t[top] = s[i]
                else:
                    if(t[top] == loopUp[s[i]]):
                        top -= 1
                    else:
                        return False
            if(top != -1):
                return False
        return True
   
  #For each character, if it is an opening parenthesis ('(', '{', '['), i incremented the top variable and pushed the opening parenthesis onto the stack t
  #if the character is a closing parenthesis, i checked if the top element of the stack t matches the corresponding opening parenthesis from the loopUp dictionary.
  #If they match, it means the parentheses are correctly matched, so it decrements the top variable to removed the matched opening parenthesis from the stack
  #If the characters do not match, it means the parentheses are not valid, and the function returns False
  #After iterating through all the characters of the string, i checked if the stack is empty
  #If the top variable is not -1, it means that there are unmatched opening parentheses in the stack
  
  
  
  
  
  
  
  


