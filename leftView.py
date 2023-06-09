#https://www.codingninjas.com/codestudio/problems/left-view-of-a-binary-tree_8230757?challengeSlug=striver-sde-challenge

def getLeftView(root)->list:
    level = []
    queue = []
    if root == None:
        return []
    queue.append(root)
    while queue:
        order = []
        for i in range(len(queue)):
            node = queue.pop(0)
            order.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level.append(order[0])
    return level
  
  #i used bfs and level order traversal
  #i traversed tree in level order fashion and took first element in each level
