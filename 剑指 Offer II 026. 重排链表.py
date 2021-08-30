#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-30 20:31:22
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-30 20:49:37
FilePath: /leetcode/剑指 Offer II 026. 重排链表.py
Description: 
给定一个单链表 L 的头节点 head ，单链表 L 表示为：
 L0 → L1 → … → Ln-1 → Ln 
请将其重新排列后变为：
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reversed(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        mid = self.reversed(mid)

        pre = head
        while mid:
            tmp = pre.next
            pre.next = mid
            mid = mid.next
            pre.next.next = tmp
            pre = pre.next.next


if __name__ == '__main__':
    head = ListNode(1)
    pre = head
    for i in range(2, 5):
        pre.next = ListNode(i)
        pre = pre.next
    
    Solution().reorderList(head)

    while head:
        print(head.val)
        head = head.next
    

        



