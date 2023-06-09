#https://www.codingninjas.com/codestudio/problems/level-order-traversal_8230716?challengeSlug=striver-sde-challenge

def getLevelOrder(root):
    if root == None:
        return []
    ans = []
    queue = []
    queue.append(root)
    while queue:
        order = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            order.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans.extend(order)
    return ans
  
#first i checked whether root is none or not
#next i declared queue inorder to process bfs traversal
#i appended current root to the queue 
#and i iterated through the queue until it becomes empty
#and i declared order inside the loop to store elements in one level
#then i iterated for len(queue) times
#i poped current node from the queue and appended its value to the order list
#then if node has left i appended its left child to queue
#if node has right i appended its right child to the queue
#at last i appended orderlist to ans
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
