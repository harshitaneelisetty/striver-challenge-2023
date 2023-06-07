#https://www.codingninjas.com/codestudio/problems/delete-node-in-a-linked-list_8230813?challengeSlug=striver-sde-challenge

def deleteNode(node):
    node.data = node.next.data 
    node.next = node.next.next 
    return node
 
#just i assigned the next value to the curr node and joined next to next.next
#so the node will be deleted
