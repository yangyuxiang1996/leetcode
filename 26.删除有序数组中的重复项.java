/*
 * @lc app=leetcode.cn id=26 lang=java
 *
 * [26] 删除有序数组中的重复项
 */

// @lc code=start
class removeDuplicates {
    public int removeDuplicates(int[] nums) {
        int slow = 1;
        int fast = 1;
        while (fast < nums.length) {
            if (nums[fast] != nums[fast-1]) {
                nums[slow] = nums[fast];
                slow++;  
            }
            fast++; 
        }
        return slow;

    }
}
// @lc code=end

