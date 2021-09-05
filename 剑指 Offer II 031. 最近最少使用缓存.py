#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-31 16:14:44
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-31 17:58:31
FilePath: /leetcode/剑指 Offer II 031. 最近最少使用缓存.py
Description: 
运用所掌握的数据结构，设计和实现一个  LRU (Least Recently Used，最近最少使用) 缓存机制 。
实现 LRUCache 类：
LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
'''
# 定义双向链表节点
class Node(object):
    def __init__(self, key, val, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next

# 定义双向链表
class DoubleLinkList(object):
    """双向链表
    addLast: 往最后添加元素
    remove：移除某个节点
    removeFirst：移除开头的节点
    """
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0
    
    def addLast(self, node):
        node.pre, node.next = self.tail.pre, self.tail
        self.tail.pre.next, self.tail.pre = node, node
        self.size += 1
        
    def remove(self, node):
        node.pre.next, node.next.pre = node.next, node.pre
        self.size -= 1
    
    def removeFist(self):
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
        # 初始化hashmap，每一个元素都是双向链表的一个节点
        self.hashmap = {}
        self.linklist = DoubleLinkList()
        self.cap = capacity

    def makeRecently(self, key):
        node = self.hashmap[key]
        self.linklist.remove(node)
        self.linklist.addLast(node)


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not key in self.hashmap:
            return -1
        self.makeRecently(key)
        return self.hashmap[key].val       

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hashmap:
            # delete
            node = self.hashmap[key]
            self.linklist.remove(node)
            self.hashmap.pop(key)
            # add
            node = Node(key, value)
            self.linklist.addLast(node)
            self.hashmap[key] = node
        else:
            if self.cap == self.linklist.size:
                # remove
                node = self.linklist.removeFist()
                del_key = node.key
                self.hashmap.pop(del_key)
            # add
            node = Node(key, value)
            self.linklist.addLast(node)
            self.hashmap[key] = node
        
        return




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)