# -*- coding:utf-8 -*-


# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
#
# Example:
#
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
#


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Double pointer, calculate the amount of rain accumulated on each bar, the value = min (the maxmum height of all bars on the left (including itsself), the maximum height of all bars on the right (including itsself)) - own height
        # 双指针，计算每个坐标的柱子上的积雨量，值 = min(左边所有柱子(包括自己)最大值， 右边所有柱子(包括自己)最大值) - 自己的高度
        res = 0
        if height == []:
            return res
        left = 0
        right = len(height) - 1
        left_max = height[0]
        right_max = height[-1]
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1
        return res
