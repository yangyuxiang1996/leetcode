#!/usr/bin/env python
# coding=utf-8
'''
Description: 先排序，再计算最长递增子序列的长度
Author: yangyuxiang
Date: 2021-04-26 07:35:47
LastEditors: yangyuxiang
LastEditTime: 2021-04-26 07:42:20
FilePath: /leetcode/354.俄罗斯套娃信封问题.py
'''
#
# @lc app=leetcode.cn id=354 lang=python
#
# [354] 俄罗斯套娃信封问题
#

# @lc code=start
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes = sorted(envelopes, key=lambda x: x[0])
        dp = [1] * len(envelopes)
        for i in range(len(envelopes)):
            for j in range(0, i):
                if envelopes[j][0] < envelopes[i][0] and \
                    envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        res = max(dp)
        return res
                    


        
# @lc code=end

