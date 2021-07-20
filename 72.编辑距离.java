/*
 * @lc app=leetcode.cn id=72 lang=java
 *
 * [72] 编辑距离
 */

// @lc code=start
class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        if (m == 0 || n == 0) {
            return m == 0 ? n : m;
        }
        // dp, dp[i][j]表示word1[0:i]替换为word2[:j]的最少操作次数
        // if word1[i-1] == word2[j-1], 那么 dp[i][j] = dp[i-1][j-1]；
        // if word1[i-1] != word2[j-1]，那么，从插入/删除/替换中选择最小的操作次数
        // 插入：min(dp[i-1][j], dp[i][j-1])+1，例如当单词 A 为 da B 为 bd 时, da经过2次变成b, 然后在b的后面插入d，或者bd经过一次变成d，然后在d的后面插入a；
        // 删除：对单词 A 删除一个字符和对单词 B 插入一个字符是等价的。例如当单词 A 为 doge，单词 B 为 dog 时，我们既可以删除单词 A 的最后一个字符 e，得到相同的 dog，也可以在单词 B 末尾添加一个字符 e，得到相同的 doge；
        // 替换：dp[i-1][j-1]+1

        int[][] dp = new int[m+1][n+1];
        for (int i = 0; i <= m; i++) {
            dp[i][0] = i;
        }
        for (int j = 0; j <= n; j++) {
            dp[0][j] = j;
        }
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1.charAt(i-1) == word2.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1];
                } else {
                    dp[i][j] = Math.min(dp[i-1][j]+1, dp[i][j-1]+1);
                    dp[i][j] = Math.min(dp[i][j], dp[i-1][j-1]+1);
                }
            }
        }
        return dp[m][n];

    }
}
// @lc code=end

