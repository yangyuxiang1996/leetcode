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
        #层次遍历
        """
        if not root:
            return 0
        stack = []
        stack.append(root)
        res = 0
        while stack:
            cur = stack.pop(0)
            if cur.left and (not cur.left.left and not cur.left.right):
                # 该节点为左节点
                res += cur.left.val
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return res

    def sumOfLeftLeaves1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        #递归解法
        """
        if not root:
            return 0

        def helper(root, res):
            # 如何判断左叶子
            if not root:
                return 0

            # 递归
            leftv = helper(root.left, res)
            rightv = helper(root.right, res)
            midv = 0
            if root and root.left and (not root.left.left and not root.left.right):
                midv = root.left.val
            
            return midv + leftv + rightv
        
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

