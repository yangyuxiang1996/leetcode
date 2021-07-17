import java.util.HashSet;
import java.util.List;
import java.util.Set;

/*
 * @lc app=leetcode.cn id=139 lang=java
 *
 * [139] 单词拆分
 */

// @lc code=start
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordDictSet = new HashSet<String>(wordDict);
        int n = s.length();
        boolean[] dp = new boolean[n+1];
        dp[0] = true;

        for (int j = 1; j < n+1; j++) {
            for (int i = 0; i < j; i++) {
                if (dp[i] && wordDictSet.contains(s.substring(i, j))) {
                    dp[j] = true;
                }
            }
        }
        return dp[n];
    }
        
}
// @lc code=end

