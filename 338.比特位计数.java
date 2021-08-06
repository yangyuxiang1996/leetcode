/*
 * @lc app=leetcode.cn id=338 lang=java
 *
 * [338] 比特位计数
 */

// @lc code=start
class Solution {
    public int[] countBits(int n) {
        // 根据奇偶性判断
        int[] res = new int[n+1];
        res[0] = 0;
        for (int i = 1; i < res.length; i++) {
            if (i % 2 == 1) {
                res[i] = res[i-1] + 1;  //奇数，比前面的偶数多最低位的0
            } else {
                res[i] = res[i / 2];  // 偶数， 除以2， 相当于抹去最低位的0，1的个数不变
            }
        }
        return res;
    }

    public int[] countBits1(int n) {
        // Brian Kernighan 算法
        // 对于任意整数x，令x=x & (x−1)，该运算将 x 的二进制表示的最后一个 1 变成 0。因此，对 x 重复该操作，直到 x 变成 0，则操作次数即为 x 的「一比特数」。
        int[] res = new int[n+1];
        for (int i = 0; i < n+1; i++) {
            int ones = 0;
            int x = i;
            while (x > 0) {
                x &= x - 1;
                ones++;
            }
            res[i] = ones;
        }
        return res;
    }

    public int[] countBits0(int n) {
        // 二进制向右移位，判断最低位出现1的次数
        int[] res = new int[n+1];
        res[0] = 0;
        for (int i = 1; i < n+1; i++) {
            int k = i;
            while (k != 0) {
                res[i] += k & 1;
                k >>= 1;
            }
        }
        return res;
    }
}
// @lc code=end

