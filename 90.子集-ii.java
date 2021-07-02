import java.util.*;
/*
 * @lc app=leetcode.cn id=90 lang=java
 *
 * [90] 子集 II
 */

// @lc code=start
class SubsetsWithDup {
    List<List<Integer>> result= new ArrayList<>();
    LinkedList<Integer> path = new LinkedList<>();
    
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        if(nums.length == 0){
            result.add(new ArrayList<>());
            return result;
        }
        Boolean[] visited = new Boolean[nums.length];
        for (int i=0; i<nums.length; i++) {
            visited[i]=false;
        }

        Arrays.sort(nums);
        backtrace(nums, 0, visited);
        return result;

    }
    
    public void backtrace(int[] nums, int start, Boolean[] visited) {
        result.add(new ArrayList<>(path));

        for (int i=start; i<nums.length; i++) {
            if (i>start && nums[i] == nums[i-1]){
                continue;
            }
            path.add(nums[i]);
            visited[i] = true;
            backtrace(nums, i+1, visited);
            path.removeLast();
            visited[i] = false;
        }
    }

    public static void main(String[] args) {
        int[] nums = {1,2,2};
        System.out.println(new SubsetsWithDup().subsetsWithDup(nums));
    }
}
// @lc code=end

