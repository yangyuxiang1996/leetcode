/*
 * @lc app=leetcode.cn id=238 lang=java
 *
 * [238] 除自身以外数组的乘积
 */

// @lc code=start
class Solution {
    public int[] productExceptSelf(int[] nums) {
        // 直接将输出数组初始化为当前元素左边所有元素乘积，然后再反向遍历，修改输出数组
        int n = nums.length;
        int[] output = new int[n];
        output[0] = 1;
        for (int i = 1; i < n; i++) {
            output[i] = output[i - 1] * nums[i - 1];
        }
        int right = 1;
        for (int i = n-1; i >= 0; i--) {
            output[i] = output[i] * right;
            right *= nums[i];
        }
        return output;
    }
    
    public int[] productExceptSelf0(int[] nums) {
        // 两次遍历，时间复杂度O(n), 空间复杂度O(n)
        int n = nums.length;
        int[] left = new int[n];
        int[] right = new int[n];
        int[] output = new int[n];
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                left[i] = 1;
            }else{
                left[i] = left[i - 1] * nums[i - 1];
            }
        }
        for (int i = n-1; i >=0; i--) {
            if (i == n-1) {
                right[i] = 1;
            }else{
                right[i] = right[i + 1] * nums[i + 1];
            }
        }
        for (int i = 0; i < n; i++){
            output[i] = left[i] * right[i];
        }
        return output;
    }
}
// @lc code=end

