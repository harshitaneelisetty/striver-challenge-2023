  #https://www.codingninjas.com/codestudio/problems/linked-list-cycle-ii_8230823?challengeSlug=striver-sde-challenge

  def firstNode(head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
              break
        else:
            return None 
        while head != slow:
            head, slow = head.next, slow.next
        return head
      
   #first i found if cycle is present in linked list using Floyd's cycle detection algorithm
   #After detecting cycle i reseted the head ptr to the head of the ll and moved both head and slow ptr
   #one step at a time until the meet again
   #the node at which they meet is the first node of the cycle.
