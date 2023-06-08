    #https://www.codingninjas.com/codestudio/problems/next-greater-element_8230718?challengeSlug=striver-sde-challenge
  
    def nextGreater(A,n):
        A = A[::-1]
        stack = []
        ans = [-1] * len(A)
        for i in range(len(A)):
            while stack and stack[-1] <= A[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(A[i])
        return ans[::-1]
      
      #firstly i reversed the list and created on stack to store elements
      #i iterated through list using a loop 
      #for each element ichecked if the stack is not empty and the top element of the stack is less than or equal to the current element 
      #If this condition is true, it means that the current element is the next greater element for the top element of the stack
      #so i poped elements from the stack until the condition failed
      #After this step, if the stack is not empty, it means that the top element of the stack is the next greater element for the current element. So, i assigned stack[-1] to ans[i]
      #finally i pushed curr element onto the stack
      
      
      
      
      
      
      
