import unittest

from interviewbit.Array_interviewbit.spiralOrder_Array import Solution


class SpiralOrderArray(unittest.TestCase):
    def test_spiral_output(self):
        """
        Test that it gives the correct output.
        """
        #case-1
        A = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        exp = [1, 2, 3, 6, 9, 8, 7, 4,5]

        # case-2
        A1 = [[1]]
        exp1 = [1]

        ##case-3
        A2 = [[1, 3, 4, 2]]
        exp2 = [1,3,4,2]

        ##case-4
        A3 = [[1,3],[4,2]]
        exp3 = [1,3,2,4]

        self.assertEqual(Solution().spiralOrder(A), exp)
        self.assertEqual(Solution().spiralOrder(A1), exp1)
        self.assertEqual(Solution().spiralOrder(A2), exp2)
        self.assertEqual(Solution().spiralOrder(A3), exp3)

if __name__ == '__main__':
    unittest.main()
