   #https://www.codingninjas.com/codestudio/problems/ways-to-make-coin-change_8230691?challengeSlug=striver-sde-challenge

   def countWaysToMakeChange(coins, amount) :
        dp = [[-1 for i in range(amount + 1)] for j in range(len(coins))]
        def helper(idx, amount, coins, dp):
            if idx == 0:
                return 1 if amount % coins[0] == 0 else 0
            if dp[idx][amount] != -1:
                return dp[idx][amount]
            notTake = helper(idx - 1, amount, coins, dp)
            take = 0
            if coins[idx] <= amount:
                take = helper(idx, amount - coins[idx], coins, dp)
            dp[idx][amount] = take + notTake
            return dp[idx][amount]
        return helper(len(coins) - 1, amount, coins, dp)
