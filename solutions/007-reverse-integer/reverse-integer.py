# -*- coding:utf-8 -*-


# Given a 32-bit signed integer, reverse digits of an integer.
#
# Note:
# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
#
#  
# Example 1:
# Input: x = 123
# Output: 321
# Example 2:
# Input: x = -123
# Output: -321
# Example 3:
# Input: x = 120
# Output: 21
# Example 4:
# Input: x = 0
# Output: 0
#
#  
# Constraints:
#
#
# 	-231 <= x <= 231 - 1
#
#


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str1 = str(x)
        if str1[0] == '-':
            str1= str1[0] + str1[:0:-1]
        else:
            str1= str1[::-1]
        res = int(str1)
        if res < -2**31 or res > 2**31-1:
            return 0
        else:
            return res
        
        
