import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/*
 * @Description: 
 * @Author: yangyuxiang
 * @Date: 2021-04-21 22:35:20
 * @LastEditors: yangyuxiang
 * @LastEditTime: 2021-04-21 22:50:44
 * @FilePath: /leetcode/752.打开转盘锁.java
 */
/*
 * @lc app=leetcode.cn id=752 lang=java
 *
 * [752] 打开转盘锁
 */

// @lc code=start
class OpenLock {
    public String plusOne(String cur, int i) {
        char[] ch = cur.toCharArray();
        if (ch[i] == '9') {
            ch[i] = '0';
        } else {
            ch[i] += 1;
        }
        return new String(ch);
    }

    public String minusOne(String cur, int i) {
        char[] ch = cur.toCharArray();
        if (ch[i] == '0') {
            ch[i] = '9';
        } else {
            ch[i] -= 1;
        }
        return new String(ch);
    }

    public int openLock(String[] deadends, String target) {

        HashSet<String> deads = new HashSet<String>();
        for (String dead : deadends) {
            deads.add(dead);
        }
        
        Queue<String> q = new LinkedList<String>();
        q.offer("0000");

        HashSet<String> visited = new HashSet<String>();
        visited.add("0000");

        int step = 0;

        while(!q.isEmpty()) {
            int sz = q.size();
            for (int i=0; i<sz; i++) {
                String cur = q.poll();
                if (deads.contains(cur)){
                    continue;
                }
                if (cur.equals(target)) {
                    return step;
                }
                for (int j=0; j<4; j++) {
                    String up = plusOne(cur, j);
                    if (visited.contains(up)) continue;
                    q.offer(up);
                    visited.add(up);
                }
                for (int j=0; j<4; j++) {
                    String down = minusOne(cur, j);
                    if (visited.contains(down)) continue;
                    q.offer(down);
                    visited.add(down);

                }
            }
            step += 1;
        }

        return -1;
        
    }
}
// @lc code=end

