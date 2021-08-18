#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-18 10:11:39
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-18 10:28:10
FilePath: /leetcode/剑指 Offer 44. 数字序列中某一位的数字.py
Description: 
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。
请写一个函数，求任意第n位对应的数字。
'''
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # count = digit*start*9
        if n < 10:
            return n
        
        # 先找n位对应的位数digit
        digit, start, count = 1, 1, 9
        while n > count:
            n -= count
            start *= 10
            digit += 1
            count = digit * start * 9

        # 找n位在哪个数字中
        num = start + (n - 1)//digit

        # 找n位对应的数字
        s = str(num)
        res = s[(n-1)%digit]

        return int(res)
        

