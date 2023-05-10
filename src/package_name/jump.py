class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        jump = nums.pop(0)
        for index in range(len(nums)):
            if not jump:
                return False
            jump = max(~-jump, nums[index])

        return True
