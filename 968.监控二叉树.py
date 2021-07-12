#
# @lc app=leetcode.cn id=968 lang=python
#
# [968] 监控二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0

        def traverse(cur):
            if not cur:
                return 2 # 2表示当前节点有覆盖
            
            left = traverse(cur.left)
            right = traverse(cur.right)

            if left == 2 and right == 2:  # 左右节点都右覆盖，父节点应该无覆盖
                return 0
            if left == 0 or right == 0:  # 左右节点其中一个无覆盖，那么父节点应该有摄像头
                self.result += 1
                return 1
            if left == 1 or right == 1:  # 左右节点其中一个有摄像头，那么父节点有覆盖
                return 2
            

        if traverse(root) == 0:
            self.result += 1
        return self.result

# @lc code=end

