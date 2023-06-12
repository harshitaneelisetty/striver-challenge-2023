#https://www.codingninjas.com/codestudio/problems/clone-graph_8230812?challengeSlug=striver-sde-challenge

class GraphNode:
    def __init__(self, *args):
        if len(args) == 0:
            self.data = 0
            self.neighbours = []
        elif len(args) == 1:
            self.data = args[0]
            self.neighbours = []
        elif len(args) == 2:
            self.data = args[0]
            self.neighbours = args[1]

    def __del__(self):
        self.neighbours.clear()


def clone_graph_helper(node, copies):

    if node is None:
        return None

    copy = GraphNode(node.data)
    copies[node] = copy
    level = Queue()
    level.put(node)

    while not level.empty():
        cur = level.get()

        for neighbor in cur.neighbours:
            if neighbor not in copies:
                copies[neighbor] = GraphNode(neighbor.data)
                level.put(neighbor)

            copies[cur].neighbours.append(copies[neighbor])

    return copy


def cloneGraph(node):
    copies = {}
    return clone_graph_helper(node, copies)
  

  
  
  
  
  
  
  
  
  
  
  
  
