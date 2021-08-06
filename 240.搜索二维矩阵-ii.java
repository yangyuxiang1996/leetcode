/*
 * @lc app=leetcode.cn id=240 lang=java
 *
 * [240] 搜索二维矩阵 II
 */

// @lc code=start
class Solution {
    public boolean binarySearch(int[][] matrix, int target, int row) {
        int left = 0;
        int right = matrix[0].length-1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (matrix[row][mid] == target) {
                return true;
            }else if (matrix[row][mid] > target) {
                right = mid - 1;
            }else {
                left = mid + 1;
            }
        }
        return false;
    }

    public boolean searchMatrix(int[][] matrix, int target) {
        // 二分
        // 时间复杂度O(mlogn)
        int m = matrix.length, n = matrix[0].length;
        if(matrix == null || m < 1 || n < 1) {
            return false;
        }
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] <= target && matrix[i][n-1] >= target) {
                if (binarySearch(matrix, target, i) == true) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean searchMatrix1(int[][] matrix, int target) {
        // 时间复杂度O(m+n)
        if(matrix == null || matrix.length < 1 || matrix[0].length <1) {
            return false;
        }
        int col = matrix[0].length-1; // 从右上角开始
        int row = 0;
        while(col >= 0 && row <= matrix.length-1) {
            if(target == matrix[row][col]) {
                return true;
            } else if(target < matrix[row][col]) {
                col--;
            } else if(target > matrix[row][col]) {
                row++;
            }
        }
        return false;
    }

    public boolean searchMatrix0(int[][] matrix, int target) {
        // 暴力解法, 时间复杂度O(mn)
        int m = matrix.length;
        int n = matrix[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == target) {
                    return true;
                }
            }
        }
        return false;
    }
}
// @lc code=end

