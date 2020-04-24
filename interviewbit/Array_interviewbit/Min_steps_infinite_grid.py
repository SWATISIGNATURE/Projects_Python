"""
You are in an infinite 2D grid where you can move in any of the 8 directions
You are given a sequence of points and the order in which you need to cover the points.
Give the minimum number of steps in which you can achieve it. You start from the first point.
"""

class Solution:
    def coverPoints(self, A, B):
        steps = 0
        for i in range(len(A) - 1):
            pt1 = (A[i], B[i])
            pt2 = (A[i + 1], B[i + 1])
            distance = self.distanceBtwnPoints(pt1, pt2)
            steps += distance

            # print(pt1, pt2, distance)

        return steps


    def distanceBtwnPoints(self, pt1, pt2):
        return max(abs(pt1[0] - pt2[0]), abs(pt1[1] - pt2[1]))

#A = [-7,-13]
#B = [1,5]
#Solution().coverPoints(A,B)
# result is: 6
