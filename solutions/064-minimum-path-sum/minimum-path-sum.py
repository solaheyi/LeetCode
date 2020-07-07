# -*- coding:utf-8 -*-


# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
#
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
#
#


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # DP
        rows, cols = len(grid), len(grid[0])
        sum = rows + cols
        leftdown = [[0, 1], [1, 0]]
        while sum >= 2:
            for row in range(rows):
                col = sum - row - 2
                if 0 <= col < cols:
                    if 0 <= 0+row < rows and 0 <= 1+col < cols and 0 <= 1+row < rows and 0 <= 0+col < cols:
                        grid[row][col] += min(grid[row][col+1], grid[row+1][col])
                    elif 0 <= 0+row < rows and 0 <= 1+col < cols:
                        grid[row][col] += grid[row][col+1]
                    elif 0 <= 1+row < rows and 0 <= 0+col < cols:
                        grid[row][col] += grid[row+1][col]
            sum -= 1
        return grid[0][0]
