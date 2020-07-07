# -*- coding:utf-8 -*-


# The set [1,2,3,...,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
#
#
# 	"123"
# 	"132"
# 	"213"
# 	"231"
# 	"312"
# 	"321"
#
#
# Given n and k, return the kth permutation sequence.
#
# Note:
#
#
# 	Given n will be between 1 and 9 inclusive.
# 	Given k will be between 1 and n! inclusive.
#
#
# Example 1:
#
#
# Input: n = 3, k = 3
# Output: "213"
#
#
# Example 2:
#
#
# Input: n = 4, k = 9
# Output: "2314"
#
#


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorial = {'1': 1, '2': 2, '3': 6, '4': 24, '5': 120, '6': 720, '7': 5040, '8': 40320, '9':362880}
        nums = [i for i in range(1, n+1)]
        res = ''
        for i in range(n-1, 0, -1):
            if k % factorial.get(str(i)):
                res += str(nums.pop(k // factorial.get(str(i))))
            else:
                res += str(nums.pop((k // factorial.get(str(i)) - 1)))
            k %= factorial.get(str(i))
        res = res + str(nums[0])
        return res
