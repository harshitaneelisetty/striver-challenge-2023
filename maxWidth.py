#https://www.codingninjas.com/codestudio/problems/maximum-width-in-binary-tree_8230710?challengeSlug=striver-sde-challenge

def getMaxWidth(root):
    if root is None:
        return 0
    q = queue.Queue()
    q.put(root)
    max_width = 0
    while not q.empty():
        current_width = q.qsize()
        if max_width < current_width:
            max_width = current_width
        while current_width > 0:
            current_node = q.get()
            if current_node.left is not None:
                q.put(current_node.left)   
            if current_node.right is not None:
                q.put(current_node.right)
            current_width = current_width - 1
    return max_width
  
  #i started by checking the value of the root, if root is none it means the tree is empty so i returned 0
  #i implemented queue to store the nodes during the bfs traversal
  #i pushed root into the queue
  #i looped the queue until it becomes empty
  #inside the loop i assigned current-width to the currentsize of queue
  #if the current_width is greater than the current max_width, it means the current level has a greater width, so i updated current_width to the max_width 
  #next i iterated loop for current_width times
  #in innerloop i dequed the current_node from queue
  #if the current_node has a left child i appended to the queue
  #if the current_node has a right childd i appended to the quee
  #after processing the current node and appending its children i decremented current width by 1 and moved to the nexr node in curr level
  
  
  
  
  
  
  
  
  
  
