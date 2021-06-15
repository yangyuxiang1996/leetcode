import java.util.HashMap;
import java.util.Map;

/*
 * @Description: 
 * @Author: yangyuxiang
 * @Date: 2021-04-25 11:04:41
 * @LastEditors: yangyuxiang
 * @LastEditTime: 2021-04-25 11:14:30
 * @FilePath: /leetcode/3.无重复字符的最长子串.java
 */
/*
 * @lc app=leetcode.cn id=3 lang=java
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start
class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        Map<Character, Integer> window = new HashMap<Character, Integer>();
        int left=0;
        int right=0;
        int maxLength=0;
        while (right < s.length()) {
            Character c = s.charAt(right);
            right++;
            window.put(c, window.getOrDefault(c, 0) + 1);

            while (window.get(c) > 1) {
                Character d = s.charAt(left);
                left++;
                window.put(d, window.get(d) - 1);
                
            }
            maxLength = Math.max(maxLength, right - left);
        }
        return maxLength;
    }
}
// @lc code=end

