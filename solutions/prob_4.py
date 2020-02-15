'''Project Euler - Problem 4
   Largest palindrome product

   A palindromic number reads the same both ways. The largest palindrome made 
   from the product of two 2-digit numbers is 9009 = 91 × 99.

   Find the largest palindrome made from the product of two 3-digit numbers.
'''
from utils.utils import ispalindrome

def solve():
    # a and b will be the prospective factors of the palindrome
    # a will always be the max factor. a will start at 999 working backwards
    a = 999
    max_palindrome = 0

    # a and b can't be less than 100 since they must be 3 digits
    while a >= 100:
        # set b to a and loop through the b factors less <= a
        b = a

        while b >= 100:
            number = a * b
            # if a * b is less than max_palindrome we can exit this loop since 
            # all numbers after this will be less as well
            if number < max_palindrome:
                break

            if ispalindrome(number):
                max_palindrome = number

            b -= 1
        
        a -= 1

    return max_palindrome
