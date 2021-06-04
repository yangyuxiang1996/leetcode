#
# @lc app=leetcode.cn id=112 lang=python
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum1(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        递归，如果需要搜索整颗二叉树，那么递归函数就不要返回值，
        如果要搜索其中一条符合条件的路径，递归函数就需要返回值，
        因为遇到符合条件的路径了就要及时返回。
        """
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        left = self.hasPathSum(root.left, targetSum-root.val)
        right = self.hasPathSum(root.right, targetSum-root.val)
        return left or right

    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        递归，如果需要搜索整颗二叉树，那么递归函数就不要返回值，
        如果要搜索其中一条符合条件的路径，递归函数就需要返回值，
        因为遇到符合条件的路径了就要及时返回。
        """
        if not root:
            return False
        
        def traverse(root, count):
            if not root.left and not root.right:
                return count == 0
            if root.left:
                if traverse(root.left, count-root.left.val):
                    return True
            if root.right:
                if traverse(root.right, count-root.right.val):
                    return True
            return False

        return traverse(root, targetSum-root.val)

    def hasPathSum2(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        层次遍历
        """
        if not root:
            return False
        stack = []
        stack.append((root, root.val))

        while stack:
            n = len(stack)
            for i in range(n):
                cur = stack.pop(0)
                node, tmp = cur
                if not node.left and not node.right:
                    if tmp == targetSum:
                        return True  
                if node.left:
                    stack.append((node.left, tmp+node.left.val))
                if node.right:
                    stack.append((node.right, tmp+node.right.val))
        return False


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(Solution().hasPathSum(root, 2))
# @lc code=end

