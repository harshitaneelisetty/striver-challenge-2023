#https://www.codingninjas.com/codestudio/problems/binary-tree-zigzag-traversal_8230796?challengeSlug=striver-sde-challenge

  def zigZagTraversal(root):
        if root is None:
            return []
        order = []
        queue = [root]
        c = 0
        while queue:
            level = []
            c += 1
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if c % 2 != 0:
                order.append(level)
            else:
                order.append(level[::-1])
        ans = []
        for i in order:
            ans.extend(i)
        return ans
      
#i checked the value of the root if it is none or not
#then i declared queue to store current node in bfs traversal
#i maintained a counter variable c and i done level order traversal
#if counter variable is even i appended elements in cth level as it is
#if counter variable is odd i appended elements in cth level by reversing elemnts
#at atlast returned ans
      
      
      
      
      
      
      
      
      
      
      
