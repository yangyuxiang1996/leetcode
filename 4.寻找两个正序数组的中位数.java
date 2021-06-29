/*
 * @lc app=leetcode.cn id=4 lang=java
 *
 * [4] 寻找两个正序数组的中位数
 */

// @lc code=start
class FindMedianSortedArrays {
    
    public static void main(String[] args) {
        int[] nums1 = {1,3};
        int[] nums2 = {2};

        double res = new FindMedianSortedArrays().findMedianSortedArrays(nums1, nums2);
        System.out.println(res);
    }

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) {
            // 保持短数组为nums1
            int[] tmp = nums1;
            nums1 = nums2;
            nums2 = tmp;
        }
        int m = nums1.length;
        int n = nums2.length;

        int l_size = (m + n + 1) / 2;  // 维持左边的两个数组的元素个数之和与右边相等或者多一个
        int left = 0;
        int right = m-1;
        while (left <= right) {
            int i = left + (right - left) / 2;  //这里不会向上取整，所以i不会等于m
            int j = l_size - i;
            if (nums1[i] < nums2[j-1]) {
                // 下一轮搜索区间[i+1, right]
                left = i + 1;
            } else {
                // 下一轮搜索区间[left, i]
                right = i - 1;
            }
        }
        int i = left;
        int j = l_size - i;
        int nums1LeftMax = i == 0 ? Integer.MIN_VALUE : nums1[i-1];
        int nums1RightMin = i == m ? Integer.MAX_VALUE : nums1[i];
        int nums2LeftMax = j == 0 ? Integer.MIN_VALUE : nums2[j-1];
        int nums2RightMin = j == n ? Integer.MAX_VALUE : nums2[j];

        if ((m+n) % 2 == 1) {
            return Math.max(nums1LeftMax, nums2LeftMax);
        } else {
            return (Math.max(nums1LeftMax, nums2LeftMax) + Math.min(nums1RightMin, nums2RightMin)) / 2.;
        }
    }
}
// @lc code=end

