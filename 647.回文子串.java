/*
 * @lc app=leetcode.cn id=647 lang=java
 *
 * [647] 回文子串
 */

// @lc code=start
class Solution {
    public int countSubstrings0(String s) {
        // dp, dp[i:j]表示s中从i到j的字串是否为回文串
        if (s.length() <= 1) {
            return s.length();
        }
        int n = s.length();
        int res = 0;
        int[][] dp = new int[n][n];
        
        for (int i = n-1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (s.charAt(i) == s.charAt(j)) {
                    if (j - i < 3 || dp[i+1][j-1] == 1) {
                        dp[i][j] = 1;
                        res++;
                    }
                }
            }
        }
        return res;
    }
    public int countSubstrings1(String s) {
        // 中心扩散法
        if (s.length() <= 1) {
            return s.length();
        }
        int left = 0;
        int right = 0;
        int res = 0;
        for (int i = 0; i < 2*s.length()-1; i++) {
            left = i / 2;
            right = left + i%2;
            while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
                left--;
                right++;
                res++;
            }
        }
        return res;
    }

    public int countSubstrings(String s) {
        // 中心扩散法
        if (s.length() <= 1) {
            return s.length();
        }
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            res += countSubstrings(s, i, i);
            res += countSubstrings(s, i, i + 1);
        }
        return res;
    }
    
    public int countSubstrings(String s, int left, int right) {
        int res = 0;
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
            res++;
        }
        return res;

    }
}
// @lc code=end

