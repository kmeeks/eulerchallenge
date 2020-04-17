import unittest
import solutions.prob_2 as prob

class Prob2(unittest.TestCase):
    def test_prob_2(self):
        answer = prob.solve()
        self.assertEqual(answer, 4613732)

if __name__ == '__main__':
    unittest.main()