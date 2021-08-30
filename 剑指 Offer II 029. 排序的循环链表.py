#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-30 22:00:20
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-30 23:06:31
FilePath: /leetcode/剑指 Offer II 029. 排序的循环链表.py
Description: 
'''
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        
        min_val, max_val = head.val, head.val
        cur = head
        count = 0
        while cur.next != head:
            count += 1
            cur = cur.next
            min_val = min(min_val, cur.val)
            max_val = max(max_val, cur.val)
        print(min_val, max_val)
        
        if insertVal <= min_val or insertVal >= max_val:
            # 比最小值小或者比最大值大，插到最大值的后面
            cur = head
            k = 0
            while cur.val == cur.next.val or cur.next.val != min_val:
                k += 1
                cur = cur.next
                if k > count:
                    break
        else:
            # 比最小值大，比最大值小
            cur = head
            while not (cur.val <= insertVal and cur.next.val >= insertVal):
                cur = cur.next
        tmp = cur.next
        cur.next = Node(insertVal)
        cur.next.next = tmp
        return head