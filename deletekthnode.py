#https://www.codingninjas.com/codestudio/problems/delete-kth-node-from-end_8230725?challengeSlug=striver-sde-challenge

class Solution:
  def removeKthNode(head, n):
      start = Node()
      start.next = head
      slow = start
      fast = start
      for i in range(1, n+1):
          fast = fast.next
      while fast.next is not None:
          slow = slow.next
          fast = fast.next
          slow.next = slow.next.next
      return start.next
    
  #I used two pointers slow and fast
  #i moved fast pointer to kth node
  #so then i moved slow pointer one step ahead until fast pointer becomes null
  #it indicates it is the last kth node
  #so i finally returned 
