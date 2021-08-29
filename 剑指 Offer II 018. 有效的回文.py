#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-27 11:32:37
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-27 11:50:25
FilePath: /leetcode/剑指 Offer II 018. 有效的回文.py
Description: 
给定一个字符串 s ，验证 s 是否是 回文串 ，只考虑字母和数字字符，可以忽略字母的大小写。
本题中，将空字符串定义为有效的 回文串 。
输入: s = "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串
'''
class Solution(object):
    def isdigit(self, c):
        return "0" <= c <= "9"
    def isalpha(self, c):
        return "a" <= c <= "z" or "A" <= c <= "Z"

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not self.isdigit(s[left]) and not self.isalpha(s[left]):
                left += 1
            while left < right and not self.isdigit(s[right]) and not self.isalpha(s[right]):
                right -= 1
            if left < right:
                if s[left] != s[right]:
                    if self.isalpha(s[left]) and self.isalpha(s[right]):
                        if s[left].upper() == s[right].upper():
                            left += 1
                            right -= 1
                        else:
                            return False
                    else:
                        return False
                else:
                    left += 1
                    right -= 1
        return True


if __name__ == '__main__':
    s = "race a car"
    print(Solution().isPalindrome(s))

