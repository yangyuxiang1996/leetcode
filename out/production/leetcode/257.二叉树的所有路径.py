#
# @lc app=leetcode.cn id=257 lang=python
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def binaryTreePaths1(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        DFS+stack
        """ 
        if not root:
            return []
        
        stack = []
        res = []
        stack.append([root, ''])
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.left:
                stack.append([node.left, ls+str(node.val)+'->'])
            if node.right:
                stack.append([node.right, ls+str(node.val)+'->'])
        return res


    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        回溯法
        """
        if not root:
            return []
        paths = []
        def helper(root, path):
            path.append(str(root.val))
            if not root.left and not root.right:
                paths.append("->".join(path))
                return
            
            if root.left:
                # path.append(str(root.left.val))
                helper(root.left, path)
                path.pop()
            if root.right:
                # path.append(str(root.right.val))
                helper(root.right, path)
                path.pop()
        helper(root, [])
        return paths


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    print(Solution().binaryTreePaths(root))

            
# @lc code=end

