#
# @lc app=leetcode.cn id=474 lang=python
#
# [474] 一和零
#

# @lc code=start
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[0] * (n+1) for _ in range(m+1)]
        for str in strs:
            zero_num, one_num = 0, 0
            for c in str:
                if c == '0':
                    zero_num += 1
                else:
                    one_num += 1

            for i in range(m, zero_num-1, -1):
                for j in range(n, one_num-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zero_num][j-one_num]+1)

        return dp[-1][-1]


if __name__ == '__main__':
    strs = ["10","0001","111001","1","0"]
    m, n = 5, 3
    print(Solution().findMaxForm(strs, m, n))


# @lc code=end

