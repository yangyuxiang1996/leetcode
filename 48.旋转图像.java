/*
 * @lc app=leetcode.cn id=48 lang=java
 *
 * [48] 旋转图像
 */

// @lc code=start
class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        // 先以左上-右下对角线进行翻转
        for (int i = 0; i < n-1; i++) {
            for (int j = i+1; j < n; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }
        }
        // 再以每一行的中点左右翻转
        int mid = n / 2;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < mid; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[i][n-1-j];
                matrix[i][n-1-j] = tmp;
            }
        }
    }

    public void rotate0(int[][] matrix) {
        // 旋转前matrix[i][j]，旋转后matrix[j][n-1-i]
        int n = matrix.length;
        int[][] matrix1 = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix1[j][n-1-i] = matrix[i][j];
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = matrix1[i][j];
            }
        }
    }
}
// @lc code=end

