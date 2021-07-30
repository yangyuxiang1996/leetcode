/*
 * @lc app=leetcode.cn id=79 lang=java
 *
 * [79] 单词搜索
 */

// @lc code=start
class Solution {
    public boolean exist(char[][] board, String word) {
        // 回溯
        boolean[][] visited = new boolean[board.length][board[0].length];
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (backtrace(board, word, i, j, 0, visited)) {
                    return true;
                }
            }
        }
        return false;

    }

    int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    public boolean backtrace(char[][] board, String word, int i, int j, int k, boolean[][] visited) {
        // 终止条件
        if (board[i][j] != word.charAt(k)) {
            return false;
        }
        if (k == word.length()-1) {
            return true;
        }
        visited[i][j] = true;
        // boolean result = false;
        // 遍历选择
        for (int[] d: directions) {
            int new_i = i + d[0];
            int new_j = j + d[1];
            if (new_i >= 0 && new_j >= 0 && new_i < board.length && new_j < board[0].length) {
                if (visited[new_i][new_j] == false) {
                    boolean flag = backtrace(board, word, new_i, new_j, k+1, visited);
                    if (flag) {
                        // result = true;
                        return true;
                        // break;
                    }
                }
            }
        }
        visited[i][j] = false;
        return false;

    }
}
// @lc code=end

