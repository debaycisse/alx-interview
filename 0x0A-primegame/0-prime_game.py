#!/usr/bin/python3
"""This module houses the definition of a function, named isWinner"""


def square_root(num):
    """Manually computes the integer square root of a given number

    Args:
        num - the number whose root is manually computed

    Returns:
        the square root of the number
    """
    root = 1
    while root * root <= num:
        root += 1
    return root - 1


def is_prime(num):
    """Checks if a number is prime

    Args:
        num - the number to validate if it is prime or not

    Returns:
        True if number is prime, otherwise false
    """
    if num <= 1:
        return False
    for i in range(2, square_root(num) + 1):
        if num % i == 0:
            return False
    return True


def gen_arr(num):
    """Generates an array of numbers from 1 to num

    Args:
        num - the number from, which an array is gnerated

    Returns:
        the array of the given number is returned
    """
    return [i for i in range(1, num + 1)]


def play_game(num):
    """Simulates a game round and returns
    the winner ('M' for Maria, 'B' for Ben)

    Args:
        num - the number from which prime number and its multiples are
        picked by Ben and Maria. Anyone who couldn't pick any number
        during his or her turn loses

    Returns:
        B if Ben wins or M if Maria is the winner
    """
    if num <= 1:
        return 'B'

    p_array = gen_arr(num)
    maria_play = True

    while True:
        # Find the first prime number left in the array
        prime_found = False
        for i in p_array:
            if is_prime(i):
                prime_found = True
                # Remove all multiples of the prime
                p_array = [x for x in p_array if x % i != 0]
                break

        # If no prime was found, the game ends
        if not prime_found:
            break

        # Switch turns between Maria and Ben
        maria_play = not maria_play

    # If Maria was the last to play, Ben wins, otherwise Maria wins
    return 'B' if maria_play else 'M'


def isWinner(x, nums):
    """Determines the overall winner after x rounds of the game

    Args:
        x - the number of rounds Maria and Ben have to play the game
        nums - the array of number from which each element's
        array is used to pick prime nmber and its multiples

    Returns:
        the winner of the game is returned
    """
    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        result = play_game(nums[i])
        if result == 'M':
            maria_wins += 1
        elif result == 'B':
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Winner: Maria'
    elif ben_wins > maria_wins:
        return 'Winner: Ben'
    return None
