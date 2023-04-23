class Solution(object):
    def maxSubArray(self, nums):
        curr_sum = 0
        max_sum = -1e8
        for num in nums:
            curr_sum += num
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return max_sum

class TestSearchInsert:

    def test_1(self):
        assert Solution().maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    def test_sole_positiv(self):
        assert Solution().maxSubArray(nums=[1]) == 1

    def test_sole_negative(self):
        assert Solution().maxSubArray(nums=[-1]) == -1

    def test_2(self):
        assert Solution().maxSubArray(nums=[5, 4, -1, 7, 8]) == 23
