#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-30 08:42:32
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-30 08:51:26
FilePath: /leetcode/剑指 Offer II 025. 链表中的两数相加.py
Description: 
给定两个 非空链表 l1和 l2 来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
可以假设除了数字 0 之外，这两个数字都不会以零开头。
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n_l1, n_l2 = self.reverseList(l1), self.reverseList(l2)
        carry = 0
        dummy = cur = ListNode(0)
        while n_l1 or n_l2:
            if not n_l1:
                val1 = 0
            else:
                val1 = n_l1.val
            if not n_l2:
                val2 = 0
            else:
                val2 = n_l2.val
            val = val1 + val2 + carry
            if val >= 10:
                carry = 1
            else:
                carry = 0
            val = val % 10
            cur.next = ListNode(val)
            cur = cur.next
            if n_l1:
                n_l1 = n_l1.next
            if n_l2:
                n_l2 = n_l2.next

        if carry:
            cur.next = ListNode(1)

        res = self.reverseList(dummy.next)
        return res
        

        
        



