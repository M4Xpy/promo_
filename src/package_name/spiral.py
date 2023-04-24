class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            if matrix:
                res.extend(matrix[index].pop() for index in range(len(matrix)) if len(matrix[index]))
            if matrix:
                res.extend(reversed(matrix.pop(-1)))
            if matrix:
                res.extend(matrix[index].pop(0) for index in range(~-len(matrix), -1, -1) if len(matrix[index]))
        return res


class TestSearchInsert:

    def test_1(self):
        assert Solution().spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    def test_sole_folders(self):
        assert Solution().spiralOrder([[7], [9], [6]]) == [7, 9, 6]

    def test_2(self):
        assert Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
                                      ) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

