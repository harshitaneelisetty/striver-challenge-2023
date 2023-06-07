#https://www.codingninjas.com/codestudio/problems/intersection-of-two-linked-lists_8230688?challengeSlug=striver-sde-challenge

def length(head):
    length = 0
    while head is not None:
        head = head.next
        length += 1
    return length

def findIntersection(firstHead, secondHead):
    firstListLength = length(firstHead)
    secondListLength = length(secondHead)
    
    while firstListLength > secondListLength:
        firstHead = firstHead.next
        firstListLength -= 1
        
    while firstListLength < secondListLength:
        secondHead = secondHead.next
        secondListLength -= 1
        
    while firstHead != secondHead:
        firstHead = firstHead.next
        secondHead = secondHead.next
    
    return firstHead
#I created length function calculates the length of a linked list by iterating through it.
#I adjusted their starting points to align them
#and the i iterated through them to find the intersection node

