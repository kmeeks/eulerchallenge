import unittest
import solutions.prob_6 as prob

class Prob6(unittest.TestCase):
    def test_prob_6(self):
        answer = prob.solve()
        self.assertEqual(answer, 25164150)

if __name__ == '__main__':
    unittest.main()