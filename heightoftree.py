#https://www.codingninjas.com/codestudio/problems/height-of-the-binary-tree-from-inorder-and-level-order-traversal_8230730?challengeSlug=striver-sde-challenge

def heightOfTheTree(inorder, levelOrder, N):
    q = Queue()
    init = Node()
    init.height = 0
    init.left_index = 0
    init.right_index = N - 1
    q.put(init)
    pos = [0] * (N + 1)
    
    for i in range(N):
        pos[inorder[i]] = i
        
    max_height = 0
    
    for i in range(N):
        curr = levelOrder[i]
        now = q.get()
        curr_pos = pos[levelOrder[i]]
        
        if curr_pos > now.left_index:
            new_node = Node()
            new_node.height = now.height + 1
            max_height = max(max_height, new_node.height)
            new_node.left_index = now.left_index
            new_node.right_index = curr_pos - 1
            q.put(new_node)
        
        if curr_pos < now.right_index:
            new_node = Node()
            new_node.height = now.height + 1
            max_height = max(max_height, new_node.height)
            new_node.left_index = curr_pos + 1
            new_node.right_index = now.right_index
            q.put(new_node)
            
    return max_height

#i initialized queue to store nodes during the bfs tarversal
#i created an initial node init and with a initial height 0, i setted left_index and right_index attributes to represent the range of indices for the current subtree
#i appended init node to the queue
#i cretaed a array pos with size N + 1 to store the indices of the nodes in the inorder traversal
#i populated pos array, for each element inorder[i] i stored the corresponding position in the inorder traversal in pos array
#i initialized max_height variable to 0 
#i used another loop to process each element in the levelOrder traversal
#i stored curr element in curr variable and poped first node from queue, this node represents the current subtree being processed
#i obtained pos of curr element in inorder traversal and i stored it in curr posi
#if the curr_pos is greater than the left_index of the current node, it means there are elements on the left subtree
#in this case i created a new Node object, representing the left child of the current node
#i setted height of new node to now.height + 1 representing an increase in height from the current node
#if the curr_pos is greater than the right_index of the current node, it means there are elements on the right subtree
#in this case i created a new Node object, representing the right child of the current node
#i setted height of new node to now.height + 1 representing an increase in height from the current node

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
