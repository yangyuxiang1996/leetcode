#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] 回文数
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        
        l = []
        l.append(x%10)
        x //= 10
        while x != 0:
            l.append(x%10)
            x //= 10
        
        # print(l)
        left = 0
        right = len(l)-1
        while left <= right:
            if l[left] != l[right]:
                return False
            left += 1
            right -= 1
        return True


    def isPalindrome0(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
            
        l = list(str(x))
        n = len(l)
        if n == 1:
            return True
        
        left = 0
        right = len(l)-1
        while left <= right:
            if l[left] != l[right]:
                return False
            left += 1
            right -= 1
        return True
# @lc code=end

