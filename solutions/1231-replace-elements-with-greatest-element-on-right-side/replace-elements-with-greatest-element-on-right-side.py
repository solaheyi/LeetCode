# -*- coding:utf-8 -*-


# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
#
# After doing so, return the array.
#
#  
# Example 1:
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
#
#  
# Constraints:
#
#
# 	1 <= arr.length <= 10^4
# 	1 <= arr[i] <= 10^5
#


class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        max = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            tmp = arr[i]
            arr[i] = max
            if tmp > max:
                max = tmp
        arr[-1] = -1
        return arr
