/*
 * @lc app=leetcode.cn id=718 lang=java
 *
 * [718] 最长重复子数组
 */

// @lc code=start
class Solution {
    public int findLength(int[] nums1, int[] nums2) {
        // 动态规划
        int n = nums1.length;
        int m = nums2.length;
        if (m == 0 || n == 0) { return 0; }

        int[][] dp = new int[n+1][m+1];
        int res = 0;
        for (int i = 1; i < n+1; i++) {
            for (int j = 1; j < m+1; j++) {
                if (nums1[i-1] == nums2[j-1]) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                }
                res = Math.max(res, dp[i][j]);
            }
            
        }
        return res;
    }
}
// @lc code=end

