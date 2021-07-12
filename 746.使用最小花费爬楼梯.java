/*
 * @lc app=leetcode.cn id=746 lang=java
 *
 * [746] 使用最小花费爬楼梯
 */

// @lc code=start
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        // 定义dp数组，dp[i]含义为楼层i所需要的最低花费
        int[] dp = new int[cost.length+1];
        
        // 初始化dp数组
        dp[0] = 0;
        dp[1] = 0;

        // 递推
        for (int i = 2; i < cost.length+1; i++) {
            dp[i] = Math.min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]);  // 动态转移方程
        }
        
        return dp[cost.length];

    }
}
// @lc code=end

