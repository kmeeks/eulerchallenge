'''Project Euler - Problem 7
   10,001st prime

   By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

   What is the 10,001st prime number?
'''
from utils.utils import PRIMES_TPL, isprime

def solve():
    prime_cnt = len(PRIMES_TPL)
    nth_prime = 10001
    x = 5

    # Primes can be expressed as 6x +/- 1 when x > 4 (23 already included)
    while prime_cnt < nth_prime:
        check = 6 * x
        check_low = check - 1
        if isprime(check_low):
            prime_cnt += 1

        check_hi = check + 1
        if isprime(check_hi):
            prime_cnt += 1

        x += 1

    if prime_cnt > nth_prime:
        return check_low
    else:
        return check_hi
