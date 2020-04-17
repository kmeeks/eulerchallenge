'''Project Euler - Problem 3
   Largest prime factor

   The prime factors of 13195 are 5, 7, 13 and 29.

   What is the largest prime factor of the number 600851475143 ?
'''
import math


def solve():
    n = 600851475143
    last_factor = 1

    # If n were even we could address it by dividing by 2
    while n % 2 == 0:
        max_prime = 2
        n /= 2

    factor = 3
    # We can also set the max factor to the square root of n to reduce the number
    # of factors we need to check.
    max_factor = math.sqrt(n)
    while n > 1 and factor <= max_factor:
        # If n is divisible by a factor we need to update the last_factor to be 
        # equal to the current factor.
        while n % factor == 0:
            n /= factor
            last_factor = factor
            max_factor = math.sqrt(n)
    
        # Increase the factor by 2 since evens would be divisible by 2
        factor += 2
    
    # If factor was equal to n use last_factor
    if n == 1:
        return last_factor
    else:  # if factor equals/exceeded max_factor
        return n

