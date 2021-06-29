#
# @lc app=leetcode.cn id=106 lang=python
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        root_v = postorder.pop()
        root = TreeNode(root_v)
        root_index = inorder.index(root_v)
        # 注意这里中序遍历的数组和后序遍历的数组大小一定是相等的
        left_inorder, right_inorder = inorder[:root_index], inorder[root_index+1:]
        left_postorder, right_postorder = postorder[:len(left_inorder)], postorder[len(left_inorder):]
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
            
        return root

    def buildTree1(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        root_v = postorder.pop()
        root = TreeNode(root_v)
        if root_v in inorder:
            root_index = inorder.index(root_v)
            left = inorder[:root_index]
            right = inorder[root_index + 1:]
            root.right = self.buildTree(right, postorder)
            root.left = self.buildTree(left, postorder)
            
        return root


if __name__ == '__main__':
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    root = Solution().buildTree(inorder, postorder)
    stack = [root]
    res = []
    while stack:
        n = len(stack)
        for i in range(n):
            cur = stack.pop(0)
            res.append(str(cur.val) if cur else 'null')
            if cur:
                stack.append(cur.left)
                stack.append(cur.right)
    print(res)


# @lc code=end

