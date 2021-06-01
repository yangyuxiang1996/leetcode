#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-22 08:51:28
LastEditors: yangyuxiang
LastEditTime: 2021-05-11 14:25:08
FilePath: /leetcode/206.反转链表.py
'''
#
# @lc app=leetcode.cn id=206 lang=python
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next:
            return head
        
        pre = None
        while head:
            cur = head
            head = head.next
            cur.next = pre
            pre = cur

        return pre

    def reverseList(self, head):
        """
        递归
        """
        if not head or not head.next:
            return head
        
        last = self.reverseList1(head.next)
        head.next.next = head
        head.next = None

        return last
        

            

            

        
# @lc code=end

