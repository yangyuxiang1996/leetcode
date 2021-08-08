/*
 * @lc app=leetcode.cn id=437 lang=java
 *
 * [437] 路径总和 III
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int res = 0;
    public int pathSum(TreeNode root, int targetSum) {
        if (root == null) return 0;
        helper(root, targetSum, targetSum);
        pathSum(root.left, targetSum);
        pathSum(root.right, targetSum);
        return res;
    }
    public void helper(TreeNode root, int targetSum, int tmpSum) {
        // dfs
        if (root == null) {
            return;
        }
        if (tmpSum == root.val) {
            res++;
        }
        helper(root.left, targetSum, tmpSum-root.val);
        helper(root.right, targetSum, tmpSum-root.val);

    }
}
// @lc code=end

