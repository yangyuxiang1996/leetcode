#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-21 16:29:41
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-21 17:02:54
FilePath: /leetcode/剑指 Offer 60. n个骰子的点数.py
Description: 
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
假设n=1，和一共有6种，6=5*1+1
n=2, 和一共有11种（最小是2，最大是12），11=5*2+1
n=3, 和一共有16种（最小是3，最大是18），11=5*3+1
依次类推
https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/solution/jian-zhi-offer-60-n-ge-tou-zi-de-dian-sh-z36d/
'''

class Solution(object):
    def dicesProbability(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        dp = [1 / 6] * 6  # 初始化一个骰子
        for i in range(2, n+1): # 从第二个骰子开始遍历
            tmp = [0] * (5*i+1)  # 初始化下一个骰子
            for j in range(len(dp)):
                for k in range(6): # 固定下一个骰子的值，
                    tmp[j+k] += dp[j] / 6
            dp = tmp
        return dp


if __name__ == '__main__':
    print(Solution().dicesProbability(1))




