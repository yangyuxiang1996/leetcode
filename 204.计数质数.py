#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-19 11:05:20
LastEditors: yangyuxiang
LastEditTime: 2021-05-19 11:35:38
FilePath: /leetcode/204.计数质数.py
'''
#
# @lc app=leetcode.cn id=204 lang=python
#
# [204] 计数质数
#

# @lc code=start
import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        prime = [1] * n

        for i in range(2, int(math.sqrt(n))+1):
            if prime[i]:
                for j in range(i*i, n, i):
                    prime[j] = 0

        # res = 0
        # for i in range(2, n):
        #     if prime[i]:
        #         res += 1
        return sum(prime)-2


if __name__ == "__main__":
    n = 10
    print(Solution().countPrimes(n))

# @lc code=end

