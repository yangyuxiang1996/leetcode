#
# @lc app=leetcode.cn id=530 lang=python
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.res = float('inf')

    def getMinimumDifference1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        第一种方法，先中序遍历得到二叉树的值的数组，
        然后计算相邻两个元素的差的最小值
        时间复杂度O(N),空间复杂度O(N)
        """
        arr = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)

        inorder(root)
        res = float("inf")
        for i in range(len(arr)-1):
            if abs(arr[i] - arr[i+1]) < res:
                res = abs(arr[i] - arr[i+1])
        return res

    def getMinimumDifference2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        第2种方法，递归，因为需要在整棵树中计算两节点之差的绝对值的最小值，所以每一次递归需要传入当前子树的上界和下界
        """
        def helper(root, lo, hi):
            if not root:
                return hi - lo
            
            left = helper(root.left, lo, root.val)
            right = helper(root.right, root.val, hi)

            return min(left, right)
        
        res = helper(root, float('-inf'), float('inf'))
        return res

    def getMinimumDifference3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        第3种方法，迭代，中序遍历，直接保存最小的差值
        """
        stack = []
        cur = root
        pre = None
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            if pre:
                self.res = min(self.res, abs(cur.val-pre.val))
            pre = cur
            cur = cur.right
        return self.res





# @lc code=end
