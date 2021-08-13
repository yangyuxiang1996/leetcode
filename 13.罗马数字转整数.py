#
# @lc app=leetcode.cn id=13 lang=python
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 
             'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 
             'XL':40, 'XC':90, 'CD':400, 'CM':900}
        i = 0
        res = 0
        while i < len(s):
            if s[i:i+2] in m:
                res += m[s[i:i+2]]
                i += 2
            else:
                res += m[s[i]]
                i += 1
        return res



# @lc code=end
