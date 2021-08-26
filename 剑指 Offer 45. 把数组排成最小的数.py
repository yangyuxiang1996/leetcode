#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-23 22:14:21
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-23 22:45:23
FilePath: /leetcode/剑指 Offer 45. 把数组排成最小的数.py
Description:
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
输入: [10,2]
输出: "102"
输入: [3,30,34,5,9]
输出: "3033459"
'''
class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # 快速排序
        def quickSort(strs, left, right):
            if left >= right:
                return
            
            tmp = strs[left]
            i, j = left, right
            while i < j:
                while i < j and tmp + strs[j] <= strs[j] + tmp:  # 当tmp应该排在右边，strs[j]应该排在左边，退出循环
                    j -= 1
                strs[i] = strs[j]
                while i < j and tmp + strs[i] >= strs[i] + tmp:
                    i += 1
                strs[j] = strs[i]
            strs[i] = tmp

            quickSort(strs, left, i-1)
            quickSort(strs, i+1, right)

        strs = [str(num) for num in nums]
        quickSort(strs, 0, len(strs)-1)
        return "".join(strs)
            


