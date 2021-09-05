#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-09-02 08:56:11
LastEditors: Yuxiang Yang
LastEditTime: 2021-09-02 09:06:07
FilePath: /leetcode/剑指 Offer II 094. 最少回文分割.py
Description: 
给定一个字符串 s，请将 s 分割成一些子串，使每个子串都是回文串。
返回符合要求的 最少分割次数 。
'''
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        g = [[0] * n for i in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    g[i][j] = 1
                else:
                    g[i][j] = 1 if g[i+1][j-1] and s[i] == s[j] else 0
        
        f = [float('inf')] * n
        for i in range(n):
            if g[0][i] == 1: 
                f[i] = 0
            else: 
                for j in range(i):
                    if g[j+1][i]:  
                        f[i] = min(f[i], f[j]+1)
        return f[n-1]




