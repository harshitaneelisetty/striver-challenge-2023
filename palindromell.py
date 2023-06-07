  #https://www.codingninjas.com/codestudio/problems/palindrome-linked-list_8230717?challengeSlug=striver-sde-challenge

          
  def isPalindrome(head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt

        while node:
            if node.data != head.data:
                return False
            node = node.next
            head = head.next
        return True
      
   #firsly i found mid using slow and fast pointers
   #next i reversed the end part
   #next i compared elements of each block simultaneously
  
