from src.package_name.convert import Solution


class TestSearchInsert:

    def test_1(self):
        assert Solution().convert(string="PAYPALISHIRING", numRows=3
                                  ) == "PAHNAPLSIIGYIR"