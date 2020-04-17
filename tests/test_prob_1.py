import unittest
import solutions.prob_1 as prob

class Prob1(unittest.TestCase):
    def test_prob_1(self):
        answer = prob.solve()
        self.assertEqual(answer, 233168)

if __name__ == '__main__':
    unittest.main()
