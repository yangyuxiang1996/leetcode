#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-22 08:29:33
LastEditors: yangyuxiang
LastEditTime: 2021-04-22 08:46:01
FilePath: /leetcode/7.整数反转.py
'''
#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if not (-2**31 <= x <= 2**31 - 1):
            return 0

        
        def helper(x):
            x = list(x)
            left = 0
            right = len(x) - 1
            while left < right:
                tmp = x[left]
                x[left] = x[right]
                x[right] = tmp
                left += 1
                right -= 1
            return "".join(x) if x[0] != 0 else "".join(x[1:])

        if x < 0:
            out = -1 * int(helper(str(x)[1:]))
            return out if out >= -2**31 else 0
            
        else:
            out = int(helper(str(x)))
            return out if out <= 2**31 - 1 else 0


        
# @lc code=end

