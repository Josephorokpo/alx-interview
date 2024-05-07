#!/usr/bin/python3

def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The fewest number of operations needed.

    """
    if n <= 1:
        return 0
    
    # Initialize a list to store the minimum operations for each number of H characters
    dp = [0] * (n + 1)
    
    for i in range(2, n + 1):
        dp[i] = i  # Default to pasting i times
        
        # Iterate over all factors of i
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                # If j is a factor of i, we can achieve i by copying j times and pasting (i // j - 1) times
                dp[i] = min(dp[i], dp[j] + (i // j))
                
    return dp[n]
