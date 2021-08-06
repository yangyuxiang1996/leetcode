/*
 * @lc app=leetcode.cn id=461 lang=java
 *
 * [461] 汉明距离
 */

// @lc code=start
class Solution {
    public int hammingDistance0(int x, int y) {
        int s = x ^ y;
        int res = 0;
        while (s != 0) {
            res += s & 1;
            s >>= 1;
        }
        return res;
    }

    public int hammingDistance(int x, int y) {
        return Integer.bitCount(x ^ y);
    }
}
// @lc code=end

