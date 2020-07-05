# -*- coding:utf-8 -*-


# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# Example:
#
#
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
#
#


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
            else:
                for i in range(len(nums)):
                    backtrack(nums[:i]+nums[i+1:], tmp+[nums[i]])
        backtrack(nums, [])
        res = list(set([tuple(t) for t in res]))
        res = [list(v) for v in res]
        return res
