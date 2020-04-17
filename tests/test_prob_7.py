import unittest
import solutions.prob_7 as prob

class Prob7(unittest.TestCase):
    def test_prob_7(self):
        answer = prob.solve()
        self.assertEqual(answer, 104743)

if __name__ == '__main__':
    unittest.main()