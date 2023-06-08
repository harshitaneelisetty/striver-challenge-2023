#https://www.codingninjas.com/codestudio/problems/implement-a-queue_8230848?challengeSlug=striver-sde-challenge

class Queue :
    def __init__(self):
        self.lst = []

    def isEmpty(self) :
        return self.lst == []

    def enqueue(self, data) :
        self.lst.append(data)
        #Implement the enqueue(element) function

    def dequeue(self) :
        if self.lst == []:
            return -1
        return self.lst.pop(0)
        #Implement the dequeue() function

    def front(self) :
        if self.lst == []:
            return -1
        return self.lst[0]
        #Implement the front() function

 #simply i created array and done enqueue and dequeue operation
        
        
        
        
        
