#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-13 08:44:47
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-13 08:47:49
FilePath: /leetcode/剑指 Offer 25. 合并两个排序的链表.py
Description: 
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next
