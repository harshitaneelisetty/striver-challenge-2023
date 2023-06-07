#https://www.codingninjas.com/codestudio/problems/merge-two-sorted-linked-lists_8230729?challengeSlug=striver-sde-challenge

  def sortTwoLists(first, second):
        dummy = final = Node(0)
        temp1 = first
        temp2 = second
        while temp1 and temp2:
            if temp1.data > temp2.data:
                dummy.next = temp2
                temp2 = temp2.next
            else:
                dummy.next = temp1
                temp1 = temp1.next
            dummy = dummy.next
        dummy.next = temp1 or temp2
        return final.next
      
   #Firstly, i created a dummy node and kept track of curr node using final ptr
   #i initialised two ptrs temp1, and temo2 to head
   #I i compared values of temp1 and temp2, i created node with smallest value and increased that ptr
   #I processed until temp1 or temp2 becomes null
