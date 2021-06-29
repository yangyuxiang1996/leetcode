#
# @lc app=leetcode.cn id=513 lang=python
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findBottomLeftValue1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        层次遍历
        """
        if not root:
            return 0
        stack =[]
        stack.append(root)
        left = None
        while stack:
            nz = len(stack)
            for i in range(nz):
                cur = stack.pop(0)
                if i == 0:
                    left = cur.val
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
        return left

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        递归
        """
        res = {}
        def helper(root, depth):
            if not root:
                return
            helper(root.left, depth+1)
            if not root.left and not root.right:
                if depth+1 not in res:
                    res[depth+1] = root.val
                return
            helper(root.right, depth+1)

        helper(root, 0)
        max_depth = max(res.keys())
        
        return res[max_depth]

    def findBottomLeftValue2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        递归
        """
        self.maxDepth = float('-inf')
        self.res = float('-inf')
        def helper(root, depth):
            if not root.left and not root.right:
                if depth > self.maxDepth:
                    self.maxDepth = depth
                    self.res = root.val
            if root.left:
                helper(root.left, depth+1)
            if root.right:
                helper(root.right, depth+1)

        helper(root, 0)
        return self.res

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(Solution().findBottomLeftValue(root))

    
# @lc code=end

