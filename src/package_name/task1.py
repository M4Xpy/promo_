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
