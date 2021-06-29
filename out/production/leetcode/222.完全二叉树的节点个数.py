#
# @lc app=leetcode.cn id=222 lang=python
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_depth = right_depth = 0
        left, right = root.left, root.right
        while left:
            left_depth += 1
            left = left.left
        while right:
            right_depth += 1
            right = right.left  # 完全二叉树的节点最后一定是在左边
        if left_depth == right_depth: # 说明左子树是满二叉树
            return 2 ** left_depth - 1 + 1 + self.countNodes(root.right)
        else: #说明右子树是满二叉树
            return 2 ** right_depth + self.countNodes(root.left)
        
    def countNodes2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        lc = rc = root
        ll = rr = 0
        while lc:
            lc = lc.left
            ll += 1
        
        while rc:
            rc = rc.right
            rr += 1
        
        if ll == rr: # 如果左右子树高度相同，说明是一个满二叉树，直接返回节点个数，否则递归计算
            return 2 ** ll - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        

    def countNodes1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
# @lc code=end

