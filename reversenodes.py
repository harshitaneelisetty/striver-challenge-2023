#https://www.codingninjas.com/codestudio/problems/reverse-nodes-in-k-group_8230709?challengeSlug=striver-sde-challenge

def getListAfterReverseOperation(head,n, block_sizes):
    if head is None:
        return None

    index = 0

    current, previous, temp = head, None, None
    tail, join = None, None
    is_head_updated = False

    while current is not None and index < len(block_sizes):
        block_size = block_sizes[index]

        if block_size == 0:
            index += 1
            continue

        join = current
        previous = None

        while current is not None and block_size > 0:
            block_size -= 1
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        if not is_head_updated:
            head = previous
            is_head_updated = True

        if tail is not None:
            tail.next = previous

        tail = join
        index += 1

    if tail is not None:
        tail.next = current

    return head
 
  #I created a function which iterates through the linked list and the block_sizes list simultaneously.
  #For each block size, it reversed the corresponding block of nodes in the linked list.
  #I maintained pointers current, previous, and temp to keep track of the current node, the previous node, and a temporary node during reversal.
  #I tracked tain and join nodes to corretly join the reversed blocks

