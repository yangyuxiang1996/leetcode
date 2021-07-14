/*
 * @lc app=leetcode.cn id=416 lang=java
 *
 * [416] 分割等和子集
 */

// @lc code=start
class CanPartition {
    public static void main(String[] args) {
        int[] nums = {1,5,10,6};
        System.out.println(new CanPartition().canPartition1(nums));
    }

    public boolean canPartition(int[] nums) {
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }
        if (sum % 2 == 1) {
            return false;
        }
        int target = sum / 2;

        // 定义二维dp数组
        int[][] dp = new int[nums.length][target+1];
        // 初始化dp数组
        for (int i = 0; i < nums.length; i++) {
            dp[i][0] = 1;
        }
        for (int j = 1; j < target+1; j++) {
            if (j == nums[0]) {
                dp[0][j] = 1;
            } else {
                dp[0][j] = 0;
            }
        }

        for (int i = 1; i < nums.length; i++) {
            for (int j = 1; j < target+1; j++) {
                if (j - nums[i] >= 0) {
                    if (dp[i-1][j] == 1 || dp[i-1][j-nums[i]] == 1) {
                        dp[i][j] = 1;
                    }
                } else {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }

        return dp[nums.length-1][target] == 1 ? true : false;
    }
    public boolean canPartition1(int[] nums) {
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }
        if (sum % 2 == 1) {
            return false;
        }
        int target = sum / 2;
        // 定义一维dp数组
        int[] dp = new int[target+1];
        dp[0] = 1;
        for (int i = 0; i < nums.length; i++) {
            for (int j = target; j > 0; j--) {
                if (j - nums[i] >= 0) {
                    if (dp[j] == 1 || dp[j - nums[i]] == 1) {
                        dp[j] = 1;
                    }
                }
            }
        }

        return dp[target] == 1 ? true : false;
    }
}
// @lc code=end

