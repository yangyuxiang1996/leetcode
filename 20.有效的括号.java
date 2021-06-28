import java.util.Map;
import java.util.Stack;

/*
 * @lc app=leetcode.cn id=20 lang=java
 *
 * [20] 有效的括号
 */

// @lc code=start
class Solution {
    public boolean isValid(String s) {
        if (s.isEmpty()) {
            return false;
        }
        Map<Character, Character> m = new HashMap<Character, Character>();
        m.put('}', '{');
        m.put(']', '[');
        m.put(')', '(');
        Stack<Character> stack = new Stack<Character>();

        for (Character c : s.toCharArray()) {
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else {
                if (!stack.isEmpty() && m.get(c) == stack.peek()) {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
// @lc code=end

