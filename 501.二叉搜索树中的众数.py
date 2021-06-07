#
# @lc app=leetcode.cn id=501 lang=python
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findMode1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        方法一：使用map记录每一个值出现的次数，最后按照value排序返回value最大的
        """
        count = {}
        stack = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            if cur.val not in count:
                count[cur.val] = 1
            else:
                count[cur.val] += 1
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        max_v = max(count.values())
        res = []
        for k, v in count.items():
            if v == max_v:
                res.append(k)
        return res

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        方法二：递归，中序遍历，使用pre指针保存上一个节点
        """
        self.res = []
        self.pre = None
        self.max_v = 1
        self.count = 1
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            # 这里处理
            if self.pre and root.val == self.pre.val:
                self.count += 1
            else:
                self.count = 1
            self.pre = root
            # 结果放入数组
            if self.count == self.max_v:
                self.res.append(root.val)
            if self.count > self.max_v:
                self.max_v = self.count
                self.res = []
                self.res.append(root.val)

            inorder(root.right)
        
        inorder(root)
        return self.res


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.left = TreeNode(1)
    print(Solution().findMode(root))



        
# @lc code=end

