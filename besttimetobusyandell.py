#https://www.codingninjas.com/codestudio/problems/best-time-to-buy-and-sell-stock_8230746?challengeSlug=striver-sde-challenge

def maximumProfit(prices):
    profit = 0
    mnPrice = float('inf')
    for i in range(len(prices)):
        mnPrice = min(prices[i], mnPrice)
        profit = max(profit, prices[i] - mnPrice)
    return profit
  
#I used the "Maximum Subarray Sum" algorithm to find the maximum profit by buying and selling a stock, given an array of stock prices.
