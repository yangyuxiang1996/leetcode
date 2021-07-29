/*
 * @lc app=leetcode.cn id=33 lang=java
 *
 * [33] 搜索旋转排序数组
 */

// @lc code=start
class Search {

    public static void main(String[] args) {
        int[] nums = {4,5,6,7,0,1,2};
        System.out.println(new Search().search(nums, 3));
    }
    public int search(int[] nums, int target) {
        // 二分
        if(nums.length == 1) {
            return nums[0] == target ? 0 : -1;
        }
        if (nums.length > 1) {
            if (target < nums[0] && target > nums[nums.length-1]) {
                return -1;
            }
        }

        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (target == nums[mid]) {
                return mid;
            }
            if (nums[left] <= nums[mid]) {
                // 说明区间[left, mid]是递增的
                if (nums[left] < target && target < nums[mid]) {
                    right = mid - 1;
                } else if (target < nums[left]) {
                    left = mid + 1;
                } else if (target > nums[mid]) {
                    left = mid + 1;
                } else {
                    return left;
                }
            } else {
                // 说明区间[mid, right]是递增的
                if (nums[mid] < target && target < nums[right]) {
                    left = mid + 1;
                } else if (target < nums[mid]) {
                    right = mid - 1;
                } else if (target > nums[right]) {
                    right = mid - 1;
                } else {
                    return right;
                }
            }
        }
        return -1;
    }

    public int search0(int[] nums, int target) {
        // 时间复杂度：O(N)
        if(nums.length == 1) {
            return nums[0] == target ? 0 : -1;
        }
        if (nums.length > 1) {
            if (target < nums[0] && target > nums[nums.length-1]) {
                return -1;
            }
        }

        int i = 0;
        if (nums[0] <= target) {
            // 从前往后
            i = 0;
            while (i < nums.length-1 && nums[i] < nums[i+1]) {
                if (nums[i] == target) {
                    return i;
                }
                i += 1;
            }
        } else {
            // 从后往前
            i = nums.length - 1;
            while (i > 0 && nums[i] > nums[i-1]) {
                if (nums[i] == target) {
                    return i;
                }
                i -= 1;
            }
        }
        if (nums[i] == target) {
            return i;
        }
        return -1;
    }
}
// @lc code=end

