"""
57. Insert Interval
medium

You are given an array of non-overlapping intervals intervals
where intervals[i] = [starti, endi]
represent the start and the end
of the ith interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end]
that represents the start and end of another interval.

Insert newInterval into intervals
such that intervals is still sorted in ascending order
by starti and intervals still does not have any overlapping intervals
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
        _1, _2 = newInterval
        output = []
        for frm, to in intervals:
            if frm in range(_1, _2 + 1) or to in range(_1, _2 + 1) or _1 in range(frm, to + 1) or _2 in range(frm,
                                                                                                              to + 1):
                _1, _2 = min(_1, frm), max(_2, to)
            else:
                output.append([frm, to])
        output.append([_1, _2])
        return sorted(output)


class TestSearchInsert:

    def test_solo(self):
        assert Solution().insert(intervals=[[1, 5]], newInterval=[2, 3]
                                 ) == [[1, 5]]
    def test_1(self):
        assert Solution().insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]) == [[1, 5], [6, 9]]

    def test_2(self):
        assert Solution().insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]
                                 ) == [[1, 2], [3, 10], [12, 16]]
