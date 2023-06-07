  #https://www.codingninjas.com/codestudio/problems/rotate-linked-list_8230752?challengeSlug=striver-sde-challenge
  def rotate(head: Node, k: int) -> Node:
        if not head:
           return
        lastNode = head
        length = 1
        while lastNode.next:
            lastNode = lastNode.next
            length += 1
        k = k % length
        lastNode.next = head
        currNode = head
        for i in range(length - k - 1):
            currNode = currNode.next
        ans = currNode.next
        currNode.next = None
        return ans
    
    #first i checked head is none or not
    #next i travesed linkedlist to find last node and calculated length
    #To handle cases where k is larger than the length of the list
    #I took k % len to get num of rotations
    #then i connected last node to head to make list circular
    #after that i moved currNode to the position before the new head after rotation.
    #traversed list for len - k - 1 steps
    #then i connected cuurNode to none to find new head
