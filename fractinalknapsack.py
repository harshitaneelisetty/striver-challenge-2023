#https://www.codingninjas.com/codestudio/problems/fractional-knapsack_8230767?challengeSlug=striver-sde-challenge

def maximumValue(items, n, W):
    items.sort(key = lambda x : x[1] / x[0], reverse = True)
    res = 0
    for i in items:
        if i[0] <= W:
            W -= i[0]
            res += i[1]
        else:
            res += (i[1] / i[0]) * W
            break
    return res
  
  #I sorted the tems based on their value to weight ratio in descending order and iterated through each item
  # I added the entire item's value if its weight is less than or equal to the remaining capacity
  # else i added a fraction of the item's value based on the remaining capacity
