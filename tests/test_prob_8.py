import unittest
import solutions.prob_8 as prob

class Prob8(unittest.TestCase):
    def test_prob_8(self):
        answer = prob.solve()
        self.assertEqual(answer, 23514624000)

if __name__ == '__main__':
    unittest.main()