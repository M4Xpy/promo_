from src.package_name.set_zero import Solution


class TestSearchInsert:
    def test_1(self):
        assert Solution().setZeroes(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]
                                    ) == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    def test_2(self):
        assert Solution().setZeroes(matrix=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
                                    ) == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
