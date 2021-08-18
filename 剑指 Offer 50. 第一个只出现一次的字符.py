#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-18 11:36:18
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-18 14:38:46
FilePath: /leetcode/剑指 Offer 50. 第一个只出现一次的字符.py
Description: 
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
'''
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 使用双端队列
        from collections import deque
        p = deque()
        hm = {}

        for i in range(len(s)):
            if s[i] not in hm:
                hm[s[i]] = i
                p.append(s[i], i)
            else:
                hm[s[i]] = -1
            while p and hm[p[0][0]] == -1:
                p.popleft()
        return " " if not p else p[0][0]
        
        
        
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 使用哈希表
        if not s:
            return " "

        import collections
        m = collections.defaultdict(int)
        for i in range(len(s)):
            m[s[i]] += 1
        for i in range(len(s)):
            if m[s[i]] == 1:
                return s[i]
        return " "

