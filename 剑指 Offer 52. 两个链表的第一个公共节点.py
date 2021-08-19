#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-19 08:27:37
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-19 08:42:14
FilePath: /leetcode/剑指 Offer 52. 两个链表的第一个公共节点.py
Description: 
输入两个链表，找出它们的第一个公共节点。
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # p1 + k + p2 = p2 + k + p1
        cur1, cur2 = headA, headB
        while cur1 != cur2:
            if cur1:
                cur1 = cur1.next
            else:
                cur1 = headB
            if cur2:
                cur2 = cur2.next
            else:
                cur2 = headA
        return cur1