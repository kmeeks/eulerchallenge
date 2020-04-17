import unittest
import solutions.prob_5 as prob

class Prob5(unittest.TestCase):
    def test_prob_5(self):
        answer = prob.solve()
        self.assertEqual(answer, 232792560)

if __name__ == '__main__':
    unittest.main()