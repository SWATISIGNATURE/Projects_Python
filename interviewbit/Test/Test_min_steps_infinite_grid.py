import unittest
from interviewbit.Array_interviewbit.Min_steps_infinite_grid import Solution

class Test_Min_Steps(unittest.TestCase):
    def test_min_steps_grid(self):
        #case:1
        A1= [-7,-13]
        B1= [1,5]
        C1 = 6

        #case:2
        A2 = [1, 0, 2]
        B2 = [1, 3, 5]
        C2 = 4

        obj = Solution()

        self.assertEqual(obj.coverPoints(A1,B1),C1)
        self.assertEqual(obj.coverPoints(A2,B2),C2)


if '__name__' == '__main__':
    unittest.main()