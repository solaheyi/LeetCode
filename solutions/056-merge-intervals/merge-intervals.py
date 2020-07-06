# -*- coding:utf-8 -*-


# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
#
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#
#
# Example 2:
#
#
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
#


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if intervals == []:
            return []
        intervals.sort(key=lambda x: x[0])
        res = [intervals.pop(0)]
        while intervals:
            if res[-1][1] >= intervals[0][0] and res[-1][0] <= intervals[0][1]:
                res[-1][1] = max(res[-1][1], intervals[0][1])
                res[-1][0] = min(res[-1][0], intervals[0][0])
                intervals.pop(0)
            else:
                res.append(intervals.pop(0))
        return res
        
