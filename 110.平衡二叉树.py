#
# @lc app=leetcode.cn id=110 lang=python
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def get_depth(self, root):
        if not root:
            return 0
        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        return max(left_depth, right_depth) + 1

    def isBalanced1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        :先计算当前节点的左右子树的高度，如果高度差大于1，返回False，否则递归判断
        自顶向下，时间复杂度O(n2)，空间复杂度：O(n)
        """
        if not root:
            return True
        
        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        if abs(left_depth - right_depth) > 1:
            return False
        else: 
            return self.isBalanced(root.left) and self.isBalanced(root.right) 

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        自底向上的递归，时间复杂度O(N)，空间复杂度：O(n)
        """    
        def getDepth(root):
            if not root:
                return 0
            leftDepth = getDepth(root.left)
            if leftDepth == -1:
                return -1
            rightDepth = getDepth(root.right)
            if rightDepth == -1:
                return -1
            if abs(leftDepth - rightDepth) > 1: # 如果左右子树高度差大于1，返回-1，表示此时已经不是平衡二叉树
                return -1
            else:
                return 1 + max(leftDepth, rightDepth)  # 否则返回当前节点的最大高度
        
        return getDepth(root) != -1
        
# @lc code=end

