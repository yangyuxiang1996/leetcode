import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
 * @Description: 
 * @Author: yangyuxiang
 * @Date: 2021-04-21 08:04:09
 * @LastEditors: yangyuxiang
 * @LastEditTime: 2021-04-21 08:32:13
 * @FilePath: /leetcode/51.n-皇后.java
 */
/*
 * @lc app=leetcode.cn id=51 lang=java
 *
 * [51] N 皇后
 */

// @lc code=start
class SolveNQueens {
    
    List<List<String>> result = new ArrayList<>();
    
    public List<List<String>> solveNQueens(int n) {

        char[][] board = new char[n][n];
        for (char[] row : board) {
            Arrays.fill(row, '.');
        }
        backtrace(board, 0);
        return result;

    }

    public void backtrace(char[][] board, int row) {
        if (row == board.length) {
            List<String> copy = new ArrayList<String>();
            for (char[] c : board) {
                copy.add(String.valueOf(c));
            }
            result.add(copy);
            return;
        }

        for (int col = 0; col < board.length; col++) {
            if (!isValid(board, row, col)){
                continue;
            }
            board[row][col] = 'Q';
            backtrace(board, row + 1);
            board[row][col] = '.';
        }

    }

    boolean isValid(char[][] board, int row, int col) {
        int n = board.length;
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 'Q') 
                return false;
        }
        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j] == 'Q')
                return false;
        }
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q')
                return false;
        }
        return true;
    }
}
// @lc code=end

