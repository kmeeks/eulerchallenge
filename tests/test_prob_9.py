import unittest
import solutions.prob_9 as prob

class Prob9(unittest.TestCase):
    def test_prob_9(self):
        answer = prob.solve()
        self.assertEqual(answer, 31875000)

if __name__ == '__main__':
    unittest.main()