#
# @lc app=leetcode.cn id=99 lang=python
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.res = []

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)

    def recover(self, root, count, x, y):
        if not root:
            return
        
        if root.val == x or root.val == y:
            root.val = x if root.val == y else y
            count -= 1
            if count == 0:
                return
        
        self.recover(root.right, count, x, y)
        self.recover(root.left, count, x, y)

        
    def recoverTree0(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.inorder(root)
        x, y = -1, -1
        for i in range(len(self.res)-1):
            if self.res[i] > self.res[i+1]:
                y = self.res[i+1]
                if x == -1:
                    x = self.res[i]
                else:
                    break
        
        self.recover(root, 2, x, y)
        return


    def recoverTree(self, root):
        if not root:
            return
        
        x, y, pre = None, None, None
        stack = []
        
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            if pre and cur.val < pre.val:
                y = cur
                if x is None:
                    x = pre
                else:
                    break
            
            pre = cur
            cur = cur.right

        x.val, y.val = y.val, x.val
        return





if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.right = TreeNode(2)
    Solution().recoverTree(root)



# @lc code=end

