#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-23 16:57:03
LastEditors: yangyuxiang
LastEditTime: 2021-05-23 17:13:36
FilePath: /leetcode/83.删除排序链表中的重复元素.py
'''

#
# @lc app=leetcode.cn id=83 lang=python
#
# [83] 删除排序链表中的重复元素
#


# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        # slow = head
        # fast = head.next
        # while fast:
        #     if fast.val != slow.val:
        #         slow.next = fast
        #         slow = slow.next
        #     fast = fast.next

        # slow.next = None
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next

        return head


# @lc code=end
