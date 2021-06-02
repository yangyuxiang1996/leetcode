#
# @lc app=leetcode.cn id=404 lang=python
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def helper(root, res):
            # 如何判断左叶子
            if not root:
                return 0

            # 递归
            res += helper(root.left, res)
            res += helper(root.right, res)
            if root and root.left and (not root.left.left and not root.left.right):
                res += root.left.val
            
            return res
        
        res = helper(root, 0)

        return res


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().sumOfLeftLeaves(root))


            


# @lc code=end

