import java.util.Arrays;
import java.util.Stack;

/*
 * @lc app=leetcode.cn id=503 lang=java
 *
 * [503] 下一个更大元素 II
 */

// @lc code=start
class Solution {
    public int[] nextGreaterElements(int[] nums) {
        Stack<Integer> stack = new Stack<Integer>();
        int[] result = new int[nums.length];
        Arrays.fill(result, -1);
        for (int i = 0; i < nums.length*2; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] < nums[i % nums.length]) {
                int idx = stack.pop();
                result[idx] = nums[i % nums.length];
            }
            stack.push(i % nums.length);
        }

        return result;
        

    }
}
// @lc code=end

