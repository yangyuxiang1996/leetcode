#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-30 20:51:05
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-30 21:03:27
FilePath: /leetcode/剑指 Offer II 027. 回文链表.py
Description: 
给定一个链表的 头节点 head ，请判断其是否为回文链表。
如果一个链表是回文，那么链表节点序列从前往后看和从后往前看是相同的。
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l = []
        while head:
            l.append(head.val)
            head = head.next
        
        left, right = 0, len(l)-1
        while left < right:
            if l[left] != l[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    print(Solution().isPalindrome(head))
