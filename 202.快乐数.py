#
# @lc app=leetcode.cn id=202 lang=python
#
# [202] 快乐数
#

# @lc code=start
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mem = set()
        while n != 1:
            n = sum([int(i) **2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        return True
# @lc code=end

