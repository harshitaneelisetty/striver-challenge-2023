#https://www.codingninjas.com/codestudio/problems/maximum-of-minimum-for-every-window-size_8230783?challengeSlug=striver-sde-challenge&leftPanelTab=0

def maxMinWindow(arr, n):
    s = [] 
    left = [-1] * (n + 1)
    right = [n] * (n + 1)
    for i in range(n):
        while (len(s) != 0 and arr[s[-1]] >= arr[i]):
            s.pop()
        if (len(s) != 0):
            left[i] = s[-1]
        s.append(i)
    while (len(s) != 0):
        s.pop()
    for i in range(n - 1, -1, -1):
        while (len(s) != 0 and arr[s[-1]] >= arr[i]):
            s.pop()
        if(len(s) != 0):
            right[i] = s[-1]
        s.append(i)
    ans = [float('-inf')] * (n + 1)
    for i in range(n):
        Len = right[i] - left[i] - 1
        ans[Len] = max(ans[Len], arr[i])
    for i in range(n - 1, 0, -1):
        ans[i] = max(ans[i], ans[i + 1])
    return ans[1:]
  
  #Firstly i found the maximum value in each window of elements
  #such that the minimum element in that window is greater than all the elements preceding it and greater than all the elements following it
  #i followed stack approach to find next min element
  #and i also found next max element
  #after that i found the difference between max and min element and i considered max and retuned array
  
  
  
