#https://www.codingninjas.com/codestudio/problems/stack-implementation-using-array_8230854?challengeSlug=striver-sde-challenge


class Stack:
    
    def __init__(self, capacity: int):
        self.stack = []
        self.topp = -1
        self.n = capacity

    def push(self, num: int) -> None:
        self.topp += 1
        if len(self.stack) >= self.n:
            return
        self.stack.append(num)

    def pop(self) -> int:
        self.topp -= 1
        if self.stack == []:
            return -1
        x = self.stack.pop()
        return x
    
    def top(self) -> int:
        if self.stack == []:
            return -1
        return self.stack[-1]
    
    def isEmpty(self) -> int:
        # Write your code here.
        return 1 if self.stack == [] else 0
    
    def isFull(self) -> int:
        # Write your code here.
        return 1 if len(self.stack) == self.n else 0
  
  #simply i performed stack operations push and pop using array
  
  
  
  
  
