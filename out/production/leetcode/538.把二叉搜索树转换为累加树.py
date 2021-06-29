#
# @lc app=leetcode.cn id=538 lang=python
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        :解法：迭代+中序遍历
        """
        if not root:
            return root
        
        stack = []
        pre = None
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.right
            
            cur = stack.pop()
            if pre:
                cur.val += pre.val
            pre = cur
            cur = cur.left
        return root


        

    def convertBST1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        :解法：递归+中序遍历
        """
        if not root:
            return root
        
        self.pre = None

        def reverse_inorder(root):
            if not root:
                return
            
            reverse_inorder(root.right)
            if self.pre:
                root.val += self.pre.val
            self.pre = root
            reverse_inorder(root.left)

        reverse_inorder(root)
        return root


# @lc code=end

