"""


"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        items = set()
        row_range = range(len(matrix))
        item_range = range(len(matrix[0]))

        for row_id in row_range:
            for item_id in item_range:
                if not matrix[row_id][item_id]:
                    rows.add(row_id)
                    items.add(item_id)
        for row in rows:
            for index in item_range:
                matrix[row][index] = 0
        for item in items:
            for in_dex in row_range:
                matrix[in_dex][item] = 0

        return matrix


# print(Solution().setZeroes(  matrix = [[1,1,1],[1,0,1],[1,1,1]]))


class TestSearchInsert:

    def test_1(self):
        assert Solution().setZeroes(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]
                                    ) == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    def test_2(self):
        assert Solution().setZeroes(matrix=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
                                    ) == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
#
#     def test_solo(self):
#         assert Solution().xxxxx(  xxxx
#                                  ) == xxx
