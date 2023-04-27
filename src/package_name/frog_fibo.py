class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n == 0 \
            else n if n in (1, 2) \
            else Solution.climbStairs(self, n - 1) + Solution.climbStairs(self, n - 2)


class TestSearchInsert:

    def test_solo(self):
        assert Solution().climbStairs(2
                                      ) == 2
#
#     def test_solo(self):
#         assert Solution().xxxxx(  xxxx
#                                  ) == xxx