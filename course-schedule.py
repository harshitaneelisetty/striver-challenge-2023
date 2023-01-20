# https://leetcode.com/problems/course-schedule/submissions/860622764/

class Solution:
    def canFinish(self, V: int, adj1: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for i in adj1:
            adj[i[0]].append(i[1])
        indegree = defaultdict(int)
        for i in range(V):
            for j in adj[i]:
                indegree[j] += 1
        topo = []
        queue = []
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            node = queue[0]
            queue.pop(0)
            topo.append(node)
            for i in adj[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        return len(topo) == V
      
      #Here I used bfs approach to solve the problem
      #found the indegree of all nodes
      #taken nodes whose indegree is 0 and appended to queue then decreased the indegree of adjacent nodes
      
