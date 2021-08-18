#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-18 23:40:30
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-19 00:00:58
FilePath: /leetcode/剑指 Offer 56 - II. 数组中数字出现的次数 II.py
Description: 
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        is_neg = False
        for i in range(32):
            counter = 0
            for num in nums:  # 记录当前位出现1的次数
                if (num >> i) & 1:
                    counter += 1
            
            if counter % 3 == 1: # 说明只出现一次的数字在该位为1
                ans += pow(2, i)
                if i == 31:
                    is_neg = True
        return ans if not is_neg else ans - pow(2, 32)

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #有限状态机：三次分别记为 00->01->10
        #状态转移表
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones
