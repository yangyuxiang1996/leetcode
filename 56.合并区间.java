import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;

/*
 * @lc app=leetcode.cn id=56 lang=java
 *
 * [56] 合并区间
 */

// @lc code=start
class Solution {
    public int[][] merge(int[][] intervals) {
        if(intervals.length < 2){
            return intervals;
        }

        Arrays.sort(intervals, (o1, o2) -> Integer.compare(o1[0], o2[0]));  // 按照左边界从小到大排序
        List<int[]> res = new LinkedList<>();
        int start = intervals[0][0];  // 最小的start
        for (int i = 1; i < intervals.length; i++){
            if (intervals[i][0] > intervals[i-1][1]){ // 无重叠
                res.add(new int[]{start, intervals[i-1][1]});
                start = intervals[i][0];  // 更新当前的start
            }else{ // 有重叠，更新右边界
                intervals[i][1] = Math.max(intervals[i-1][1], intervals[i][1]);
            }
        }
        res.add(new int[]{start, intervals[intervals.length-1][1]});

        return res.toArray(new int[res.size()][]);

    }
}
// @lc code=end

