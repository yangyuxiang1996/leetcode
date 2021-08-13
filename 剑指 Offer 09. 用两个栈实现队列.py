#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-10 23:06:02
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-10 23:16:42
FilePath: /leetcode/剑指 Offer 09. 用两个栈实现队列.py
Description: 
栈：后进先出
队列：先进先出
'''
class CQueue(object):

    def __init__(self):
        self.stack1 = [] # 负责插入
        self.stack2 = [] # 负责删除

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack1.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if not self.stack2:  # 如果空了，从stack1中获取数据
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return -1
        else:
            return self.stack2.pop()
        



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()