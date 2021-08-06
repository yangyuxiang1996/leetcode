import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/*
 * @lc app=leetcode.cn id=448 lang=java
 *
 * [448] 找到所有数组中消失的数字
 */

// @lc code=start
class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        // 原地标记，获取每个元素的索引，并在索引位置加n
        // 例如，如果nums[i]=3,那么在nums[2]处加n,这样出现过的数字作为索引，其所在位置的值一定大于n
        List<Integer> result = new ArrayList<Integer>();
        int n = nums.length;
        for (int num : nums) {
            nums[(num-1) % n] += n;
        }
        for (int i = 0; i < n; i++) {
            if (nums[i] <= n) {
                result.add(i+1);
            }
        }
        return result;
    }

    public List<Integer> findDisappearedNumbers1(int[] nums) {
        // hash set, 时间复杂度O(n), 空间复杂度O(n)
        Set<Integer> set = new HashSet<Integer>();
        List<Integer> result = new ArrayList<Integer>();
        for (int i = 0; i < nums.length; i++) {
            set.add(nums[i]);
        }
        for (int i = 1; i <= nums.length; i++) {
            if (!set.contains(i)) {
                result.add(i);
            }
        }
        return result;
    }

    public List<Integer> findDisappearedNumbers0(int[] nums) {
        // 暴力解法, 时间复杂度O(n2)，超时
        List<Integer> result = new ArrayList<Integer>();
        for (int i = 1; i <= nums.length; i++) {
            boolean flag = false;
            for (int j = 0; j < nums.length; j++) {
                if (nums[j] == i) {
                    flag = true;
                    break;
                }
            }
            if (!flag) {
                result.add(i);
            }
        }
        return result;
    }
}
// @lc code=end

