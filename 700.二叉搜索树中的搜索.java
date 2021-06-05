import java.util.Stack;

/*
 * @lc app=leetcode.cn id=700 lang=java
 *
 * [700] 二叉搜索树中的搜索
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
class Search {
    public TreeNode searchBST1(TreeNode root, int val) {
        if (root == null) return null;
        if (root.val == val) return root;
        if (root.val < val) {
            return searchBST(root.right, val);
        } else {
            return searchBST(root.left, val);
        }
    }

    public TreeNode searchBST0(TreeNode root, int val) {
        if (root == null) return null;
        Stack<TreeNode> stack = new Stack<TreeNode>();
        stack.push(root);
        while (!stack.isEmpty()){
            TreeNode cur = stack.pop();
            if (cur.val == val) return cur;
            if (cur.val > val) { 
                if (cur.left != null)  {
                    stack.push(cur.left);
                }
            } else {
                if (cur.right != null) {
                    stack.push(cur.right);
                }
            }

        }
        return null;

    }

    public TreeNode searchBST(TreeNode root, int val) {
        while (root != null) {
            if (root.val == val) return root;
            if (root.val > val) { 
                root = root.left;
            } else {
                root = root.right;
            }
        }
        return null;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        root.right = new TreeNode(7);
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);
        System.out.println(new Search().searchBST(root, 5));

    }
}
// @lc code=end

