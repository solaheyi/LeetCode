# -*- coding:utf-8 -*-


# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# Example:
#
#
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Note:
#
# You can assume that you can always reach the last index.
#


class Solution(object):
    def jump(self, nums):
        start = 0
        count = 0
        if len(nums) == 1:
            return 0
        while start < len(nums):
            next = 0
            max_dis = 0
            for i in range(1, nums[start]+1):
                if start + i == len(nums) - 1:
                    count += 1
                    return count
                if i + nums[start + i] > max_dis:
                    next = start + i
                    max_dis = i + nums[start + i]
            start = next
            count += 1
