#https://www.codingninjas.com/codestudio/problems/stack-using-queue_8230715?challengeSlug=striver-sde-challenge

class Stack:
    def __init__(self):
        self.lst = []
        self.count = 0
        
    def getSize(self):
        return self.count
      
    def isEmpty(self):
        return "true" if self.lst == [] else "false"
      
    def push(self,ele):
        self.lst.append(ele)
        self.count += 1
        
    def pop(self):
        if self.lst == []:
            return -1
        self.count -= 1
        return self.lst.pop()
        
    def top(self):
        if self.lst == []:
            return -1
        return self.lst[-1]
    
    #just i used simple lists and created a count variable to keep track of number of elements
    
    
    
    
    
    
    
      
    
