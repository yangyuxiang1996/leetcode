import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=621 lang=java
 *
 * [621] 任务调度器
 */

// @lc code=start
class Solution {
    public int leastInterval(char[] tasks, int n) {
        if (n == 0) { return tasks.length;}
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int max = Integer.MIN_VALUE;
        for (char task : tasks) {
            map.put(task, map.getOrDefault(task, 0)+1);
            max = Math.max(max, map.get(task));
        }
        int max_count = 0;
        for (char task : map.keySet()) {
            if (map.get(task) == max) {
                max_count++;
            }
        }
        return Math.max((max-1)*(n+1) + max_count, tasks.length);
    }
}
// @lc code=end

