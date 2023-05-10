"""
59. Spiral Matrix II

Given a positive integer n, generate an n x n matrix
filled with elements from 1 to n2 in spiral order.
"""


class Solution(object):
    def generateMatrix(self, number):
        """
        :type number: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * number for _ in range(number)]
        m = number >> 1
        for i in range(m):
            b = ~-number - 2 * i
            for j in range(b):
                number_i = number - i
                xxx = number_i * i // 4 + -~j
                matrix[i][i + j] = xxx
                matrix[i + j][~-number_i] = xxx + b
                matrix[~-number_i][~-number_i - j] = xxx + 2 * b
                matrix[~-number_i - j][i] = xxx + 3 * b
        if number - 2 * m:
            matrix[m][m] = number ** 2
        return matrix


print(Solution().generateMatrix(3))
