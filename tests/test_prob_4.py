import unittest
import solutions.prob_4 as prob

class Prob4(unittest.TestCase):
    def test_prob_4(self):
        answer = prob.solve()
        self.assertEqual(answer, 906609)

if __name__ == '__main__':
    unittest.main()