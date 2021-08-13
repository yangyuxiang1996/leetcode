#
# @lc app=leetcode.cn id=312 lang=python
#
# [312] 戳气球
#

# @lc code=start
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划，令dp[i][j]表示戳破（i，j）之间的气球的最大得分
        # dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+points[i]*points[k]*points[j]),  i+1 <= k < j
        # https://zhuanlan.zhihu.com/p/144384951
        points = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * (n+2) for i in range(n+2)]
        for i in range(n, -1, -1):
            for j in range(i+1, n+2):
                for k in range(i+1, j):
                    dp[i][j] = max(
                        dp[i][j], dp[i][k] + dp[k][j] +
                        points[i] * points[k] * points[j])
        return dp[0][n+1]


# @lc code=end
