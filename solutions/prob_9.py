'''Project Euler - Problem 9
   Special Pythagorean Triplet

   A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a**2 + b**2 = c**2
    For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.

    Solve using the relationships defined in Euclids formula
'''
import math

sum_of_triple = 1000


def solve():
    a, b, c = 0, 0, 0
    # While some what arbitrary it seems inefficient to just start at 2
    # It seems reasonable that if we divide the sum by 3 and take the sqrt
    # this would be a good starting point for m... 
    # m = math.floor(math.sqrt(sum_of_triple / 3))
    # For now leave as m = 2
    m = 2
    while c < sum_of_triple:
        for n in range(1, m):
            a = (m * m) - (n * n)
            b = 2 * m * n
            c = (m * m) + (n * n)
            if a + b + c == sum_of_triple:
                return a * b * c
        
        m += 1

    return 'No solution found'