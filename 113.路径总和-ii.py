#
# @lc app=leetcode.cn id=113 lang=python
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        递归
        """
        if not root:
            return []
        paths = []

        def traversal(root, count, path):
            if not root.left and not root.right:
                if count == 0:
                    paths.append(path[:])
                    return
            if root.left:
                path.append(root.left.val)
                traversal(root.left, count-root.left.val, path)
                path.pop()
            if root.right:
                path.append(root.right.val)
                traversal(root.right, count-root.right.val, path)
                path.pop()

        traversal(root, targetSum-root.val, [root.val])
        return paths


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().pathSum(root, 4))


# @lc code=end

