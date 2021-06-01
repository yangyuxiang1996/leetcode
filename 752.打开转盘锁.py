#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-21 21:54:06
LastEditors: yangyuxiang
LastEditTime: 2021-04-21 22:57:09
FilePath: /leetcode/752.打开转盘锁.py
'''
#
# @lc app=leetcode.cn id=752 lang=python
#
# [752] 打开转盘锁
#

# @lc code=start
class Solution(object):

    def plusOne(self, cur, i):
        cur = list(cur)
        if cur[i] == '9':
            cur[i] = '0'
        else:
            cur[i] = str(int(cur[i]) + 1)
        return ''.join(cur)
    
    def minusOne(self, cur, i):
        cur = list(cur)
        if cur[i] == '0':
            cur[i] = '9'
        else:
            cur[i] = str(int(cur[i]) - 1)
        return ''.join(cur)

    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if "0000" in deadends:
            return -1
        
        deads = set()
        for dead in deadends:
            deads.add(dead)
        root = ['0000']
        step = 0
        visited = set()
        visited.add('0000')

        while root:
            for j in range(len(root)):
                cur = root.pop(0)
                if cur in deadends:
                    continue
                if cur == target:
                    return step
                
                for i in range(4):
                    next = self.plusOne(cur, i)
                    if next in visited:
                        continue
                    root.append(next)
                    visited.add(next)
                for i in range(4):
                    next = self.minusOne(cur, i)
                    if next in visited:
                        continue
                    root.append(next)
                    visited.add(next)
                
            step += 1
        
        return -1
            
        
        
        
# @lc code=end

