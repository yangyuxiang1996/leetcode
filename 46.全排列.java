import java.util.LinkedList;
import java.util.List;

/*
 * @Description: 
 * @Author: yangyuxiang
 * @Date: 2021-04-21 07:17:16
 * @LastEditors: yangyuxiang
 * @LastEditTime: 2021-04-21 07:42:11
 * @FilePath: /leetcode/46.全排列.java
 */
/*
 * @lc app=leetcode.cn id=46 lang=java
 *
 * [46] 全排列
 */

// @lc code=start
class Solution {
    
    List<List<Integer>> paths = new LinkedList<>();
    
    public List<List<Integer>> permute(int[] nums) {
        
        LinkedList<Integer> path = new LinkedList<>();
        backtrace(nums, path);
        return paths;

    }
    
    public void backtrace(int[] nums, LinkedList<Integer> path) {
        if(nums.length == path.size()) {
            paths.add(new LinkedList(path));
            return;
        }
        for (int num : nums) {
            if (path.contains(num)) {
                continue;
            }
            path.add(num);
            backtrace(nums, path);
            path.removeLast();

        }
        
    }
}
// @lc code=end

