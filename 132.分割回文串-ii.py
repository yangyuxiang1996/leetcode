#
# @lc app=leetcode.cn id=132 lang=python
#
# [132] 分割回文串 II
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s, left, right):
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
 
    def minCut0(self, s):
        """
        :type s: str
        :rtype: int
        回溯法：超时
        """
        self.min_step = len(s)
        
        def backtrace(s, start, step):
            if start >= len(s):
                self.min_step = min(self.min_step, step)
                return
            
            for i in range(start, len(s)):
                if self.isPalindrome(s, start, i):
                    step += 1
                    backtrace(s, i+1, step)
                    step -= 1
                else:
                    continue
            return
        
        backtrace(s, 0, 0)
        return self.min_step - 1

    
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        动态递归：
        令f[i]表示字串s[0:i]的最小分割次数，可以得到如下状态转移方程：
        f[i] = min(f[0:i]) + 1
        """
        n = len(s)
        g = [[True] * n for i in range(n)]  # g[i][j]表示s中以i开头，j结尾的字串是否为回文串

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]  # 判断是否为回文串的状态转移方程

        f = [float("inf")] * n  # f[i]表示字串s中，区间[0,i]的最小分割次数
        for i in range(n):
            if g[0][i]:  # 如果以i结尾的字串为回文串，最小分割次数为0
                f[i] = 0
            else:  # 否则，往前找最后一个分割出来的回文串
                for j in range(i):  # j表示前一个回文串的开始位置
                    if g[j + 1][i]:  # 如果区间[j+1,i]是回文串，f[j]+1就是f[i]的最小分割次数
                        f[i] = min(f[i], f[j] + 1)
        
        return f[n - 1]





if __name__ == '__main__':
    s = "ababacababa"
    print(Solution().minCut(s))

# @lc code=end

