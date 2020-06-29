# -*- coding:utf-8 -*-


# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
#
# Input: ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Note:
#
# All given inputs are in lowercase letters a-z.
#


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        if not strs:
            return res
        lenth = len(strs)
        for i in range(len(strs[0])):
            for j in range(1, lenth):
                if i == len(strs[j]) or strs[0][i] != strs[j][i]:
                    return res
            res += strs[0][i]
        return res
