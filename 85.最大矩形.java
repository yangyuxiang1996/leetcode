/*
 * @lc app=leetcode.cn id=85 lang=java
 *
 * [85] 最大矩形
 */

// @lc code=start
class Solution {
    public int maximalRectangle(char[][] matrix) {
        if (matrix.length == 0) {
            return 0;
        }
        int[] heights = new int[matrix[0].length];
        int maxArea = 0;
        for (int row = 0; row < matrix.length; row++) {
            for (int col = 0; col < matrix[0].length; col++) {
                if (matrix[row][col] == '1') {
                    heights[col]++;
                } else {
                    heights[col] = 0;
                }
            }
            maxArea = Math.max(maxArea, largestRectangleArea(heights));
        }
        return maxArea;
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

