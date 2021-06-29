#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-11 10:07:35
LastEditors: yangyuxiang
LastEditTime: 2021-05-11 11:26:08
FilePath: /leetcode/234.回文链表.py
'''
#
# @lc app=leetcode.cn id=234 lang=python
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy
class Solution(object):
    def reverse(self, root):
        if not root or not root.next:
            return root

        re = None
        # cur = copy.deepcopy(root)
        cur = root
        while cur:
            tmp = cur
            cur = cur.next
            tmp.next = re
            re = tmp

        return re
        
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True 

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        if fast:
            slow = slow.next

        left = head
        right = self.reverse(slow)

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
        
        # re = self.reverse(head)
        # while head and re and head.val == re.val:
        #     head = head.next
        #     re = re.next
        # if head or re:
        #     return False
        # return True

    def isPalindrome1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next

        left = 0
        right = len(tmp)-1
        while left <= right:
            if tmp[left] != tmp[right]:
                return False
            left += 1
            right -=1

        return True
        
            



            
        
        
# @lc code=end

