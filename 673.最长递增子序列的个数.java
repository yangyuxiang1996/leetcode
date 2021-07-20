import java.util.Arrays;

/*
 * @lc app=leetcode.cn id=673 lang=java
 *
 * [673] 最长递增子序列的个数
 */

// @lc code=start
class Solution {
    public int findNumberOfLIS(int[] nums) {
         // 动态规划
         int n = nums.length;
         int[] dp = new int[n];
         int[] count = new int[n];
         Arrays.fill(dp, 1);
         Arrays.fill(count, 1);
         int max_length = 0;

         for (int i = 1; i < n; i++) {
             for (int j = 0; j < i; j++) {
                 if (nums[j] < nums[i]) {
                     if (dp[j] >= dp[i]) {
                         dp[i] = dp[j]+1;
                         count[i] = count[j];
                     } else if (dp[j]+1 == dp[i]) {
                        count[i] += count[j];
                     }
                 }
             }
             if (dp[i] > max_length) {
                 max_length = dp[i];
             }
         }

         int res = 0;
         for (int i = 0; i < n; i++) {
             if (dp[i] == max_length) {
                 res += count[i];
             }
         }
         return n == 1 ? 1 : res;
    }
}
// @lc code=end

