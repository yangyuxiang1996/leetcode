#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-12 22:26:42
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-12 22:42:01
FilePath: /leetcode/剑指 Offer 06. 从尾到头打印链表.py
Description: 
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse0(self, head):
        if not head:
            return None
        
        pre = None
        while head:
            cur = head
            head = head.next
            cur.next = pre
            pre = cur
        return pre

    def reverse(self, head):
        if not head:
            return None
        
        last = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return last
    
    def reversePrint1(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        head = self.reverse(head)
        res = []
        while head:
            res.append(head.val)
            head = head.next
        
        return res

    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        res = []
        def help(head):
            if not head:
                return
            help(head.next)
            res.append(head.val)
        help(head)
        return res
            

    def reversePrint0(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        res = []
        while head:
            res.append(head.val)
            head = head.next
        
        left, right = 0, len(res)-1
        while left <= right:
            res[left], res[right] = res[right], res[left]
            left += 1
            right -= 1
        return res



