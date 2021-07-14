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
}
// @lc code=end

