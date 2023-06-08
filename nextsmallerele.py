       #https://www.codingninjas.com/codestudio/problems/next-smaller-element_8230814?challengeSlug=striver-sde-challenge

       def nextSmallerElement(arr,n):
        stack = []
        ans = []
        for i in arr[::-1]:
            while stack and stack[-1] >= i:
                stack.pop()
            if stack == []:
                ans.append(-1)
            else:
                ans.append(stack[-1])
            stack.append(i)
        return ans[::-1]

      #firstly i reversed the list and created on stack to store elements
      #i iterated through list using a loop 
      #for each element ichecked if the stack is not empty and the top element of the stack is greater than or equal to the current element 
      #If this condition is true, it means that the current element is the next smallerr element for the top element of the stack
      #so i poped elements from the stack until the condition failed
      #After this step, if the stack is not empty, it means that the top element of the stack is the next smaller element for the current element. So, i assigned stack[-1] to ans[i]
      #finally i pushed curr element onto the stack
      
