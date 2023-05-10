from src.package_name.my_atoi import Solution


class TestSearchInsert:

    def test_1(self):
        assert Solution().myAtoi("words and 987"
                                 ) == 0

    def test_2(self):
        assert Solution().myAtoi("   -42"
                                 ) == -42
    #
    def test_3(self):
        assert Solution().myAtoi("-+12"
                                 ) == 12

    def test_4(self):
        assert Solution().myAtoi("42"
                                 ) == 42
