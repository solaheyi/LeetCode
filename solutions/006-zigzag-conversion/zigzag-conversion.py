# -*- coding:utf-8 -*-


# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
#
# string convert(string s, int numRows);
#
#
#  
# Example 1:
#
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#
#
# Example 2:
#
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#
#
# Example 3:
#
#
# Input: s = "A", numRows = 1
# Output: "A"
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 1000
# 	s consists of English letters (lower-case and upper-case), ',' and '.'.
# 	1 <= numRows <= 1000
#
#


class Solution(object):
    def convert(self, s, numRows):
        convert = []
        s = list(s)
        while s:
            count = 0
            aalist = [None] * numRows
            while s and count < numRows:
                aalist[count] = s.pop(0)
                count += 1
            rcount = 0
            convert += aalist
            while s and rcount < numRows - 2:
                alist = [None] * numRows
                alist[numRows - 2 - rcount] = s.pop(0)
                convert += alist
                rcount += 1
        result = ''
        for i in range(numRows):
            for j in range(len(convert)//numRows):
                if convert[j*numRows+i]:
                    result += convert[j*numRows+i]
        return result
            
        
