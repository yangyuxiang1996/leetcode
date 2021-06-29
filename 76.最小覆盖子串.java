import java.util.HashMap;
import java.util.Map;

/*
 * @Description: 
 * @Author: yangyuxiang
 * @Date: 2021-04-23 07:39:38
 * @LastEditors: yangyuxiang
 * @LastEditTime: 2021-04-23 08:56:14
 * @FilePath: /leetcode/76.最小覆盖子串.java
 */
/*
 * @lc app=leetcode.cn id=76 lang=java
 *
 * [76] 最小覆盖子串
 */

// @lc code=start
class MinWindow {
    public String minWindow(String s, String t) {
        if(s==null||s.isEmpty()||t==null||t.isEmpty()) return "";
        int left = 0;
        int right = 0;
        Map<Character, Integer> needed = new HashMap<Character, Integer>();
        for (char c : t.toCharArray()) {
            needed.put(c, needed.getOrDefault(c, 0) + 1);
        } 
        Map<Character, Integer> window = new HashMap<Character, Integer>();
        int valid = 0;
        int start = 0;
        int len = Integer.MAX_VALUE;
        String res = "";
        
        while (right < s.length()) {
            char c = s.charAt(right);
            if (needed.containsKey(c)) {
                window.put(c, window.getOrDefault(c, 0) + 1);
                if (needed.get(c).equals(window.get(c))) {
                    valid++;
                }
            }
            right++;

            while (valid == needed.size()) {
                if (right - left < len) {
                    len = right - left;
                    res = s.substring(left, right);
                }
                char d = s.charAt(left);
                left++;
                if (needed.containsKey(d)){
                    if (needed.get(d).equals(window.get(d))) {
                        valid--;
                    }
                    window.put(d, window.getOrDefault(d, 0) - 1);
                }
            }
        }
        return res;

        
    }
}
// @lc code=end

