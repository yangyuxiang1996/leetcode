#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-29 23:39:09
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-30 00:02:38
FilePath: /leetcode/剑指 Offer II 021. 删除链表的倒数第 n 个结点.py
Description: 
给定一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def removeNthFromEnd0(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        new_head = self.reverse(head)
        cur = new_head
        dummy = pre = ListNode(0)
        pre.next = cur
        for i in range(n-1):
            pre = pre.next
            cur = cur.next
        pre.next = cur.next

        res = self.reverse(dummy.next)
        return res   


    def removeNthFromEnd1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """  
        if not head:
            return None

        length = 0 
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        del_idx = length - n
        dummy = pre = ListNode(0)
        pre.next = head
        cur = head
        i = 0
        while i < del_idx:
            pre = pre.next
            cur = cur.next
            i += 1
        pre.next = cur.next
        return dummy.next



    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """  
        # 双指针，快指针先走n步
        if not head:
            return None
        
        slow = fast = head
        for i in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        else:
            while fast and fast.next:
                fast = fast.next
                slow = slow.next
            slow.next = slow.next.next
            return head
        


