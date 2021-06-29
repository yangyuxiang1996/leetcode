#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-11 14:25:40
LastEditors: yangyuxiang
LastEditTime: 2021-05-11 15:13:51
FilePath: /leetcode/92.反转链表-ii.py
'''
#
# @lc app=leetcode.cn id=92 lang=python
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def __init__(self):
        self.successor = None

    def reverseN1(self, head, n):
        """
        递归计算：反转链表前n个节点
        """
        if n == 1:
            self.successor = head.next
            return head
        
        last = self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = self.successor

        return last

    def reverseN(self, head, n):
        """
        迭代计算反转链表前n个节点
        """
        if n == 1: 
            return head

        pre = None
        while n > 0:
            cur = head
            head = head.next
            cur.next = pre
            pre = cur
            n -= 1

        new = pre
        while new.next:
            new = new.next
        new.next = head

        return pre


        
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        if left == 1:
            return self.reverseN(head, right)
            
        cur = head
        for i in range(1, left-1):
            cur = cur.next
        
        cur.next = self.reverseN(cur.next, right-left+1)

        return head
        
        
if __name__ == "__main__":
    head = ListNode(1)
    cur = head
    for i in range(2, 6):
        cur.next = ListNode(i)
        cur = cur.next

    l = Solution().reverseBetween(head, 2, 4)
    while l :
        print(l.val)
        l = l.next
        
        
        
        
# @lc code=end

