import java.util.Stack;

/*
 * @lc app=leetcode.cn id=617 lang=java
 *
 * [617] 合并二叉树
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
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        if (root1 == null && root2 == null) {
            return null;
        }
        if (root1 == null) return root2;
        if (root2 == null) return root1;

        Stack<TreeNode> stack = new Stack<>();
        stack.push(root1);
        stack.push(root2);

        while (!stack.isEmpty()) {
            TreeNode cur2 = stack.pop();
            TreeNode cur1 = stack.pop();

            cur1.val += cur2.val;

            if (cur1.left != null && cur2.left != null){
                stack.push(cur1.left);
                stack.push(cur2.left);
            } else {
                if (cur1.left == null) {
                    cur1.left = cur2.left;
                }
            }
            if (cur1.right != null && cur2.right != null){
                stack.push(cur1.right);
                stack.push(cur2.right);
            } else {
                if (cur1.right == null) {
                    cur1.right = cur2.right;
                }
            }
        }
        return root1;

    }
}
// @lc code=end

