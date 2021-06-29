#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-28 22:32:14
LastEditors: yangyuxiang
LastEditTime: 2021-04-29 08:17:58
FilePath: /leetcode/887.鸡蛋掉落.py
'''
#
# @lc app=leetcode.cn id=887 lang=python
#
# [887] 鸡蛋掉落
#

# @lc code=start
class Solution(object):
    def superEggDrop(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        memo = {}
        def helper(k, n):
            if k == 1:
                return n
            if n == 0:
                return 0
            
            if (k, n) in memo:
                return memo[(k,n)]
            res = float("inf")

            left = 1
            right = n
            while left <= right:
                mid = (left + right) // 2
                broken = helper(k-1, mid-1)
                not_broken = helper(k, n-mid)
                if broken >= not_broken:
                    right = mid - 1
                    res = min(res, broken+1)
                else:
                    left = mid + 1
                    res = min(res, not_broken+1)

            memo[(k,n)] = res
            return res
            
        return helper(k,n) 
        
# @lc code=end

