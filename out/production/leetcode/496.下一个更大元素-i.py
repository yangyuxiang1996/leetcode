#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-10 10:43:34
LastEditors: yangyuxiang
LastEditTime: 2021-05-10 11:33:12
FilePath: /leetcode/496.下一个更大元素-i.py
'''
#
# @lc app=leetcode.cn id=496 lang=python
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution(object):
    def nextGreaterElement1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for n in nums1:
            i = nums2.index(n)
            while i+1 < len(nums2) and nums2[i+1] < n:
                i += 1
            if i+1 == len(nums2):
                res.append(-1)
            else:
                res.append(nums2[i+1])
        return res

    def nextGreaterElement(self, nums1, nums2):
        """
        利用哈希表和单调栈解决
        """
        len1 = len(nums1)
        len2 = len(nums2)
        
        m = {}
        stack = []
        for i in range(0, len2):
            while stack != [] and stack[-1] < nums2[i]:
                p = stack.pop()
                m[p] = nums2[i]
            stack.append(nums2[i])
        
        res = []
        for i in range(0, len1):
            if nums1[i] in m:
                res.append(m[nums1[i]])
            else:
                res.append(-1)

        return res
            
         
# @lc code=end

