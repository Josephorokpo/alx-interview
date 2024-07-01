#!/usr/bin/python3
"""
Determine the winner of each game played by Maria and Ben.
"""


def isWinner(x, nums):
    """
    Determine who the winner of each game is.

    Args:
        x (int): The number of rounds.
        nums (list of int): List containing the 'n' for each round.

    Returns:
        str: The name of the player that won the most rounds,
        or None if it's a tie.
    """
    if x < 1 or not nums:
        return None

    # Sieve of Eratosthenes to find all primes up to the maximum number in nums
    max_num = max(nums)
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False

    p = 2
    while (p * p <= max_num):
        if sieve[p]:
            for i in range(p * p, max_num + 1, p):
                sieve[i] = False
        p += 1

    primes = [i for i in range(max_num + 1) if sieve[i]]

    # Function to count primes <= n
    def count_primes(n):
        count = 0
        for prime in primes:
            if prime <= n:
                count += 1
            else:
                break
        return count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = count_primes(n)
        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
