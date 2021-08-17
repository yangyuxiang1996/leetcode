#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-17 22:34:09
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-17 22:57:50
FilePath: /leetcode/剑指 Offer 31. 栈的压入、弹出序列.py
Description: 
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。
'''
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        # tmp = []
        # for i in range(len(pushed)):
        #     if pushed[i] == popped[0]:
        #         popped.pop(0)
        #         while tmp and tmp[-1] == popped[0]:
        #             tmp.pop()
        #             popped.pop(0)
        #         if popped == []:
        #             return True
        #     else:
        #         tmp.append(pushed[i])
        # return popped == []
        stack, i = [], 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return stack == []
                


if __name__ == '__main__':
    pushed = [1,2,3,4,5]
    popped = [4,3,5,1,2]
    print(Solution().validateStackSequences(pushed, popped))
                
