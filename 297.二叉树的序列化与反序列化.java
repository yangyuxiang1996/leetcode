import java.util.List;
import java.util.Arrays;
import java.util.LinkedList;

/*
 * @lc app=leetcode.cn id=297 lang=java
 *
 * [297] 二叉树的序列化与反序列化
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {
    
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        // 前序遍历
        String str = encode(root, "");
        return str;
    }

    public String encode(TreeNode root, String str) {
        if (root == null) {
            str += "null,";
            return str;
        }else {
            str += String.valueOf(root.val) + ",";
            str = encode(root.left, str);
            str = encode(root.right, str);
        }
        return str;
    }
    
    public TreeNode decode(List<String> data) {
        if (data.get(0).equals("null")) {
            data.remove(0);
            return null;
        }
        TreeNode root = new TreeNode(Integer.valueOf(data.get(0)));
        data.remove(0);
        root.left = decode(data);
        root.right = decode(data);
        return root;
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] strs = data.split(",");
        List<String> dataList = new LinkedList<String>(Arrays.asList(strs));
        return decode(dataList);
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));
// @lc code=end

