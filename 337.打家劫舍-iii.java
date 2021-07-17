import java.util.HashMap;
import java.util.Map;

/*
 * @lc app=leetcode.cn id=337 lang=java
 *
 * [337] 打家劫舍 III
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
    Map<TreeNode, Integer> memo = new HashMap<TreeNode, Integer>();
    
    public int rob(TreeNode root) {
        return helper(root);
    }
    
    public int helper(TreeNode root) {
        if (root == null){
            return 0;
        }
        if (memo.containsKey(root)){
            return memo.get(root);
        }

        int do_val = root.val;
        if (root.left != null) {
            do_val += helper(root.left.left) + helper(root.left.right);
        }
        if (root.right != null) {
            do_val += helper(root.right.left) + helper(root.right.right);
        }

        int not_do_val = 0;
        not_do_val += helper(root.left) + helper(root.right);
        int res = Math.max(do_val, not_do_val);
        memo.put(root, res);

        return res;
    }
}
// @lc code=end

