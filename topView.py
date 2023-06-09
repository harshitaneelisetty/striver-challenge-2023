   #https://www.codingninjas.com/codestudio/problems/top-view-of-binary-tree_8230721?challengeSlug=striver-sde-challenge
  
   def getTopView(root):
        if root == None:
            return []
        queue = [(0, 0, root)]
        levelElements = {}
        while queue:
            col, row, node = queue.pop(0)
            if col not in levelElements:
                levelElements[col] = node.val
            if node.left:
                queue.append((col - 1, row + 1, node.left))
            if node.right:
                queue.append((col + 1, row + 1, node.right))
        #print(levelElements)
        levelElements = sorted(levelElements.items(), key = lambda x : (x[0], x[1]))
        return [i[1] for i in levelElements]
        return ans

   #i used bfs technique and a queue
   #i done vertical order traversal if i moved to left i decremented level
   #if i moved to right i incremented level
   #it will be like -2, -1, 0, 1, 2
   #then i sorted levels in ascending order
   #i took the first element in each level
