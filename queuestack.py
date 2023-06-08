#https://www.codingninjas.com/codestudio/problems/day-25-queue-using-stack_8230722?challengeSlug=striver-sde-challenge

class Queue:

    def __init__(self):
        self.lst = []
        self.count = 0

    def enQueue(self, val):
        self.lst.append(val)
        self.count += 1

    def deQueue(self):
        if self.lst == []:
            return -1
        self.count -= 1
        return self.lst.pop(0)

    def peek(self):
        if self.lst == []:
            return -1
        return self.lst[0]

    def isEmpty(self):
        return "true" if self.lst == [] else "false"
      
    #i just simply created a list and count variable to keep track of number of elements in list
    
    
    
    
    
    
    
    
