from src.package_name.spiral import Solution


class TestSearchInsert:
    def test_1(self):
        assert Solution().spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    def test_sole_folders(self):
        assert Solution().spiralOrder([[7], [9], [6]]) == [7, 9, 6]

    def test_2(self):
        assert Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
                                      ) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]


