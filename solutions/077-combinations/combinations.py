# -*- coding:utf-8 -*-


# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# You may return the answer in any order.
#
#  
# Example 1:
#
#
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#
#
# Example 2:
#
#
# Input: n = 1, k = 1
# Output: [[1]]
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 20
# 	1 <= k <= n
#
#


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(first = 1, tmp = []):
            if len(tmp) == k:
                res.append(tmp[:])
            for i in range(first, n + 1):
                tmp.append(i)
                backtrack(i + 1, tmp)
                tmp.pop()
        res = []
        backtrack()
        return res
