#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-20 22:49:45
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-20 23:37:36
FilePath: /leetcode/剑指 Offer 61. 扑克牌中的顺子.py
Description: 
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
输入: [1,2,3,4,5]
输出: True
'''
class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tmp = [0] * 14
        min_num, max_num = 14, -1
        for num in nums:
            tmp[num] += 1
            if num != 0:
                min_num = min(min_num, num)
                max_num = max(max_num, num)
            if tmp[num] > 1 and num != 0:
                return False
            if max_num - min_num >= 5:
                return False
        return True
        