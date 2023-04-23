class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: -> int
        """
        res = nums.pop(0)
        if len(nums):
            maxi = {res}
            for num in nums:
                res = max(num, res + num)
                maxi.add(res)
            return sorted(maxi)[-1]
        return res


class TestSearchInsert:

    def test_1(self):
        assert Solution().maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    def test_sole_positiv(self):
        assert Solution().maxSubArray(nums=[1]) == 1

    def test_sole_negative(self):
        assert Solution().maxSubArray(nums=[-1]) == -1

    def test_2(self):
        assert Solution().maxSubArray(nums=[5, 4, -1, 7, 8]) == 23
