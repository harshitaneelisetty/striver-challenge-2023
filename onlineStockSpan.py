#https://www.codingninjas.com/codestudio/problems/online-stock-span_8230843?challengeSlug=striver-sde-challenge

def findSpans(price):
    n = len(price)
    result = [0] * n
    stk = []

    for i in range(n):
        while stk and price[stk[-1]] <= price[i]:
            stk.pop()

        if not stk:
            result[i] = i + 1
        else:
            result[i] = i - stk[-1]

        stk.append(i)

    return result
  
  #i simply found the span of each element, the number of consecutive previous elements
  #with a higher or equal price
  #i used a stack to keep track of the indices of the elements in descending order of prices
  

  
