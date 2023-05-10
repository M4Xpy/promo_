"""


"""


class Solution(object):
    def setZeroes(self, matrix: list[list[int]]):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        >>> Solution().setZeroes(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        """
        rows, items = set(), set()

        for row_id in range(len(matrix)):
            for item_id in range(len(matrix[0])):
                if not matrix[row_id][item_id]:
                    rows.add(row_id)
                    items.add(item_id)
        for row in rows:
            matrix[row] = [0] * len(matrix[0])

        for item in items:
            for in_dex in range(len(matrix)):
                matrix[in_dex][item] = 0

        return matrix


print(Solution().setZeroes(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]))