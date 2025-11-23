class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(amount + 1):
                if i - coin >= 0:
                    dp[i] += dp[i - coin]
        return dp[-1]

        # 2D
        # dp = [[0] * (amount + 1) for _ in range(len(coins))]
        # dp[0][0] = 1

        # for i in range(amount + 1):
        #     if i % coins[0] == 0:
        #         dp[0][i] = 1

        # for i in range(1, len(coins)):
        #     dp[i][0] = 1
        #     for j in range(amount + 1):
        #         dp[i][j] = dp[i - 1][j]
        #         if j - coins[i] >= 0:
        #             dp[i][j] += dp[i][j - coins[i]]

        # return dp[-1][-1]
