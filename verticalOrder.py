  #https://www.codingninjas.com/codestudio/problems/vertical-order-traversal_8230758?challengeSlug=striver-sde-challenge
  
   def verticalOrderTraversal(root):
        queue = [(0, 0, root)]
        levelElements = defaultdict(list)
        while queue:
            col, row, node = queue.pop(0)
            levelElements[col].append(node.data)
            if node.left:
                queue.append((col - 1, row + 1, node.left))
            if node.right:
                queue.append((col + 1, row + 1, node.right))
        levelElements = sorted(levelElements.items(), key = lambda x : (x[0], x[1]))
        temp = [i[1] for i in levelElements]
        ans = []
        for i in temp:
            ans.extend(i)
        return ans
  
   #i used bfs technique and a queue
   #i done vertical order traversal if i moved to left i decremented level
   #if i moved to right i incremented level
   #it will be like -2, -1, 0, 1, 2
   #then i sorted levels in ascending order
   #i took the elements in each level
