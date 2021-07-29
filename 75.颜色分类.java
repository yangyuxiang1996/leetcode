/*
 * @lc app=leetcode.cn id=75 lang=java
 *
 * [75] 颜色分类
 */

// @lc code=start
class Solution {
    // public static void main (String[] args) {
    //     int[] nums = {1,2,0};
    //     new SortColors().sortColors(nums);
    //     for (int i = 0; i < nums.length; i++) {
    //         System.out.println(nums[i]);
    //     }
    // }
    public void sortColors(int[] nums) {
        // 双指针，一趟扫描，时间复杂度O(N)
        // 不断将0换到头部，将2换到尾部
        if (nums.length == 1) {
            return;
        }
        int start = 0;
        int end = nums.length - 1;
        int i = 0;
        while (i <= end) {
            if (nums[i] == 0) {
                swap(nums, start, i);
                i++;
                start++;
            } else if (nums[i] == 2) {
                swap(nums, i, end);
                end--;
            } else {
                i++;
            }
        }
    }
    
    public void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }

    public void sortColors0(int[] nums) {
        // 单指针，两趟扫描，时间复杂度O(N)
        // 第一趟扫描将所有的0换到前面，
        // 第二趟扫描将所有的1换到0的后面，两趟扫描结束后，后面的全是2
        if (nums.length == 1) {
            return;
        }
        int n = nums.length;
        int pre = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                int tmp = nums[pre];
                nums[pre] = nums[i];
                nums[i] = tmp;
                pre++;
            }
        }
        for (int i = pre; i < nums.length; i++) {
            if (nums[i] == 1) {
                int tmp = nums[pre];
                nums[pre] = nums[i];
                nums[i] = tmp;
                pre++;
            }

        }
    }
}
// @lc code=end

