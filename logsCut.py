#https://www.codingninjas.com/codestudio/problems/cut-logs_8230782?challengeSlug=striver-sde-challenge

def cutLogs(num_axes, capacity):
    dp = [i for i in range(capacity + 1)]
    for axis in range(2, num_axes + 1):
        dp_new = [0 for _ in range(capacity + 1)]
        t = 1
        for i in range(1, capacity + 1):
            while t < i and max(dp[t - 1], dp_new[i - t]) > max(dp[t], dp_new[i - t - 1]):
                t += 1
            dp_new[i] = 1 + max(dp[t - 1], dp_new[i - t])
        dp = dp_new
    return dp[capacity]

  #i used 2 arrays dp and dp_new, to store the maximum number of cuts for each capacity at different stages 
  #i iterated through axes and updated the dp array based on the optimal psoition for cutting
  #i calculated and returned the max number of cuts possible for given log capacity
  
