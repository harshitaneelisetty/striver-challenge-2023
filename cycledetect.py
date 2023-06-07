#https://www.codingninjas.com/codestudio/problems/cycle-detection-in-a-singly-linked-list_8230683?challengeSlug=striver-sde-challenge

def detectCycle(head):
    if head is None or head.next is None:
        return False
    slowPtr = head
    fastPtr = head.next
    while slowPtr != fastPtr:
        if fastPtr is None or fastPtr.next is None:
            return False
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next

    return True
  
  #I used the "Floyd's Tortoise and Hare" algorithm to determine if there is a cycle in the list
  #i maintained slow and fast ptr where slow ptr moves one step and fast ptr moves two steps at a time
  #if there is a cycle, the two pointers will eventually meet at the same node
  #if there is no cycle wither fast or fast,next becoe null before they meet
