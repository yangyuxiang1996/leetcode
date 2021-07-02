#
# @lc app=leetcode.cn id=131 lang=python
#
# [131] 分割回文串
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 1:
            return [[s]]
        
        self.res = []
        def backtrace(s, start, path):
            if start >= len(s):
                self.res.append(path[:])

            for i in range(start, len(s)):
                if self.isPalindrome(s, start, i):
                    path.append(s[start:i+1])
                    backtrace(s, i+1, path)
                    path.pop()
                else:
                    continue


        backtrace(s, 0, [])
        return self.res


        

# @lc code=end

