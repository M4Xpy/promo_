from src.package_name.jump import Solution


class TestSearchInsert:

    def test_1(self):
        assert Solution().canJump([2, 3, 1, 1, 4]) is True

    def test_sole_zero(self):
        assert Solution().canJump([0]) is True
