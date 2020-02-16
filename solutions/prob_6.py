'''Project Euler - Problem 6
   Sum Square Difference

   The sum of the squares of the first ten natural numbers is,

   1**2+2**2+...+10**2=385

   The square of the sum of the first ten natural numbers is,

   (1+2+...+10)**2 = 55**2 = 3025

   Hence the difference between the sum of the squares of the 
   first ten natural numbers and the square of the sum is 
   3025 − 385 = 2640.

   Find the difference between the sum of the squares of the first 
   one hundred natural numbers and the square of the sum.

   * The sum can be calculated as a function of n(n + 1)/2 where n in this case is 100
   * Based on Falhabers formula sum of a sequence of squares can also be calculated by
   n * (n + 1) * (2 * n + 1) / 6
   * Falhabers formula can be used to calculate sum of a sequence to an exponent beyond
     what is seen here
'''


def solve():
   n = 100

   # Calculate the sum of the first 100 natural numbers
   n_sum = n * (n + 1) / 2

   # Calculate the sum of squares of the first 100 natural numbers
   n_sumsq = n * (n + 1) * (2 * n + 1) / 6

   return  n_sum * n_sum - n_sumsq