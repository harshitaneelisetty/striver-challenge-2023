#https://www.codingninjas.com/codestudio/problems/convert-a-given-binary-tree-to-doubly-linked-list_8230744?challengeSlug=striver-sde-challenge

class LinkedList:

    def __init__(self):
        self.head = None
        self.prev = None

    def find_head(self, root):
        if root is None:
            return

        self.find_head(root.left)

        if self.prev is None:
            self.head = root
        else:
            root.left = self.prev
            self.prev.right = root

        self.prev = root

        self.find_head(root.right)

def BTtoDLL(root):
    linked_list = LinkedList()
    linked_list.find_head(root)
    return linked_list.head
  
#I created find_head method to recursively traverse the binary tree
#setted the head attribute of the linked list to the leftmost node
#and i reconfigured the tree nodes to form the doubly linked list structure
  
  
  
  
  
  
  
  
  
  
  
  
  
  
