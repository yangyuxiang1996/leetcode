#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-20 00:39:35
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-20 08:30:19
FilePath: /leetcode/剑指 Offer 62. 圆圈中最后剩下的数字.py
Description: 
0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。
例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
题解：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/javajie-jue-yue-se-fu-huan-wen-ti-gao-su-ni-wei-sh/
'''
class Solution:
    def lastRemaining(self, n, m):
        ans = 0
        # 最后一轮剩下两个人，所以从2开始反推
        for i in range(2, n + 1):
            ans = (ans + m) % i
        return ans
