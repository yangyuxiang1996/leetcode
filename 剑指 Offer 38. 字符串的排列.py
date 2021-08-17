#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-17 23:34:29
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-18 00:07:54
FilePath: /leetcode/剑指 Offer 38. 字符串的排列.py
Description: 
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素.
'''
class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # 回溯
        def backtrace(s, visited, path):
            repeat = []  # 当前层去重，不需排序
            if len(path) == len(s):
                res.append("".join(path))
                return
            for i in range(0, len(s)):
                if s[i] in repeat or visited[i] == True:
                    continue
                path.append(s[i])
                repeat.append(s[i])
                visited[i] = True
                backtrace(s, visited, path)
                path.pop()
                visited[i] = False
            
        res = []
        visited = [False] * len(s)
        backtrace(s, visited, [])
        return res

    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # 回溯
        def backtrace(s, visited, path):
            if len(path) == len(s):
                res.append("".join(path))
                return
            for i in range(0, len(s)):
                if i > 0 and s[i] == s[i-1] and visited[i-1] == False:  # 当前层去重，必须有序
                    continue
                if visited[i] == True:
                    continue
                path.append(s[i])
                visited[i] = True
                backtrace(s, visited, path)
                path.pop()
                visited[i] = False
            
        res = []
        s = sorted(s)
        visited = [False] * len(s)
        backtrace(s, visited, [])
        return res



