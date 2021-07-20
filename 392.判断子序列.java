import java.util.Arrays;

/*
 * @lc app=leetcode.cn id=392 lang=java
 *
 * [392] 判断子序列
 */

// @lc code=start
class Solution {
    // public static void main(String[] args) {
    //     String s = "axc";
    //     String t = "ahbgdc";
    //     System.out.println(new IsSubsequence().isSubsequence(s, t));
    // }
    public boolean isSubsequence0(String s, String t) {
        // dp
        if (s.length() == 0) { return true; }
        if (t.length() == 0) { return false; }
        if (s.length() > t.length()) { return false; }
        int m = s.length();
        int n = t.length();
        boolean[][] dp = new boolean[m+1][n+1];
        for (int i = 0; i <= m; i++) {
            dp[i][0] = false; // 注意这里初始化
        }
        for (int j = 0; j <= n; j++) {
            dp[0][j] = true;
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s.charAt(i-1) == t.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1];
                } else {
                    dp[i][j] = dp[i][j-1];
                }
            }
        }
        return dp[m][n];
    }

    public boolean isSubsequence(String s, String t) {
        // 双指针
        if (s.length() == 0) { return true; }
        if (t.length() == 0) { return false; }
        if (s.length() > t.length()) { return false; }

        int i = 0;
        int j = 0;
        while (i < s.length() && j < t.length()) {
            if (s.charAt(i) == t.charAt(j)) {
                i++;
                j++;
            } else {
                j++;
            }
            if (i == s.length()) { return true;}
        }
        return false;

    }
}
// @lc code=end

