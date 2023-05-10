from src.package_name.task1 import Solution


class TestSearchInsert:

    def test_1(self):
        assert Solution().maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    def test_sole_positiv(self):
        assert Solution().maxSubArray(nums=[1]) == 1

    def test_sole_negative(self):
        assert Solution().maxSubArray(nums=[-1]) == -1

    def test_2(self):
        assert Solution().maxSubArray(nums=[5, 4, -1, 7, 8]) == 23
