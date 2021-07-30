import java.util.ArrayList;
import java.util.LinkedList;

/*
 * @lc app=leetcode.cn id=114 lang=java
 *
 * [114] 二叉树展开为链表
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
    private TreeNode pre = null;

    public void flatten(TreeNode root) {
        // 递归, 自底向上
        if (root == null)
            return;
        flatten(root.right);
        flatten(root.left);
        root.right = pre;
        root.left = null;
        pre = root;
    }
    
    public void flatten0(TreeNode root) {
       // 前序遍历
       if (root == null) {
           return;
       }

       LinkedList<TreeNode> stack = new LinkedList<>();
       stack.push(root);
       TreeNode pre = null;
       while(!stack.isEmpty()) {
           TreeNode cur = stack.pop();
           if (pre != null) {
               pre.left = null;
               pre.right = cur;
           }

           if (cur.right != null) {
               stack.push(cur.right);
           }
           if (cur.left != null) {
               stack.push(cur.left);
           }
           pre = cur;
       }       
    }
}
// @lc code=end

