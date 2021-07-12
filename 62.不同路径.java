/*
 * @lc app=leetcode.cn id=62 lang=java
 *
 * [62] 不同路径
 */

// @lc code=start
class Solution {
    public int uniquePaths(int m, int n) {
        // 定义dp数组，dp[i][j]表示走到位置[i,j]有多少种方法
        int[][] dp = new int[m][n];
        // dp属猪初始化
        for(int i=0; i<m; i++){
            dp[i][0] = 1;
        }
        for(int j=0; j<n; j++){
            dp[0][j] = 1;
        }
        // 递推
        for(int i=1; i<m ;i++){
            for(int j=1; j<n; j++){
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            } 
        }

        return dp[m-1][n-1];

    }
}
// @lc code=end

