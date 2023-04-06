#!/usr/bin/python3

def isWinner(x, nums):
    # Define a function to check if a number is prime
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Define a function to simulate a single turn of the game
    def play_game(n):
        # Create a set of consecutive integers from 1 to n
        nums = set(range(1, n + 1))
        # Define the starting player
        player = 'Maria'
        # Continue playing until there are no more primes in the set
        while True:
            # Find the next prime number in the set
            next_prime = min(filter(is_prime, nums))
            # Remove the prime number and its multiples from the set
            nums.difference_update(range(next_prime, n + 1, next_prime))
            # If the set is now empty, the current player has lost
            if not nums:
                return player
            # Switch to the other player
            player = 'Ben' if player == 'Maria' else 'Maria'

    # Simulate each round of the game and keep track of the winner
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = play_game(n)
        if winner == 'Maria':
            maria_wins += 1
        elif winner == 'Ben':
            ben_wins += 1

    # Determine the overall winner and return their name
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
