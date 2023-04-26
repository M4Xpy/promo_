"""
59. Spiral Matrix II

Given a positive integer n, generate an n x n matrix
filled with elements from 1 to n2 in spiral order.
"""


class Solution:
    # @return a list of lists of integer

    def generateMatrix(self, n):
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        top = left = 0
        right = bottom = ~-n
        num = 1

        while left <= right and top <= bottom:
            for TOP in range(left, -~right):
                matrix[top][TOP] = num
                num += 1
            for RIGHT in range(-~top, bottom):
                matrix[RIGHT][right] = num
                num += 1
            for BOTTOM in range(right, ~-left, -1):
                if top < bottom:
                    matrix[bottom][BOTTOM] = num
                    num += 1
            for LEFT in range(~-bottom, top, -1):
                if left < right:
                    matrix[LEFT][left] = num
                    num += 1
            top = left = -~left
            right = bottom = ~-bottom

        return matrix


print(Solution().generateMatrix(3))
