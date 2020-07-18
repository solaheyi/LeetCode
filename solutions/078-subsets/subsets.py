# -*- coding:utf-8 -*-


# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0, tmp = []):
            if len(tmp) == k:
                res.append(tmp[:])
            for i in range(first, n):
                tmp.append(nums[i])
                backtrack(i + 1, tmp)
                tmp.pop()
        res = []
        n = len(nums)
        for k in range(n+1):
            backtrack()
        return res
