#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] x 的平方根
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid**2 <= x < (mid+1)**2:
                return mid
            elif mid**2 > x:
                right = mid - 1
            elif mid**2 < x:
                left = mid + 1

        return left-1
# @lc code=end

