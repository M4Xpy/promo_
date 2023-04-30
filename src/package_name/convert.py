"""

"""


class Solution(object):
    def convert(self, string, numRows):
        """
        :type string: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2 or numRows > len(string):
            return string

        # Create a string list for each ZigZag string
        res = [''] * numRows
        # Iterator to change direction
        index, direction = 0, 1
        numRows -= 1

        for char in string:
            res[index] += char
            # If you reach the edge down or up, change direction
            if index == 0:
                direction = 1
            elif index == numRows:
                direction = -1
            index += direction

        return ''.join(res)


class TestSearchInsert:

    def test_1(self):
        assert Solution().convert(string="PAYPALISHIRING", numRows=3
                                  ) == "PAHNAPLSIIGYIR"
    #
    # def test_2(self):
    #     assert Solution().convert(xxxx
    #                               ) == xxx
    #
    # def test_3(self):
    #     assert Solution().convert(xxxx
    #                               ) == xxx
    #
    # def test_4(self):
    #     assert Solution().convert(xxxx
    #                               ) == xxx
    #
    # def test_5(self):
    #     assert Solution().convert(xxxx
    #                               ) == xxx
    #
    # def test_7(self):
    #     assert Solution().convert(xxxx
    #                               ) == xxx
    #
    # def test_8(self):
    #     assert Solution().convert(xxxx
    #                               ) == xxx
    #
    # def test_9(self):
    #     assert Solution().convert(xxxx
    #                               ) == xxx
    #
    # def test_0(self):
    #     assert Solution().convert(xxxx
    #                               ) == xxx
