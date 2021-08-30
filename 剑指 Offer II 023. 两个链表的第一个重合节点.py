#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-30 08:19:56
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-30 08:38:07
FilePath: /leetcode/剑指 Offer II 023. 两个链表的第一个重合节点.py
Description: 
给定两个单链表的头节点 headA 和 headB ，请找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
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
        p, q = headA, headB
        while p != q:
            if p:
                p = p.next
            else:
                p = headB
            if q:
                q = q.next
            else:
                q = headA
        return p

