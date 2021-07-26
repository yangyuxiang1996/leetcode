import java.util.Deque;
import java.util.LinkedList;

/*
 * @lc app=leetcode.cn id=32 lang=java
 *
 * [32] 最长有效括号
 */

// @lc code=start
class Solution {
    public int longestValidParentheses0(String s) {
        // 栈
        if (s.length() <= 1) return 0;
        Deque<Integer> stack = new LinkedList<Integer>();
        stack.push(-1);
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            if (c == '(') {
                stack.push(i);
            } else {
                stack.pop();
                if (stack.isEmpty()) {
                    stack.push(i);  // 下一个起点的索引入栈
                } else {
                    res = Math.max(res, i - stack.peek());
                }
            }
        }
        return res;
    }

    public int longestValidParentheses(String s) {
        // 双指针
        if (s.length() <= 1) return 0;
        int left = 0;
        int right = 0;
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                left++;
            } else {
                right++;
            }
            if (left == right) {
                res = Math.max(res, 2*right);
            } else if (right > left) {
                left = right = 0;
            }
        }
        left = right = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == '(') {
                left++;
            } else {
                right++;
            }
            if (left == right) {
                res = Math.max(res, 2*left);
            }else if (left > right) {
                left = right = 0;
            }
        }

        return res;
    }

}
// @lc code=end

