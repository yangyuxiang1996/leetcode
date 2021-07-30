import java.util.Arrays;
import java.util.HashSet;

/*
 * @lc app=leetcode.cn id=128 lang=java
 *
 * [128] 最长连续序列
 */

// @lc code=start
class Solution {
    // public static void main(String[] args) {
    //     int[] nums = {100,4,200,1,3,2};
    //     System.out.println(new LongestConsecutive().longestConsecutive(nums));
    // }

    public int longestConsecutive0(int[] nums) {
        // 排序, 时间复杂度O(nlogn)
        if (nums.length == 0) {
            return 0;
        }
        Arrays.sort(nums);
        int res = 1;
        int cur = 1;
        for (int i = 1; i < nums.length; i++) {
            while (i < nums.length && nums[i] - nums[i-1] <= 1) {
                if (nums[i] - nums[i-1] == 1) {
                    cur++;
                }
                i++;
            }
            res = Math.max(res, cur);
            cur = 1;
        }
        return res;
    }
    public int longestConsecutive(int[] nums) {
        // 用set对nums进行去重
        if (nums.length == 0) {
            return 0;
        }

        HashSet<Integer> set = new HashSet<Integer>();
        for (int num : nums) {
            set.add(num);
        }
        int res = 0;
        int i;
        for (int num : nums) {
            int l1 = 0, l2 = 0;
            
            if (set.remove(num)) {
                i = num + 1;
                while (set.remove(i)) {
                    i++;
                    l1++;
                }
                i = num - 1;
                while (set.remove(i)) {
                    i--;
                    l2++;
                }
            }
            res = Math.max(res, l1+l2+1);
        }
        return res;
    } 
}
// @lc code=end

