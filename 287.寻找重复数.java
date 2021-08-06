import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=287 lang=java
 *
 * [287] 寻找重复数
 */

// @lc code=start
class Solution {
    public int findDuplicate0(int[] nums) {
        // 暴力解法, O(n2),超时
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                if (nums[j] == nums[i]) {
                    return nums[i];
                }
            }
        }
        return -1;
    }

    public int findDuplicate1(int[] nums) {
        // hash table
        // 时间复杂度O(n), 空间复杂度O(n)
        int n = nums.length;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < n; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0)+1);
            if (map.get(nums[i]) > 1) {
                return nums[i];
            }
        }
        return -1;
    }

    public int findDuplicate(int[] nums) {
        // 快慢指针
        // https://leetcode-cn.com/problems/find-the-duplicate-number/solution/287xun-zhao-zhong-fu-shu-by-kirsche/
        int slow = 0, fast = 0;
        slow = nums[slow]; // slow = slow.next
        fast = nums[nums[fast]]; // fast = fast.next.next
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[nums[fast]];
        }
        int pre1 = 0;
        int pre2 = slow;
        while (pre1 != pre2) {
            pre1 = nums[pre1];  // slow = slow.next
            pre2 = nums[pre2];  // fast = fast.next
        }
        return pre1;
    }

}
// @lc code=end

