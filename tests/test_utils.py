import unittest
import utils.utils as utils

class TestUtils(unittest.TestCase):
    def test_find_next_less_palindrome(self):
        palindrome_even = utils.find_next_less_palindrome(1002)
        self.assertEqual(palindrome_even, '1001')
        palindrome_odd = utils.find_next_less_palindrome(10002)
        self.assertEqual(palindrome_odd, '10001')
        palindrome_other = utils.find_next_less_palindrome(12345)
        self.assertEqual(palindrome_other, '12321')
    
    def test_get_prime_factors(self):
        primes_dict = utils.get_prime_factors(20)
        primes_check_dict = {
            2: 2,
            5: 1
        }
        self.assertEqual(primes_dict, primes_check_dict)
    
    def test_iseven(self):
        even = utils.iseven(2)
        self.assertTrue(even)
        odd = utils.iseven(1)
        self.assertFalse(odd)

    def test_ispalindrome(self):
        self.assertTrue(utils.ispalindrome(11111))
        self.assertFalse(utils.ispalindrome(123))
    
    def test_isprime(self):
        self.assertTrue(utils.isprime(29))
        self.assertTrue(utils.isprime(5))
        self.assertFalse(utils.isprime(4))
        self.assertFalse(utils.isprime(40))

    def test_prime_generator(self):
        # Check against first 20 primes
        primes_check = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
                        41, 43, 47, 53, 59, 61, 67, 71]
        count = 0
        for p in utils.prime_generator():
            if p > 71:
                break
            self.assertEqual(p, primes_check[count])
            count += 1

if __name__ == '__main__':
    unittest.main()