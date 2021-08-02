import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Random;

/*
 * @lc app=leetcode.cn id=215 lang=java
 *
 * [215] 数组中的第K个最大元素
 */

// @lc code=start
class Solution {
    public class NewComparator implements Comparator<Integer> {
        @Override
        public int compare(Integer n1, Integer n2) {
            if (n1 < n2) {
                return -1;
            } else if (n1 > n2) {
                return 1;
            } else {
                return 0;
            }
        }
    }
    public int findKthLargest0(int[] nums, int k) {
        // 维护一个堆
        // PriorityQueue实现了一个优先队列：从队首获取元素时，总是获取优先级最高的元素
        // 每次调整堆的复杂度O(logk)，整体复杂度O(nlogk)
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>(new NewComparator()); // 最小值堆 
        for (int num : nums) {
            heap.add(num); // 遍历数组，元素依次插入到堆中
            if (heap.size() > k) {  //如果堆的容量大于k，取出堆首的元素
                heap.poll();
            }
        }
        return heap.poll();  
    }
    
    public void swap(int[] nums, int a, int b) {
        int tmp = nums[a];
        nums[a] = nums[b];
        nums[b] = tmp;
    }

    public int partition(int[] nums, int pivot_index, int left, int right) {
        int pivot = nums[pivot_index];
        swap(nums, pivot_index, right);
        int store_index = left;
        for (int i = left; i <= right; i++) {
            if (nums[i] < pivot) {
                swap(nums, store_index, i);
                store_index++;
            }
        }
        swap(nums, store_index, right);
        return store_index;
    }

    public int quickSelect(int[] nums, int left, int right, int k_smallest) {
        if (left == right ){
            return nums[left];
        }
        Random random_num = new Random();
        int pivot_index = left + random_num.nextInt(right - left);
        pivot_index = partition(nums, pivot_index, left, right);
        if (k_smallest == pivot_index) {
            return nums[k_smallest];
        } else if (k_smallest < pivot_index) {
            return quickSelect(nums, left, pivot_index-1, k_smallest);
        }else {
            return quickSelect(nums, pivot_index+1, right, k_smallest);
        }
    }

    public int findKthLargest(int[] nums, int k) {
        // 快速选择，利用快速排序的思想，平均时间复杂度O(n)
        int size = nums.length;
        return quickSelect(nums, 0, size-1, size-k);
    }


}
// @lc code=end

