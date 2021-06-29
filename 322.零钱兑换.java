/*
 * @lc app=leetcode.cn id=322 lang=java
 *
 * [322] 零钱兑换
 */

// @lc code=start
class CoinChange {
    public int coinChange(int[] coins, int amount) {
        // int[] memo = new int[amount+1];
        // return dp(coins, amount, memo);
        return helper(coins, amount);
        
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

    public int helper(int[] coins, int amount) {
        int[] dp = new int[amount+1];
        for (int i=0; i<dp.length; i++) {
            dp[i] = amount + 1;
        }
        dp[0]=0;
        for (int i=0; i <dp.length; i++) {
            for (int coin: coins) {
                if (i - coin < 0) continue;
                dp[i] = Math.min(dp[i], dp[i-coin]+1);
            }
        }
        return (dp[amount] != amount + 1) ? dp[amount] : -1;
    }
        
}
// @lc code=end

