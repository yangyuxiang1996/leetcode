#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-21 17:17:32
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-21 17:31:43
FilePath: /leetcode/剑指 Offer 59 - II. 队列的最大值.py
Description: 
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1
'''
class MaxQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []  # 保存最大元素，索引从0开始，数值从大到小


    def max_value(self):
        """
        :rtype: int
        """
        if self.stack1:
            return self.stack2[0]
        else:
            return -1


    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack1.append(value)
        while self.stack2 and self.stack2[-1] < value:
            self.stack2.pop()
        self.stack2.append(value)


    def pop_front(self):
        """
        :rtype: int
        """
        if not self.stack1:
            return -1
        tmp = self.stack1.pop(0)
        if tmp == self.stack2[0]:
            self.stack2.pop(0)
        return tmp



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
