"""
57. Insert Interval
medium

You are given an array of non-overlapping intervals intervals
where intervals[i] = [start_i, end_i]
represent the start and the end
of the ith interval and intervals is sorted in ascending order by start_i.
You are also given an interval newInterval = [start, end]
that represents the start and end of another interval.

Insert newInterval into intervals
such that intervals is still sorted in ascending order
by start_i and intervals still does not have any overlapping intervals
(merge overlapping intervals if necessary).

Return intervals after the insertion.
"""


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res, new = [], newInterval

        for index, now in enumerate(intervals):
            if now[1] < new[0]:
                res.append(now)
            elif now[0] > new[1]:
                return res + [new] + intervals[index:]
            else:
                new[0] = min(new[0], now[0])
                new[1] = max(new[1], now[1])

        return res + [new]


class TestSearchInsert:

    def test_solo(self):
        assert Solution().insert(intervals=[[1, 5]], newInterval=[2, 3]
                                 ) == [[1, 5]]

    def test_1(self):
        assert Solution().insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]) == [[1, 5], [6, 9]]

    def test_2(self):
        assert Solution().insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]
                                 ) == [[1, 2], [3, 10], [12, 16]]
