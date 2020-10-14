# -*- coding:utf-8 -*-


# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        graph = [[0 for i in range(cols)] for j in range(rows)]
        row, col = 0, 0
        graph[row][col] = 1
        res = [matrix[row][col]]
        mo = 0
        while len(res) < rows * cols:
            graph[row][col] = 1
            row_n, col_n = self.move(mo, row, col)
            if self.checkEdge(row_n, col_n, rows, cols) and not graph[row_n][col_n]:
                row, col = row_n, col_n
                res.append(matrix[row][col])
            else:
                mo = (mo + 1) % 4
        return res

    def move(self, mo, row, col):
        if mo == 0:
            col += 1
            return row, col
        if mo == 1:
            row += 1
            return row, col
        if mo == 2:
            col -= 1
            return row, col
        if mo == 3:
            row -= 1
            return row, col

    def checkEdge(self, row, col, rows, cols):
        if row < 0 or row > rows - 1 or col < 0 or col > cols - 1:
            return False
        else:
            return True
