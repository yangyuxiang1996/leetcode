#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-18 10:32:36
LastEditors: yangyuxiang
LastEditTime: 2021-05-18 10:49:02
FilePath: /leetcode/341.扁平化嵌套列表迭代器.py
'''
#
# @lc app=leetcode.cn id=341 lang=python
#
# [341] 扁平化嵌套列表迭代器
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.list = nestedList
        

    def next(self):
        """
        :rtype: int
        """
        return self.list.pop(0).getInteger()

        

    def hasNext(self):
        """
        :rtype: bool
        """
        while len(self.list) != 0 and not self.list[0].isInteger(): # 结束条件，list第一个元素为int类型
            first =  self.list.pop(0).getList()
            for i in range(len(first)-1, -1, -1):
                self.list.insert(0, first[i])

        return len(self.list) != 0
                

        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

