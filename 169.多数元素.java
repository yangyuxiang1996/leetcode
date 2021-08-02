import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=169 lang=java
 *
 * [169] 多数元素
 */

// @lc code=start
class Solution {
    public int majorityElement0(int[] nums) {
        // 使用hashmap
        HashMap<Integer, Integer> map = new HashMap<>();
        int n = nums.length;
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0)+1);
            if (map.get(num) > n / 2) {
                return num;
            }
        }
        return -1;
    }
    public int majorityElement(int[] nums) { 
        /*
        Boyer-Moore 投票算法
        维护一个候选众数 candidate 和它出现的次数 count。
        初始时 candidate 可以为任意值，count 为 0；
        遍历数组 nums 中的所有元素，对于每个元素 x，在判断 x 之前，
        如果 count 的值为 0，先将 x 的值赋予 candidate，随后判断 x：
        如果 x 与 candidate 相等，那么计数器 count 的值增加 1；
        如果 x 与 candidate 不等，那么计数器 count 的值减少 1。
        在遍历完成后，candidate 即为整个数组的众数。
        */
        int candidate = 0;
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            if (count == 0) { 
                candidate = nums[i];
            }
            if (candidate == nums[i]) {
                count++;
            } else {
                count--;
            }
        }
        return candidate;
    }
}
// @lc code=end

