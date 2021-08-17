#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-16 07:45:13
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-16 10:55:17
FilePath: /leetcode/剑指 Offer 35. 复杂链表的复制.py
Description: 
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。
'''

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        拼接
        """
        if not head: return 
        cur = head
        # 1. 复制各节点，并构建拼接链表
        while cur:
            cur_new = Node(cur.val)
            cur_new.next = cur.next
            cur.next = cur_new
            cur = cur_new.next
        # 2. 构建各新节点的 random 指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 3. 拆分两链表
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None # 单独处理原链表尾节点
        return res      # 返回新链表头节点

    
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        使用哈希表
        """
        if not head:
            return None
        
        hashmap = {}
        cur = head
        while cur:
            hashmap[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            hashmap[cur].next = hashmap.get(cur.next)
            hashmap[cur].random = hashmap.get(cur.random)
            cur = cur.next
        return hashmap[head]
        

        
    