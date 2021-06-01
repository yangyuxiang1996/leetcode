#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-17 21:49:04
LastEditors: yangyuxiang
LastEditTime: 2021-05-18 07:39:52
FilePath: /leetcode/224.基本计算器.py
'''
#
# @lc app=leetcode.cn id=224 lang=python
#
# [224] 基本计算器
#

# @lc code=start
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, num, sign = 0, 0, 1
        stack = []
        signs = []
        for i in range(0, len(s)):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in ['+', '-']:
                res = res + sign * num
                sign = 1 if c == '+' else -1
                num = 0
            elif c == '(':
                stack.append(res)
                signs.append(sign)
                res = 0
                sign = 1
                num = 0
            elif c == ')':
                res = res + sign * num
                res = res * signs.pop()
                res = res + stack.pop()
                num = 0

        res = res + sign * num

        return res



if __name__ == '__main__':
    s = '1 + 1'
    print(Solution().calculate(s))
            



        
# @lc code=end

