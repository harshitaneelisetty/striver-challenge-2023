#https://www.codingninjas.com/codestudio/problems/middle-of-linked-list_8230764?challengeSlug=striver-sde-challenge

def findMiddle(head):
    slow = head
    fast = head
    while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    return slow
  
  #I used tortoise method which used slow and fast pointers
  #initially pointing to the head of the linked list.
  #In each iteration, slow moves one step forward while fast moves two steps forward.
  #so fast reached end of list when slow reaches middle
