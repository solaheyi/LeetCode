# -*- coding:utf-8 -*-


# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# Example:
#
#
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
#
#


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        graph = [[0 for i in range(n)] for j in range(n)]
        row, col = 0, 0
        graph[row][col] = 1
        mo = 0
        count = 1
        while count < n ** 2:
            row_n, col_n = self.move(mo, row, col)
            if self.checkEdge(row_n, col_n, n, n) and not graph[row_n][col_n]:
                row, col = row_n, col_n
                count += 1
                graph[row][col] = count
            else:
                mo = (mo + 1) % 4
        return graph

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
