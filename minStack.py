#https://www.codingninjas.com/codestudio/problems/min-stack_8230861?challengeSlug=striver-sde-challenge

class MinStack:
    def __init__(self):
        self.stk = []
        self.minStk = []

    def push(self, num):
        self.stk.append(num)
        if not self.minStk or self.minStk[-1] >= num:
            self.minStk.append(num)

    def pop(self):
        if self.minStk and self.minStk[-1] == self.stk[-1]:
            self.minStk.pop()
        if self.stk:
            return self.stk.pop()
        return -1

    def top(self):
        if self.stk:
            return self.stk[-1]
        return -1

    def getMin(self):
        if self.minStk:
            return self.minStk[-1]
        return -1
      
#in init method i initialised two empty lists, stk and minStk, to store the stack elements and the minimum values respectively
#in push method i appended num to the stk. if the minStack list is empty or the top element is greater than or equal to num, i appended num to the minStk list
#in pop method i removed the top element from the stack
# If the top element of minStk is equal to the top element of stk, i removed the top element from minStk
# i then removed and returned the top element from stk if it is not empty. If stk is empty, i returned -1.







