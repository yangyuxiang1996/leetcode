import java.util.LinkedList;

/*
 * @lc app=leetcode.cn id=222 lang=java
 *
 * [222] 完全二叉树的节点个数
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
    // public class TreeNode {
    //     int val;
    //     TreeNode left;
    //     TreeNode right;
    //     TreeNode() {};
    //     TreeNode(int val) { this.val = val; }
    //     TreeNode(int val, TreeNode left, TreeNode right) {
    //         this.val = val;
    //         this.left = left;
    //         this.right = right;
    //     }
    // }

    public int countNodes(TreeNode root) {
        if (root == null) {
            return 0;
        }
        LinkedList<TreeNode> nodes = new LinkedList<>();
        nodes.add(root);
        int res = 0;
        while (!nodes.isEmpty()) {
            int nz = nodes.size();
            for (int i = 0; i <nz; i++) {
                TreeNode node = nodes.pop();
                res++;
                if (node.left != null) {
                    nodes.add(node.left);
                }
                if (node.right != null) {
                    nodes.add(node.right);
                }

            }
        }
        return res;


        

    }
}
// @lc code=end

