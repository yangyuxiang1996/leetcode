/*
 * @lc app=leetcode.cn id=42 lang=java
 *
 * [42] 接雨水
 */

// @lc code=start
class Solution {
    public int trap1(int[] height) {
        // 双数组
        if (height.length == 0) {
            return 0;
        }
        int[] left_max = new int[height.length];
        int[] right_max = new int[height.length];
        left_max[0] = height[0];
        right_max[height.length - 1]  = height[height.length - 1];
        for (int i = 1; i < height.length; i++) {
            left_max[i] = Math.max(left_max[i-1], height[i]);
        }
        for (int i = height.length - 2; i >= 0; i--) {
            right_max[i] = Math.max(right_max[i+1], height[i]);
        }

        int res = 0;
        for (int i = 1; i < height.length-1; i++) {
            res += Math.min(left_max[i], right_max[i]) - height[i];
        }

        return res;

    }

    public int trap(int[] height) {
        // 双指针
        if (height.length == 0) {
            return 0;
        }
        int left = 0;
        int right = height.length-1;
        int left_max = 0;
        int right_max = 0;
        int res = 0;
        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] > left_max) {
                    left_max = height[left];
                } else {
                    res += left_max - height[left];
                }
                left += 1;
            } else {
                if (height[right] > right_max) {
                    right_max = height[right];
                } else {
                    res += right_max - height[right];
                }
                right -= 1;
            }
        }

        return  res;

    }
}
// @lc code=end

