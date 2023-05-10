from src.package_name.merge_intervals import Solution


class TestSearchInsert:

    def test_1(self):
        assert Solution().merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]
                                ) == [[1, 6], [8, 10], [15, 18]]

    def test_same_last_1(self):
        assert Solution().merge(intervals=[[1, 4], [4, 5]]
                                ) == [[1, 5]]

    def test_zero_1(self):
        assert Solution().merge(intervals=[[1, 4], [0, 4]]
                                ) == [[0, 4]]

    def test_last_more_then_2(self):
        assert Solution().merge(intervals=[[1, 4], [2, 3]]
                                ) == [[1, 4]]