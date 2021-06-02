#
# @lc app=leetcode.cn id=572 lang=python
#
# [572] 另一个树的子树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, left, right):
        if not left and not right:
            return True
        
        if not left or not right:
            return False

        if left.val != right.val:
            return False

        return self.isSameTree(left.left, right.left) and \
            self.isSameTree(left.right, right.right)

    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not root and not subRoot:
            return True
        if not root:
            return False
        if not subRoot:
            return True

        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or \
                self.isSubtree(root.right, subRoot)


# @lc code=end
