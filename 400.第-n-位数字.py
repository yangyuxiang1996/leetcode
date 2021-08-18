#
# @lc app=leetcode.cn id=400 lang=python
#
# [400] 第 N 位数字
#

# @lc code=start
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n
        
        start, digit, count = 1 ,1, 9
        while n > count:
            n -= count
            start *= 10
            digit += 1
            count = start * digit * 9

        num = start + (n-1)//digit
        s = str(num)
        res = s[(n-1)%digit]
        return int(res)
# @lc code=end

