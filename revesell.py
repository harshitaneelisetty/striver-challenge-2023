#https://www.codingninjas.com/codestudio/problems/reverse-linked-list_8230724?challengeSlug=striver-sde-challenge

def reverseLinkedList(head):
    prev = None    
    curr = head
    nextt = None
    while curr:
        nextt = curr.next
        curr.next = prev
        prev = curr
        curr = nextt
    return prev
  
  #I implemented iterative approach upating the next ptr of the node
  #I used 3pointers prev, curr, nextt 
  #In each iteration, the i assigned nextt as the next node after curr, then sets the next pointer of curr to prev
  #i processed unit curr becomes null
