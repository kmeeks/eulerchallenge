import unittest
import solutions.prob_10 as prob

class Prob10(unittest.TestCase):
    def test_prob_10(self):
        answer = prob.solve()
        self.assertEqual(answer, 142913828922)

if __name__ == '__main__':
    unittest.main()