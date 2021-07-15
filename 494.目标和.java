/*
 * @lc app=leetcode.cn id=494 lang=java
 *
 * [494] 目标和
 */

// @lc code=start
class FindTargetSumWays {
    public static void main(String[] args) {
        int[] nums = {1,1,1,1,1};
        int target = 3;
        System.out.println(new FindTargetSumWays().findTargetSumWays(nums, target));
    }

    public int findTargetSumWays(int[] nums, int target) {
        /*
        动态规划
        假设满足题目要求，把符号为正的放在左边，符号为负的放在右边，那么一定满足：
        left-right=target, 同时又有：
        left+right=sum(nums)，所以有
        2*left=target+sum(nums)，此时可以转换成01背包问题
        动态转移方程：dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
        表示背包容量为j时，在前i个元素中能够凑成和为j的方法有多少种
        */
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }
        if (sum < target || (sum + target) % 2 == 1) {
            return 0;
        }
        int left = (sum + target) / 2;
        int[] dp = new int[left + 1];
        dp[0] = 1;
        for (int i = 0; i < nums.length; i++) {
            for (int j = left; j >= nums[i]; j--) {
                dp[j] += dp[j - nums[i]];
            }
        }
        return dp[left];

    }


    public int findTargetSumWays1(int[] nums, int target) {
        // 深度优先+回溯
        if (nums.length == 0) {
            return 0;
        }
        backtrace(nums, target, 0, 0);
        return res;
    }

    int res = 0;
    int[] ops = {1, -1};

    public void backtrace(int[] nums, int target, int i, int tmp) {
        if (i == nums.length) {
            if (tmp == target) {
                res += 1;
            }
            return;
        }

        for (int op : ops) {
            tmp += op * nums[i];
            backtrace(nums, target, i+1, tmp);
            tmp -= op * nums[i];
        }

    }
}
// @lc code=end

