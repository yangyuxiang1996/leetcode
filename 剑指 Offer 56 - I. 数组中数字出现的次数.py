#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-18 23:17:44
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-18 23:37:30
FilePath: /leetcode/剑指 Offer 56 - I. 数组中数字出现的次数.py
Description: 
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/solution/jian-zhi-offer-56-i-shu-zu-zhong-shu-zi-tykom/
'''
class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 分组异或
        m, x, y = 1, 0, 0
        for num in nums:
            x ^= num
        # 此时的x是两个只出现一次的数字的异或
        # 从右往走找第一个异或结果为1的位，并以此分组
        while m & x == 0:
            m <<= 1
        x = 0
        for num in nums:
            if num & m:
                x ^= num
            else:
                y ^= num
        return [x ,y]
        

