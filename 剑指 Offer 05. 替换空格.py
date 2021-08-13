#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-12 21:27:49
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-12 21:29:59
FilePath: /leetcode/剑指 Offer 05. 替换空格.py
Description: 
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
'''
class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        i = 0
        while i < len(s):
            if s[i] != ' ':
                stack.append(s[i])
            else:
                stack.append("%20")
            i += 1
        return "".join(stack)