/*
 * @lc app=leetcode.cn id=322 lang=java
 *
 * [322] 零钱兑换
 */

// @lc code=start
class Solution {
    public int coinChange(int[] coins, int amount) {
        // 完全背包问题
        int[] dp = new int[amount+1];
        for (int i=1; i < amount+1; i++){
            dp[i] = amount+1;
        }
        dp[0] = 0;

        for (int i=0; i < coins.length; i++){
            for (int j=1; j < amount+1; j++){
                if (j - coins[i] >= 0){
                    dp[j] = Math.min(dp[j], dp[j-coins[i]]+1);
                }
            }
        }
        return dp[amount] != amount+1 ? dp[amount] : -1;
        
    }

    public int coinChange0(int[] coins, int amount) {
        int[] memo = new int[amount+1];
        return dp(coins, amount, memo);
        
    }
    public int dp(int[] coins, int amount, int[] memo) {
        if (amount < 0) return -1;
        if (amount == 0) return 0;
        if (memo[amount] != 0) return memo[amount];

        int count = Integer.MAX_VALUE;
        for (int coin : coins) {
            int sub = dp(coins, amount-coin, memo);
            if (sub == -1) continue;
            count = Math.min(count, sub+1);
        }
        if (count != Integer.MAX_VALUE) {
            memo[amount] = count;
        } else{
            memo[amount] = -1;
        }
        return memo[amount];
    }
        
}
// @lc code=end

