import java.util.ArrayList;
import java.util.Stack;

/*
 * @lc app=leetcode.cn id=98 lang=java
 *
 * [98] 验证二叉搜索树
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
    long min = Long.MIN_VALUE;
    public boolean isValidBST(TreeNode root) {
        // 递归，中序遍历
        if (root == null) return true;
        boolean left = isValidBST(root.left);
        if (!left) return false;
        if (min >= root.val) { 
            return false;
        }
        min = root.val;
        boolean right = isValidBST(root.right);
        if (!right) return false;
        return true;
    }

    public boolean isValidBST(TreeNode node, long lower, long upper) {
        if (node == null) return true;
        if (node.val <= lower || node.val >= upper) return false;
        return isValidBST(node.left, lower, node.val) && isValidBST(node.right, node.val, upper);

    }
    public boolean isValidBST1(TreeNode root) {
        // 递归解法, 需要存储当前的上界和下界
        if (root == null) return true;
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    public boolean isValidBST2(TreeNode root) {
        // 先用中序遍历将节点的值保存成数组，然后判断数组是不是有序
        if (root == null) return true;
        inorder(root);
        for (int i = 0; i < res.size()-1; i++) {
            if (res.get(i) >= res.get(i+1)) return false;
        }
        return true;

    }
    public boolean isValidBST3(TreeNode root) {
        // 中序遍历，每一次需要保存上一个节点2
        if (root == null) return true;
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode cur = root;
        TreeNode pre = null;
        while (cur != null || !stack.isEmpty()) {
            while (cur != null) {
                stack.push(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            if (pre != null && pre.val >= cur.val) {
                return false;
            }
            pre = cur;
            cur = cur.right;
        }
        return true;

    }

    ArrayList<Integer> res = new ArrayList<Integer>();
    public void inorder(TreeNode root) {
        if (root == null) return;
        inorder(root.left);
        res.add(root.val);
        inorder(root.right); 
    }
}
// @lc code=end

