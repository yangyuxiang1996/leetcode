#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-31 14:04:32
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-31 16:12:26
FilePath: /leetcode/剑指 Offer II 092. 翻转字符.py
Description: 
如果一个由 '0' 和 '1' 组成的字符串，是以一些 '0'（可能没有 '0'）后面跟着一些 '1'（也可能没有 '1'）的形式组成的，那么该字符串是 单调递增 的。
我们给出一个由字符 '0' 和 '1' 组成的字符串 s，我们可以将任何 '0' 翻转为 '1' 或者将 '1' 翻转为 '0'。
返回使 s 单调递增 的最小翻转次数。
输入：s = "00110"
输出：1
解释：我们翻转最后一位得到 00111.
'''
class Solution(object):
    def minFlipsMonoIncr0(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 0
        
        # 定义dp[i][0]表示前i个元素,最后一个元素为0的最小翻转次数，
        # dp[i][1]表示前i个元素，最后一个元素为1的最小翻转次数。
        dp = [0, 0]
        if s[0] == '0':
            dp[1] = 1
        else:
            dp[0] = 1
        
        for i in range(1, len(s)):
            dp[1] = min(dp[0], dp[1]) + (0 if s[i] == '1' else 1) # 最后一个元素为1,前面的可能是0，也可能是1
            dp[0] = dp[0] + (0 if s[i] == '0' else 1)  # 最后一个元素为0,前面的只能是0

        return min(dp)
    
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0 # 记录1的数量
        ans = 0

        for i in range(len(s)):
            if s[i] == '1':
                cnt += 1
            else:
                # 两种情况，一种是将0翻转成1，一种是将0前面的1全部变成0
                ans = min(ans+1, cnt)

        return ans





