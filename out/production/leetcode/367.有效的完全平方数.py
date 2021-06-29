#
# @lc app=leetcode.cn id=367 lang=python
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if not num:
            return False
        
        left, right = 0, num
        while left <= right:
            mid = left + (right - left) // 2
            if mid*mid == num:
                return True
            elif mid*mid > num:
                right = mid-1
            elif mid*mid < num:
                left = mid + 1
        return False
# @lc code=end

