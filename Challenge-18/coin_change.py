class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Fewest number of coins that you need to make up that amount.
        Args:
            coins:list of coins
            amount
        Returns:
            Number of coins or
            If that amount of money cannot be made up by any combination of the coins, return -1
        """

        dp=[0]
        for val in range (1,amount+1):
            count=float('inf')
            for coin in coins:
               if (val-coin)>=0:
                    count=min(count,dp[val-coin])
            dp.append(count+1) # type: ignore
        
        if dp[amount]==float('inf'):
            return -1
        return dp[amount]    



                
        