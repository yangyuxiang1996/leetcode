import java.util.Deque;
import java.util.LinkedList;


/*
 * @lc app=leetcode.cn id=239 lang=java
 *
 * [239] 滑动窗口最大值
 */

// @lc code=start
class MaxSlidingWindow {
    public int[] maxSlidingWindow(int[] nums, int k) {
        // 单调递减队列
        if (nums.length <= 1) {
            return nums;
        }
        Deque<Integer> deque = new LinkedList<>();  // 存放索引
        int[] res = new int[nums.length - k + 1];
        int num = 0;
        for (int i = 0; i < k; i++) {
            while (!deque.isEmpty() && nums[deque.getLast()] < nums[i]) {
                deque.removeLast();
            }
            deque.addLast(i);
        }
        res[num++] = nums[deque.peek()];
        for (int i=k; i<nums.length; i++){
            if (i - k >= deque.peek()) {  // 判断单调队列的首元素是否需要出列
                deque.removeFirst();
            }
            while (!deque.isEmpty() && nums[deque.getLast()] < nums[i]) {
                deque.removeLast();
            }
            deque.addLast(i);
            res[num++] = nums[deque.peek()];
        }
        return res;
    }

    public static void main(String[] args) {
        int[] nums = {1,3,-1,-3,5,3,6,7};
        int k = 3;
        System.out.println(new MaxSlidingWindow().maxSlidingWindow(nums, k));
    }
}
// @lc code=end

