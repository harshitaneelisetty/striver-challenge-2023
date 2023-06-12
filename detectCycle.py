#https://www.codingninjas.com/codestudio/problems/detect-cycle-in-a-directed-graph_8230794?challengeSlug=striver-sde-challenge

from collections import defaultdict
 
class Graph():

    def __init__(self, numNodes):
        self.adjacencyList = defaultdict(list)
        self.numNodes = numNodes
 
    def addEdge(self, u, v):
        self.adjacencyList[u].append(v)
 
    def isCyclic(self):
        inDegree = [0] * self.numNodes

        for u in range(self.numNodes):
            for v in self.adjacencyList[u]:
                inDegree[v] += 1

        zeroInDegreeQ = []

        for i in range(self.numNodes):
            if inDegree[i] == 0:
                zeroInDegreeQ.append(i)

        cnt = 0
        topoOrdering = []

        while zeroInDegreeQ:
            u = zeroInDegreeQ.pop(0)

            for v in self.adjacencyList[u]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    zeroInDegreeQ.append(v)
            cnt += 1

        if cnt != self.numNodes:
            return True
        
        return False
        


def detectCycleInDirectedGraph(numNodes, edges):
    graph = Graph(numNodes)
    numEdges = len(edges)

    for i in range(numEdges):
        graph.addEdge(edges[i][0] - 1, edges[i][1] - 1)

    return graph.isCyclic()
  
  #i implemented topo sort in bfs fashion
  #first i calculated indegree of all nodes
  #then i iterated over nodes and appended node into queue if its indegree is 0
  #then i iterated until queue is empty
  #i appended first node into toposort list
  #i poped the first node and iterated over the adjacent node of first node and decremented its indegree
  #if the indegree is 0 i appended to queue
  #at last i compared len of toposort with number of nodes
  
  
  
  
  
  
  
  
  
