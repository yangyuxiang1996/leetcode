

/*
 * @Description: 
 * @Author: yangyuxiang
 * @Date: 2021-04-20 16:29:17
 * @LastEditors: yangyuxiang
 * @LastEditTime: 2021-04-20 17:04:13
 * @FilePath: /leetcode/509.斐波那契数.java
 */
/*
 * @lc app=leetcode.cn id=509 lang=java
 *
 * [509] 斐波那契数
 */

// @lc code=start
class Fib {
    public static void main(String[] args) {
        System.out.println(new Fib().fib(10));
    }
    public int fib(int n) {
        // int[] memo = new int[n+1];
        return helper(n);
    }
    
    public int helper(int n, int[] memo) {
        // 递归解法， 自顶向下
        if (memo[n] != 0) {
            return memo[n];
        }
        if (n == 0 || n == 1) {
            return n;
        }
        memo[n] = helper(n-1, memo) + helper(n-2, memo);
        return memo[n];
    }

    public int helper(int n) {
        // 迭代解法，动态规划，自底向上
        if (n <= 1) {
            return n;
        }
        int[] dp = new int[n+1];
        dp[0] = 0;
        dp[1] = 1;
        for (int i=2; i < n+1; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }

}


// @lc code=end

