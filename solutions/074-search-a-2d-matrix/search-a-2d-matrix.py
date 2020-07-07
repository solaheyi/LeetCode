# -*- coding:utf-8 -*-


# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
#
# 	Integers in each row are sorted from left to right.
# 	The first integer of each row is greater than the last integer of the previous row.
#
#
# Example 1:
#
#
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
#
#
# Example 2:
#
#
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false
#


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # binary search
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        # search 0~m*n, row = idx // n, col = idx % n
        left, right = 0, m*n-1
        while left <= right:
            idx = (right+left) // 2
            if matrix[idx//n][idx%n] == target:
                return True
            elif matrix[idx//n][idx%n] > target:
                right = idx -1
            else:
                left = idx + 1
        return False
        
