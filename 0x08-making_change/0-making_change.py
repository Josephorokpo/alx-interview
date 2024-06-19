#!/usr/bin/python3
"""
Determine the fewest number of coins needed to meet a given amount total
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    
    Args:
        coins (list of int): The values of the coins in your possession.
        total (int): The total amount to be met.
    
    Returns:
        int: Fewest number of coins needed to meet total. If total cannot be met, return -1.
    """
    if total <= 0:
        return 0
    
    # Initialize the dp array with a large value (total + 1 is larger than any possible number of coins)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1
