#
# @lc app=leetcode.cn id=654 lang=python
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def finxMax(self, nums):
        index = 0
        max_val = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
                index = i
        return max_val, index
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        max_val, max_i = self.finxMax(nums)
        root = TreeNode(max_val)
        left_nums, right_nums = nums[:max_i], nums[max_i+1:]
        root.left = self.constructMaximumBinaryTree(left_nums)
        root.right = self.constructMaximumBinaryTree(right_nums)
        return root

# @lc code=end

