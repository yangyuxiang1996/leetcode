#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-17 08:48:03
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-17 08:56:53
FilePath: /leetcode/剑指 Offer 30. 包含min函数的栈.py
Description: 
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
'''
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)
        if not self.stack2 or self.stack2[-1] >= x:
            self.stack2.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack1.pop() == self.stack2[-1]:
            self.stack2.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack1[-1]

    def min(self):
        """
        :rtype: int
        """
        return self.stack2[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
