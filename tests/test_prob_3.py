import unittest
import solutions.prob_3 as prob

class Prob3(unittest.TestCase):
    def test_prob_3(self):
        answer = prob.solve()
        self.assertEqual(answer, 6857)

if __name__ == '__main__':
    unittest.main()