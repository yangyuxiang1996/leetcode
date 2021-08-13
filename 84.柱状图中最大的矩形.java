/*
 * @lc app=leetcode.cn id=84 lang=java
 *
 * [84] 柱状图中最大的矩形
 */

// @lc code=start
class Solution {
    // public static void main(String[] args) {
    //     int[] heights = new int[]{};
    // }
    public int largestRectangleArea0(int[] heights) {
        // 暴力解法，向左向右找第一个比当前元素小的值, 超时, O(n2)
        int max_area = 0;
        int n = heights.length;
        for(int i=0; i<n; i++) {
            int left=i, right=i;
            int tmp = heights[i];
            while (left >= 0 && tmp <= heights[left]) {
                left--;
            }
            while (right < n && tmp <= heights[right]) {
                right++;
            }
            max_area = Math.max(max_area, heights[i] * (right-left-1));
        }

        return max_area;
    }
    public int largestRectangleArea(int[] heights) {
        // 用两个数组先存好
        int max_area = 0;
        int n = heights.length;
        int[] left_min = new int[n];
        int[] right_min = new int[n];
        left_min[0] = -1;
        right_min[n-1] = n;

        for (int i = 1; i < n; i++) {
            int p = i - 1;
            while (p >=0 && heights[i] <= heights[p]) {
                p = left_min[p]; // 跳到小于前一个元素的第一个位置
            }
            left_min[i] = p;
        }

        for (int i = n-2; i >= 0; i--) {
            int p = i+1;
            while (p < n && heights[i] <= heights[p]) {
                p = right_min[p];
            }
            right_min[i] = p;
        }

        for (int i = 0; i < n; i++) {
            max_area = Math.max(max_area, heights[i]*(right_min[i]-left_min[i]-1));
        }

        return max_area;
    }
}
// @lc code=end

