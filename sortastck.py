#https://www.codingninjas.com/codestudio/problems/sort-a-stack_8230787?challengeSlug=striver-sde-challenge

def sortStack(stack):
    stack.sort(reverse = True)
    stack.reverse()
    return stack
  
  #i simply sorted stack using inbuilt function
