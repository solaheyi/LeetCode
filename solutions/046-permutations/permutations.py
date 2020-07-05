# -*- coding:utf-8 -*-


# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#
#


class Solution(object):
    def permute(self, nums):
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
        return res
