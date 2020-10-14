# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
#
#  
#
#
# Example 1:
#
#
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
#
#
#
# Example 2:
#
#
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
#
#  
#
# Note:
#
#
# 	1 <= A.length <= 10000
# 	-10000 <= A[i] <= 10000
# 	A is sorted in non-decreasing order.
#
#
#


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        num = len(A)
        right = 0
        res = []
        while right < num and A[right] <=0 :
            right += 1
        left = right - 1
        while 0 <= left and right < num :
            if A[left]**2 <= A[right]**2:
                res.append(A[left]**2)
                left -= 1
            else:
                res.append(A[right]**2)
                right += 1
        
        while right < num :
            res.append(A[right]**2)
            right += 1
        while 0 <= left :
            res.append(A[left]**2)
            left -= 1
        return res
