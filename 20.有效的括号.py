#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-24 07:51:33
LastEditors: yangyuxiang
LastEditTime: 2021-05-24 07:58:19
FilePath: /leetcode/20.有效的括号.py
'''

#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#


# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        r_l = {')': '(', ']': '[', '}': '{'}

        for i in range(len(s)):
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            else:
                if stack and r_l[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


if __name__ == '__main__':
    s = '()'
    print(Solution().isValid(s))


# @lc code=end
