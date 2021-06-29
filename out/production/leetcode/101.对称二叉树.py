#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        :层序遍历
        """
        if not root:
            return True
        stack = []

        stack.append(root)
        while stack:
            n = len(stack)
            tmp = []
            for i in range(n):
                cur = stack.pop(0)
                tmp.append(str(cur.val) if cur else '')
                if cur:
                    stack.append(cur.left)
                    stack.append(cur.right)


            left, right = 0, len(tmp)-1
            while left <= right:
                if tmp[left] != tmp[right]:
                    return False
                left += 1
                right -= 1
        return True

    def isSymmetric2(self, root):
        # 递归
        if not root:
            return True

        def compare(left, right):
            if not left and not right:
                return True
            elif left and not right:
                return False
            elif not left and right:
                return False
            elif left.val != right.val:
                return False

            outside = compare(left.left, right.right)  
            inside = compare(left.right, right.left)
            return outside and inside

        return compare(root.left, root.right)

    def isSymmetric(self, root):
        # 双端队列
        if not root:
            return True
        
        import collections
        stack = collections.deque()
        stack.appendleft(root.left)
        stack.append(root.right)
        while stack:
            left = stack.popleft()
            right = stack.pop()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            stack.appendleft(left.right)
            stack.appendleft(left.left)
            stack.append(right.left)
            stack.append(right.right)
        return True

        
# @lc code=end
