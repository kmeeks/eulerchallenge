'''utils.py
   This file contains utility functions used to help
   with solving problems
'''
import math

def iseven(val):
   '''iseven
   Description: checks if a number is even
   Parameter:
      - val: any number
   ''' 
   return val % 2 == 0

def find_next_less_palindrome(number):
   '''find_next_less_palindrome

   Description: Constructs a palindrome by taking the first half of the
   number, duplicating, reversing the duplicated number and appending it 
   back to the first half. The will find the next palindrome less than
   the number provided.

   Parameter:
      - number: an integer
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

def ispalindrome(number):
   '''ispalindrome
   
   Description: Checks if a number is a palindrome
   '''
   numb_str = str(number)
   rev_str = numb_str[::-1]
   return numb_str == rev_str