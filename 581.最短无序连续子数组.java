/*
 * @lc app=leetcode.cn id=581 lang=java
 *
 * [581] 最短无序连续子数组
 */

// @lc code=start
class Solution {
//     public static void main(String[] args) {
//         int[] nums = new int[]{2,6,4,8,10,9,15};
//         System.out.println(new FindUnsortedSubarray().findUnsortedSubarray(nums));
//     }

    public int findUnsortedSubarray(int[] nums) {
        // 双指针，两次遍历
        // 第一次从左往右，找中间数组的右边界，初始化right为-1；
        // 第二次从右往左，找中间数组的左边界，初始化left为-1；
        int n = nums.length;
        int maxn = Integer.MIN_VALUE, right = -1;
        int minn = Integer.MAX_VALUE, left = -1;
        // 从左到右，更新right
        for (int i = 0; i < n; i++){
            if (nums[i] >= maxn) {
                maxn = nums[i];
            }else {
                right = i;
            }
        }
        // 从右往左，更新left
        for (int i = n-1; i >= 0; i--) {
            if (nums[i] <= minn) {
                minn = nums[i];
            }else {
                left = i;
            }
        }
        // right=-1表示一直升序
        if (right == -1) {
            return 0;
        }
        return right - left + 1;

    }
}
// @lc code=end

