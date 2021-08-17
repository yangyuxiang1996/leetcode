#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-14 09:15:53
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-14 23:17:12
FilePath: /leetcode/剑指 Offer 16. 数值的整数次方.py
Description: 
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。
'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        利用二进制
        """
        if x == 0:
            return 0
        res = 1
        if n < 0:
            x, n = 1 / x, -n
        
        while n:
            if n & 1 == 1:
                res *= x
            n >>= 1
            x *= x
        
        return res


    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        递归
        """
        flag = False
        if n < 0:
            flag = True
            n = -1 * n
        
        def helper(x, n):
            if n == 0:
                return 1
            print(n)
            tmp = helper(x, n//2)
            if n % 2 == 0:
                return tmp * tmp       
            else:
                return x * tmp * tmp
        
        ans = helper(x, n)
        if flag:
            return 1 / ans
        else:
            return ans


if __name__ == '__main__':
    x = 0.00001
    n = 20
    print(Solution().myPow(x,n))
