#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-20 23:42:52
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-20 23:53:29
FilePath: /leetcode/剑指 Offer 64. 求1+2+…+n.py
Description: 
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
此题考查逻辑运算符的短路连接性质
'''
class Solution(object):
    def __init__(self):
        self.res = 0

    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1:
        #     return 1
        # return self.sumNums(n-1) + n

        n > 1 and self.sumNums(n-1)
        self.res += n
        return self.res
    

if __name__ == '__main__':
    n = 9
    print(Solution().sumNums(n))
