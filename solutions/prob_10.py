'''Project Euler - Problem 10
   Summation of primes

   The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

   Find the sum of all the primes below two million.
'''
from utils.utils import PRIMES_TPL, isprime
import math

# Solve using the sieve of Eratosthenes and eliminating even numbers
# Every element of the arry (i) represents an odd number equal to 2i + 1
# Start by assuming all elements in the arry are prime. Mark multiples
# of prime as not prime up to the sieve bound 
def solve():
    limit = 2000000
    primes_sum = 2 # Start sum at 2 because 2 is prime but eliminated from evaluation
    sieve_bound = math.floor((limit - 1) / 2) + 1
    sieve_array = [False] * sieve_bound
    cross_limit = math.floor(math.sqrt(limit - 1) / 2)

    # 1 is not prime
    sieve_array[0] = True

    for i in range(1, cross_limit):
        # if false 2i + 1 is prime, if true it is not and move on to 
        # the next val
        if not sieve_array[i]:
            index = 2 * i * (i + 1)
            for j in range(index, sieve_bound, (2 * i) + 1):
                sieve_array[j] = True
    
    # Calculate the sum using the sieve_array
    for p in range(1, sieve_bound):
        if not sieve_array[p]:
            primes_sum += 2 * p + 1
    
    return primes_sum