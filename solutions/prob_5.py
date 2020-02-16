'''Project Euler - Problem 5
   Smallest Multiple

   2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

   What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
import math
from utils.utils import get_prime_factors

def set_max_factors(max_prime_factors, prime_factors):
    # Get all unique keys between the 2 dicts
    all_keys = max_prime_factors.keys() | prime_factors.keys()
    for k in all_keys:  # Loop through keys for max and prime factor dicts
        # Get the max value of max and prime factors, the set in max primes
        max_factor = max(max_prime_factors.get(k, 0), prime_factors.get(k, 0))
        max_prime_factors[k] = max_factor

def solve():
    max_prime_factors = dict()
    # Since 1 will not impact the result start at i = 2 and evaluate to n = 20
    n = 20
    x = 2
    lcm = 1
    
    for i in range(x, n + 1):
        # get a dict of the prime factors for each value { factor: factor_count }
        prime_factors = get_prime_factors(i)
        # Keep a dict of the max number of prime factors for all values { factor: max_factor_count }
        set_max_factors(max_prime_factors, prime_factors)
    
    # Perform calculation to determine the least common multiple (LCM)
    for k, v in max_prime_factors.items():
        lcm *= math.pow(k, v)

    return lcm
