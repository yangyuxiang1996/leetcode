#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-14 08:23:28
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-14 09:01:42
FilePath: /leetcode/剑指 Offer 22. 链表中倒数第k个节点.py
Description: 
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        self.ans = None
        def help(head, k):
            if not head:
                return 0
            n = help(head.next, k) + 1
            if n == k:
                self.ans = head 
            return n

        help(head, k)
        return self.ans
                
        
        
        
    def getKthFromEnd0(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        ans = head
        while length != k:
            ans = ans.next
            length -= 1
        
        return ans

        
        
