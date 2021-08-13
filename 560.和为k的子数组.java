import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=560 lang=java
 *
 * [560] 和为K的子数组
 */

// @lc code=start
class Solution {
    public int subarraySum(int[] nums, int k) {
        int[] sums = new int[nums.length+1];
        sums[0] = 0;
        int res = 0;
        for (int i = 1; i < nums.length+1; i++) {
            sums[i] = sums[i-1] + nums[i-1];
            for (int j = 0; j < i; j++) {
                if (sums[i] - sums[j] == k) {
                    res++;
                }
            }
        }
        return res;
    }

    public int subarraySum0(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        map.put(0, 1);
        int sum = 0;
        int res = 0;
        for (int num : nums) {
            sum += num;
            res += map.getOrDefault(sum-k, 0);
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        return res;
    }
}
// @lc code=end

