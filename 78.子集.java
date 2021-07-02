import java.util.ArrayList;
import java.util.List;
import java.util.LinkedList;
/*
 * @lc app=leetcode.cn id=78 lang=java
 *
 * [78] 子集
 */

// @lc code=start
class Solution {
    List<List<Integer>> result = new ArrayList<>();// 存放符合条件结果的集合
    LinkedList<Integer> path = new LinkedList<>();
    public List<List<Integer>> subsets(int[] nums) {
        if (nums.length == 0) {
            result.add(new ArrayList<Integer>());
        }
        backtrace(nums, 0);
        return result;
        
    }
    
    public void backtrace(int[] nums, int start) {
        result.add(new ArrayList<>(path));
        for (int i = start; i < nums.length; i++) {
            path.add(nums[i]);
            backtrace(nums, i+1);
            path.removeLast();
        }
    }

    // public static void main(String[] args) { 
    //     int[] nums = {1,2,3};
    //     System.out.println(new Subsets().subsets(nums));
    // }
}
// @lc code=end

