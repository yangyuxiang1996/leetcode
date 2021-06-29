#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-05 21:43:06
LastEditors: yangyuxiang
LastEditTime: 2021-05-05 22:17:32
FilePath: /leetcode/146.lru-缓存机制.py
'''
#
# @lc app=leetcode.cn id=146 lang=python
#
# [146] LRU 缓存机制
#

# @lc code=start
class Node(object):
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class DoubleList(object):
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    def addLast(self, node):
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre.next = node
        self.tail.pre = node
        self.size += 1
   
    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        self.size -= 1
        
    def removeFirst(self):
        if self.head.next == self.tail:
            return None
        first = self.head.next
        self.remove(first)
        return first

            

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = DoubleList()
        self.m = {}

    def makeRecently(self, key):
        nk = self.m[key]
        self.cache.remove(nk)
        self.cache.addLast(nk)

    def addRecently(self, key, value):
        node = Node(key, value)
        self.cache.addLast(node)
        self.m[key] = node

    def deleteKey(self, key):
        node = self.m[key]
        self.cache.remove(node)
        self.m.pop(key)

    def removeLeastKey(self):
        node = self.cache.removeFirst()
        key = node.key
        self.m.pop(key)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not key in self.m:
            return -1
        self.makeRecently(key)
        return self.m[key].value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.m:
            self.deleteKey(key)
            self.addRecently(key, value)
            return
        else:
            if self.cap == self.cache.size:
                self.removeLeastKey()
            self.addRecently(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

