import java.util.Vector;

/*
 * @Description: 
 * @Author: yangyuxiang
 * @Date: 2021-04-27 07:46:17
 * @LastEditors: yangyuxiang
 * @LastEditTime: 2021-04-27 07:58:48
 * @FilePath: /leetcode/516.最长回文子序列.java
 */
/*
 * @lc app=leetcode.cn id=516 lang=java
 *
 * [516] 最长回文子序列
 */

// @lc code=start
class LongestPalindromeSubseq {
    public int longestPalindromeSubseq(String s) {
        if (s.length() <= 1) { 
            return s.length(); 
        }
        int[][] dp = new int[s.length()][s.length()];
        for (int i = s.length()-1; i >= 0; i--) {
            for (int j = i; j < s.length(); j++) {
                if (i == j) {
                    dp[i][j] = 1;
                    continue;
                }
                if (s.charAt(i) == s.charAt(j)) {
                    dp[i][j] = dp[i+1][j-1] + 2;
                } else {
                    dp[i][j] = Math.max(dp[i][j-1], dp[i+1][j]);
                }
                
            }
        }

        return dp[0][s.length()-1];


    }
}
// @lc code=end

