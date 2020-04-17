'''Project Euler - Problem 10
   Summation of primes

   The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

   Find the sum of all the primes below two million.
'''
from utils.utils import prime_generator

# TODO: This takes about 45s to run, should be refactored to a more intelligent solution
def solve():
    limit = 2000000
    sum = 0

    for p in prime_generator():
        if p >= limit:
            return sum
        sum += p