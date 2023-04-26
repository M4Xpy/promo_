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
        matrix = [[0 for _ in range(number)] for _ in range(number)]
        value = 1
        k = row = item = 0

        while value <= number ** 2:
            matrix[row][item] = value
            value += 1
            if k % 4 == 0:
                if item < number - k // 4 - 1:
                    item += 1
                else:
                    row += 1
                    k += 1
            elif k % 4 == 1:
                if row < number - 1 - k // 4:
                    row += 1
                else:
                    item -= 1
                    k += 1
            elif k % 4 == 2:
                if item > k // 4:
                    item -= 1
                else:
                    row -= 1
                    k += 1
            elif k % 4 == 3:
                if row > k // 4 + 1:
                    row -= 1
                else:
                    item += 1
                    k += 1
        return matrix




print(Solution().generateMatrix(3))
