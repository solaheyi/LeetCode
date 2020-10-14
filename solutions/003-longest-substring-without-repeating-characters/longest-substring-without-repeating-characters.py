# -*- coding:utf-8 -*-


# Given a string s, find the length of the longest substring without repeating characters.
#
#  
# Example 1:
#
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
# Example 2:
#
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
# Example 3:
#
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
#
# Example 4:
#
#
# Input: s = ""
# Output: 0
#
#
#  
# Constraints:
#
#
# 	0 <= s.length <= 5 * 104
# 	s consists of English letters, digits, symbols and spaces.
#
#


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_set = set()
        rp, res = -1, 0
        n = len(s)
        for i in range(n):
            if i != 0:
                s_set.remove(s[i - 1])
            while rp+1 < n and s[rp + 1] not in s_set:
                s_set.add(s[rp+1])
                rp += 1
            res = max(res, rp - i + 1)
        return res
        
