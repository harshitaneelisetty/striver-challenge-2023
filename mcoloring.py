#https://www.codingninjas.com/codestudio/problems/m-coloring-problem_8230777?challengeSlug=striver-sde-challenge

def isCorrect(graph, vertex, color, col):
    for v in range(len(graph)):
        if graph[vertex][v] == 1 and color[v] == col:
            return False
    return True

def graphColoring(graph, num_colors):
    vertices = len(graph)
    color = [0] * vertices

    def graphCol(cur_vertex):
        if cur_vertex == vertices:
            return True

        for col in range(1, num_colors + 1):
            if isCorrect(graph, cur_vertex, color, col):
                color[cur_vertex] = col
                if graphCol(cur_vertex + 1):
                    return True
                color[cur_vertex] = 0

        return False

    if graphCol(0):
        return "YES"
    return "NO"
  
  #I used backtracking algorithm
  #I assigned  colors to vertices of a graph such that no adjacent vertices have the same color
  #In graphColoring function I initialized an array of colors and recursively assigned colors to vertices, checked for conflicts at each step
  #if coloring is found returned yes else no
  
  
  
