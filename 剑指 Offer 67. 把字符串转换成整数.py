#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-21 09:19:17
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-21 10:08:49
FilePath: /leetcode/剑指 Offer 67. 把字符串转换成整数.py
Description: 
写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。
'''
class Solution(object):
    def extract(self, str):
        left, right = 0, 0
        while left < len(str) and str[left] == ' ':
            left += 1
        if left == len(str):
            return None
        if str[left] == '+' or str[left] == '-':
            right = left + 1
        else:
            right = left
        while right < len(str):
            if "0" <= str[right] <= "9":
                right += 1
            else:
                break
        
        return str[left:right]

    def strToInt(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        valid_str = self.extract(str)
        if not valid_str:
            return 0
        
        int_min, int_max, bndry = -2**31, 2**31-1, 2**31 // 10
        res, i, sign = 0, 1, 1
        if valid_str[0] == '-':
            sign = -1
        elif valid_str[0] != '+':
            i = 0
        
        for c in valid_str[i:]:
            if res > bndry or res == bndry and c > '7': 
                return int_max if sign == 1 else int_min # 数字越界处理
            res = 10 * res + ord(c) - ord('0') # 数字拼接
        return sign * res


if __name__ == '__main__':
    str = "-91283472332"
    print(Solution().strToInt(str))


