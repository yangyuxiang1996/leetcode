import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/*
 * @lc app=leetcode.cn id=474 lang=java
 *
 * [474] 一和零
 */

// @lc code=start
class FindMaxForm {
    public static void main(String[] args) {
        String[] strs = {"0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"};
        int m = 9;
        int n = 80;
        System.out.println(new FindMaxForm().findMaxForm(strs, m, n));
    }

    public int findMaxForm(String[] strs, int m, int n) {
        // 回溯，超时。。。。
        if (strs.length == 0) {
            return 0;
        }
        backtrace(strs, m, n, path, 0, 0, 0);
        return res;

    }

    int res = 0;
    LinkedList<String> path = new LinkedList<>();
    public void backtrace(String[] strs, int m, int n, LinkedList<String> path, int c_0, int c_1, int start) {
        if (c_0 > m || c_1 > n) {
            return;
        }
        res = Math.max(res, path.size());
        for (int i = start; i < strs.length; i++) {
            c_0 += help(strs[i])[0];
            c_1 += help(strs[i])[1];
            path.add(strs[i]);
            backtrace(strs, m, n, path, c_0, c_1, i+1);
            c_0 -= help(strs[i])[0];
            c_1 -= help(strs[i])[1];
            path.removeLast();
        }

    }

    public int[] help(String str) {
        int i = 0;
        int j = 0;
        for (Character c : str.toCharArray()) {
            if (c == '0') {
                i += 1;
            } else if (c == '1') {
                j += 1;
            }
        }
        return new int[]{i,j};
    }
}
// @lc code=end

