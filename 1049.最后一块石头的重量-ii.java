/*
 * @lc app=leetcode.cn id=1049 lang=java
 *
 * [1049] 最后一块石头的重量 II
 * 基本思路：最大可能将一堆石头分成两部分，使得两部分重量之差尽可能小，这个重量之差即是最多只剩下一块石头的最小可能重量
 * 解法：01背包，定义一维dp数组，dp[j]表示当前背包容容量为j时所能装的最大石头重量
 */

// @lc code=start
class Solution {
    public int lastStoneWeightII(int[] stones) {
        int sum = 0;
        for (int i = 0; i < stones.length; i++) {
            sum += stones[i];
        }
        int target = sum / 2;

        int[] dp = new int[target+1];
        dp[0] = 0;
        for (int i = 0; i < stones.length; i++) {
            for (int j = target; j >= stones[i]; j--) {
                dp[j] = Math.max(dp[j], dp[j-stones[i]] + stones[i]);
            }
        }

        return sum - dp[target] - dp[target];
    }

    public int lastStoneWeightII1(int[] stones) {
        int sum = 0;
        for (int i = 0; i < stones.length; i++) {
            sum += stones[i];
        }
        int target = sum / 2;

        int[][] dp = new int[stones.length+1][target+1];
        for (int i = 1; i < stones.length+1; i++) {
            for (int j = 0; j < target+1; j++) {
                if (j - stones[i-1] >= 0) {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-stones[i-1]] + stones[i-1]);
                } else {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        return sum - 2 * dp[stones.length][target];

    }
}
// @lc code=end

