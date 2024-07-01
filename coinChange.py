def coinChange(coins, amount):
    coins.sort()
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin > i:
                break
            dp[i] = min(dp[i], dp[i - coin] + 1)

coins, amount = [1, 2, 5], 11
print(coinChange(coins, amount))