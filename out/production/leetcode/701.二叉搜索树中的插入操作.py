#
# @lc app=leetcode.cn id=701 lang=python
#
# [701] 二叉搜索树中的插入操作
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)

        if val > root.val:
            # right
            root.right = self.insertIntoBST(root.right, val)
        else:
            # left
            root.left = self.insertIntoBST(root.left, val)

        return root
        
# @lc code=end

