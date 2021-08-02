import java.util.Arrays;

/*
 * @lc app=leetcode.cn id=200 lang=java
 *
 * [200] 岛屿数量
 */

// @lc code=start
class Solution {
    public int numIslands(char[][] grid) {
        // 深度优先搜索，将相邻的岛屿置为‘0’,最终，搜索的次数就是岛屿的个数
        int m = grid.length;
        int n = grid[0].length;
        if (m == 0 || n == 0) { return 0;}
        int num_lands = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    num_lands++;
                    dfs(grid, i, j);
                }
            }
        }
        return num_lands;
    }

    int[][] directions = {{0,1}, {0,-1}, {1,0}, {-1,0}};
    public void dfs(char[][] grid, int i, int j) {
        int m = grid.length;
        int n = grid[0].length;
        
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == '0') {
            return;
        }
        grid[i][j] = '0';
        for (int[] direction: directions) {
            dfs(grid, i+direction[0], j+direction[1]);
        }


    }
}
// @lc code=end

