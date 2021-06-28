#
# @lc app=leetcode.cn id=459 lang=python
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution(object):
    def getNext(self, s):
        n = len(s)
        next = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = next[j-1]
            if s[i] == s[j]:
                j+=1
            next[i] = j
        return next

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return False
        next = self.getNext(s)
        if next[n-1] != 0 and n % (n - next[n-1]) == 0:
            return True
        return False


if __name__ == '__main__':
    s = "abcabc"
    print(Solution().repeatedSubstringPattern(s))

        
        

# @lc code=end

