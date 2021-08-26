#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-24 22:11:44
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-24 22:38:29
FilePath: /leetcode/剑指 Offer II 002. 二进制加法.py
Description: 
给定两个 01 字符串 a 和 b ，请计算它们的和，并以二进制字符串的形式输出。
输入为 非空 字符串且只包含数字 1 和 0。
输入: a = "11", b = "10"
输出: "101"
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a)-1, len(b)-1
        carry, res = 0, []
        while i >= 0 or j >= 0:
            if i >= 0:
                digitA = ord(a[i]) - ord('0')
                i -= 1
            else:
                digitA = 0
            if j >= 0:
                digitB = ord(b[j]) - ord('0')
                j -= 1
            else:
                digitB = 0
            
            sum = digitA + digitB + carry
            if sum >= 2:
                carry = 1
                sum = sum - 2
            else:
                carry = 0
                sum = sum
            res.append(str(sum))

        if carry == 1:
            res.append("1")
        return "".join(res[::-1])



if __name__ == '__main__':
    a = '1011'
    b = '1010'
    print(Solution().addBinary(a, b))
            
            

        
            




