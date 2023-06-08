   #https://www.codingninjas.com/codestudio/problems/largest-rectangle-in-a-histogram_8230792?challengeSlug=striver-sde-challenge

    def largestRectangle(heights):
        stack = []
        mx = 1
        n = len(heights)
        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                hei = heights[stack[-1]]
                stack.pop()
                if stack == []:
                    width = i
                else:
                    width = i - stack[-1] - 1 
                mx = max(mx, width * hei)
            stack.append(i)
        return mx 
      
      #i iterated over the histogram bars
      #i used stack to keep track of the indices of the bars with non-decreasing heights
      #then i calculated the area of the largest rectangle by considering each bar and its corresponding width
      #and i updated the maximum area whenever a larger rectangle is found
