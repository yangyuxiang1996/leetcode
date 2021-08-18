#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-18 10:52:16
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-18 11:34:43
FilePath: /leetcode/剑指 Offer 33. 二叉搜索树的后序遍历序列.py
Description: 
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
'''
class Solution(object):
    def verifyPostorder0(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        if not postorder:
            return True
        
        def helper(postorder):
            if not postorder:
                return True
            root_val = postorder.pop()
            left, right = 0, len(postorder)-1
            while left < right and postorder[right] > root_val:
                right -= 1
            while left < right and postorder[left] < root_val:
                left += 1
            if left < right:
                return False
            left_postorder = postorder[:left]
            right_postorder = postorder[right+1:]
            return helper(left_postorder) and helper(right_postorder)

        return helper(postorder)

    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        stack = []
        root = float("inf")
        for i in range(len(postorder)-1, -1, -1):
            if postorder[i] > root:
                return False
            while stack and postorder[i] < stack[-1]:
                root = stack.pop()
            stack.append(postorder[i])
        return True
        


if __name__ == '__main__':
    postorder = [1,6,3,2,5]
    print(Solution().verifyPostorder(postorder))


