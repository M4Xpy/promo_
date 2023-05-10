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
        meet, result = True, []
        left, right = newInterval

        for LEFT, RIGHT in intervals:
            if RIGHT < left:
                result.append([LEFT, RIGHT])
            elif LEFT > right:
                if meet:
                    meet = False
                    result.append([left, right])
                result.append([LEFT, RIGHT])
            else:
                left, right = min(LEFT, left), max(RIGHT, right)
        if meet:
            result.append([left, right])

        return result
