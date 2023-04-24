class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        jump = nums[0]
        for i in range(1, len(nums)):
            if jump == 0:
                return False
            jump = max(~-jump, nums[i])
        return True


class TestSearchInsert:

    def test_1(self):
        assert Solution().canJump([2, 3, 1, 1, 4]) is True
