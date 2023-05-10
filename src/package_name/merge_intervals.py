"""
Given an array of intervals where
intervals[i] = [start_i, end_i],
merge all overlapping intervals,
and return an array
of the non-overlapping intervals
that cover all the intervals in the input.
Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap,
 merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda pair: pair[0])
        out = [intervals.pop(0)]
        for pair in intervals:
            if pair[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], pair[1])
            else:
                out += [pair]
        return out

    # print(Solution().merge(


#     [[1, 4], [2, 3]]
# ))
class TestSearchInsert:

    def test_1(self):
        assert Solution().merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]
                                ) == [[1, 6], [8, 10], [15, 18]]

    def test_same_last_1(self):
        assert Solution().merge(intervals=[[1, 4], [4, 5]]
                                ) == [[1, 5]]

    def test_zero_1(self):
        assert Solution().merge(intervals=[[1, 4], [0, 4]]
                                ) == [[0, 4]]

    def test_last_more_then_2(self):
        assert Solution().merge(intervals=[[1, 4], [2, 3]]
                                ) == [[1, 4]]
