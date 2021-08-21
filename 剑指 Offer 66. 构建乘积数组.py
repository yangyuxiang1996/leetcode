#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-21 17:03:31
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-21 17:15:39
FilePath: /leetcode/剑指 Offer 66. 构建乘积数组.py
Description: 
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。
'''
class Solution(object):
    def constructArr0(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        # 生成两个数组，分别保存当前元素左边的乘积和右边的乘积
        if not a:
            return []
        n = len(a) 
        left, right = [1] * n, [1] * n
        for i in range(1, n):
            left[i] = left[i-1] * a[i-1]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * a[i+1]
        res = [0] * n
        for i in range(n):
            res[i] = left[i] * right[i]

        return res

    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        # 直接在output数组上计算乘积
        if not a:
            return []
        n = len(a) 
        ans = [1] * n
        for i in range(1, n):
            ans[i] = ans[i-1] * a[i-1]
        tmp = a[n-1]
        for i in range(n-2, -1, -1):
            ans[i] = ans[i] * tmp
            tmp *= a[i]
        return ans
            
        


