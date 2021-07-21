#
# @lc app=leetcode.cn id=516 lang=python
#
# [516] 最长回文子序列
#

# @lc code=start
class Solution(object):
    def longestPalindromeSubseq0(self, s):
        """
        :type s: str
        :rtype: int
        解法：求s和s反转后的字符串的最长公共子序列
        """
        if len(s) <= 1:
            return len(s)
        
        n = len(s)
        s1 = s
        s2 = "".join(list(s)[::-1])
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        解法：dp, 直接求最长回文子序列的长度，dp[i][j]表示s[i:j]的最长回文子序列的长度
        """
        if len(s) <= 1:
            return len(s)
        
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if j == i:
                    dp[i][j] = 1
                    continue
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][n-1]


if __name__ == '__main__':
    s = "cbbd"
    print(Solution().longestPalindromeSubseq(s))

# @lc code=end

