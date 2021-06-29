#
# @lc app=leetcode.cn id=100 lang=python
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        迭代
        """        
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        stack = []
        stack.append(p)
        stack.append(q)
        while stack:
            cur_p = stack.pop(0)
            cur_q = stack.pop(0)
            if cur_p.val != cur_q.val:
                return False
            if cur_p.left and cur_q.left:
                stack.append(cur_p.left)
                stack.append(cur_q.left)
            elif cur_p.left or cur_q.left:
                return False
            if cur_p.right and cur_q.right:
                stack.append(cur_p.right)
                stack.append(cur_q.right)
            elif cur_p.right or cur_q.right:
                return False
        return True
            



    def isSameTree1(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right


if __name__ == '__main__':
    p = TreeNode(1)
    q = TreeNode(1)
    q.right = TreeNode(2)
    print(Solution().isSameTree(p, q))
# @lc code=end

