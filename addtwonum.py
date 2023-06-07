  #https://www.codingninjas.com/codestudio/problems/add-two-numbers-as-linked-lists_8230833?challengeSlug=striver-sde-challenge

  def addTwoNumbers(l1: Node, l2: Node) -> Node:
        dummy = Node()
        temp = dummy
        s = 0
        carry = 0
        while l1 or l2 or carry == 1:
            s = 0
            if l1:
                s += l1.data
                l1 = l1.next
            if l2:
                s += l2.data
                l2 = l2.next
            s += carry
            carry = s // 10
            newNode = Node(s % 10)
            temp.next = newNode
            temp = temp.next
        return dummy.next
      
   #I created a dummy node 
   #I iterated through the two linked list while keeping tracj of carry and retuned a new linkedlist
    #I created linkedlist by performing digit-wise addition with carry propagation.
    
