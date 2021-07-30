/*
 * @lc app=leetcode.cn id=125 lang=java
 *
 * [125] 验证回文串
 */

// @lc code=start
class Solution {
    // public static void main(String[] args) {
    //     String s = "A man, a plan, a canal: Panama";
    //     System.out.println(new IsPalindrome().isPalindrome(s));
    // }
    public boolean isDigit(Character c) {
        return c >= '0' && c <= '9';
    }
    public boolean isAlpha(Character c) {
         return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');
    }
    public String toLowerCase(String s) {
        return s.toLowerCase();
    }
    public boolean isPalindrome(String s) {
        if (s.length() <= 1) {
            return true;
        }
        s = toLowerCase(s);
        int n = s.length();
        int left = 0, right = n-1;
        while (left <= right) {
            while (left < n && !isDigit(s.charAt(left)) && !isAlpha(s.charAt(left))){
                left++;
            } 
            while (right >= 0 && !isDigit(s.charAt(right)) && !isAlpha(s.charAt(right))){
                right--;
            }
            if (left >= n || right < 0) {
                break;
            }
            Character l = s.charAt(left);
            Character r = s.charAt(right);
            if (l != r) {
                return false;
            }
            left++;
            right--;
        }
        return true;

    }
}
// @lc code=end

