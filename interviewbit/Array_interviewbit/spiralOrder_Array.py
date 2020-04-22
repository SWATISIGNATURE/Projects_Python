class Solution:

    def spiralOrder(self, A):
        R = len(A)
        C = len(A[0])
        # print(R,C)
        L = 0
        T = 0
        B = R - 1
        R = C - 1
        Dir = 0
        res = []
        while (T <= B and L <= R):
            if Dir == 0:
                for i in range(L, R + 1):
                    # print(A[T][i])
                    res.append(A[T][i])
                T += 1
                # Dir should go to 1

            elif Dir == 1:
                for i in range(T, B + 1):
                    res.append(A[i][R])
                    # print(A[i][R])
                R -= 1
                # Dir = 2

            elif Dir == 2:
                for i in range(R, L - 1, -1):
                    # print(A[B][i])
                    res.append(A[B][i])
                B -= 1
                # Dir = 3
            elif Dir == 3:
                for i in range(B, T - 1, -1):
                    # print(A[i][L])
                    res.append(A[i][L])
                L += 1
                # Dir = 4

            Dir = (Dir + 1) % 4
        return res

#input

# A = [
#     [ 1, 2, 3 ],
#     [ 4, 5, 6 ],
#     [ 7, 8, 9 ]
# ]

# To call the function to get the output using Solution class directly
# sol = Solution()
# print(sol.spiralOrder(A))

