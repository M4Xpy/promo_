class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        _1, _2 = 0, 1
        for _ in range(-~n):
            _1, _2 = _2, _1 + _2
        return _1 if n else 0


for x in range(11):
    print(Solution().climbStairs(x))
