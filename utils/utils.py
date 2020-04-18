'''utils.py
   This file contains utility functions used to help
   with solving problems
'''
import math

PRIMES_TPL = (2, 3, 5, 7, 11, 13, 17, 19, 23)


def find_next_less_palindrome(number):
   '''find_next_less_palindrome

   Description: Constructs a palindrome by taking the first half of the
   number, duplicating, reversing the duplicated number and appending it 
   back to the first half. The will find the next palindrome less than
   the number provided.
   Parameter:
      number - an integer
   Returns:
      palindrome - a string
   '''
   # Make the number a string for the purposes of manipulation
   numb_str = str(number)
   check_len = len(numb_str)
   if iseven(check_len):  # If even, can create palindrome from first half
      split_len = int(check_len / 2)
      fh = numb_str[:split_len]
      palindrome = numb_str[:split_len] + numb_str[split_len - 1::-1]
   else:
      # If odd, divide by 2 and round up
      split_len = math.ceil(check_len / 2)
      palindrome = numb_str[:split_len] + numb_str[split_len - 2::-1]

   return palindrome


def get_prime_factors(val):
   '''get_prime_factors

   Description: returns a dictionary of prime factors for a value.
   This function
   Parameter:
      val - a number
   Returns:
      dict - { factor: factor_count }
   '''
   prime_factors = dict()

   if val in PRIMES_TPL:
      prime_factors.setdefault(val, 1)
   else:
      limit = math.sqrt(val)
      pi = 0
      calc_val = val
      while calc_val not in PRIMES_TPL and calc_val != 1:
         # If calc val is divisible by a prime add it to the factors
         # list and divid by the factor while setting calc_val to
         # the result
         if calc_val % PRIMES_TPL[pi] == 0:
            calc_val /= PRIMES_TPL[pi]
            factor_count = prime_factors.get(PRIMES_TPL[pi], 0) + 1
            prime_factors[PRIMES_TPL[pi]] = factor_count
         else:
            pi += 1
      
      # Add calc_val to the factors list once it becomes prime
      if calc_val != 1:
         # Convert to int to avoid issues
         calc_val = int(calc_val)
         factor_count = prime_factors.get(calc_val, 0) + 1
         prime_factors[calc_val] = factor_count

   return prime_factors


def iseven(val):
   '''iseven

   Description: checks if a number is even
   Parameter:
      val - any number
   ''' 
   return val % 2 == 0


def ispalindrome(number):
   '''ispalindrome
   
   Description: Checks if a number is a palindrome
   Parameter:
      number - an integer
   Returns:
      boolean
   '''
   numb_str = str(number)
   rev_str = numb_str[::-1]
   return numb_str == rev_str


def isprime(num):
   '''isprime

   Description: determines if a given number is prime
   '''
   # Check if number is in Primes Tuple first
   if num in PRIMES_TPL:
      return True

   # 23 is the last prime in the Primes Tuple so any other number less than
   # 23 would not be Prime. Also check if divisible by 2 or 3
   if num <= 23 or num % 2 == 0 or num % 3 == 0:
      return False

   # If there's no number less than the sqrt(num) that can evenly divide num,
   # then it is prime
   x = 5
   while x <= math.sqrt(num):
      if num % x == 0 or num % (x + 2) == 0:
         return False
      # Increment by 6 since primes can be expressed as 6x +/- 1 when x > 4
      x += 6
   
   return True

   
def prime_generator():
   # Start by yielding the primes in PRIME_TUPLE
   for p in PRIMES_TPL:
      yield p
   
   # Primes can be expressed as 6x +/- 1 when x > 4 (23 already included)
   x = 5
   while True:
      check = 6 * x
      check_low = check - 1
      if isprime(check_low):
         yield check_low

      check_hi = check + 1
      if isprime(check_hi):
         yield check_hi

      x += 1