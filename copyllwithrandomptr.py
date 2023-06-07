#https://www.codingninjas.com/codestudio/problems/copy-list-with-random-pointer_8230734?challengeSlug=striver-sde-challenge

def cloneRandomList(head):
    curr = head
    temp = None

    while curr is not None:
        temp = curr.next
        curr.next = LinkedListNode(curr.data)
        curr.next.next = temp
        curr = temp

    curr = head

    while curr is not None:
        if curr.next is not None:
            if curr.random is not None:
                curr.next.random = curr.random.next

        if curr.next is not None:
            curr = curr.next.next
        else:
            curr = curr.next

    original = head
    copy = None

    if head is not None:
        copy = head.next

    temp = copy

    while original is not None and copy is not None:
        if original.next is not None:
            original.next = original.next.next

        if copy.next is not None:
            copy.next = copy.next.next

        original = original.next
        copy = copy.next

    return temp
  
  #first i initialsed curr to head and temp to none
  #next i iterated through  the original list
  #For each node, it created a new node with the same data and I inserted after the current node.
  #I updated the next ptr to curr node to the new node and next ptr of the new node to original next node
  #then i moved curr to next origninal node
  #after i reseted curr to head and entered into second while
  #next i reseted original to head and initialised copy to none
  #if head is node none i resedted copy to the cloned head
  #in the final while loop, I adjusted the next pointers of the original list and the cloned list to restore the original list and extracted the cloned lis
  #I updated next ptr of each original node to skip the cloned node
