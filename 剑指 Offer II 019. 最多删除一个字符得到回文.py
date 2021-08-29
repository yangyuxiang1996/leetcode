#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-28 23:22:30
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-29 00:00:48
FilePath: /leetcode/剑指 Offer II 019. 最多删除一个字符得到回文.py
Description: 
给定一个非空字符串 s，请判断如果 最多 从字符串中删除一个字符能否得到一个回文字符串。
'''
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isValid(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def helper(s, left, right):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    # 两种情况
                    # 删掉left
                    # 删掉right
                    return isValid(s, left+1, right) or isValid(s, left, right-1)
            return True

        return helper(s, 0, len(s) - 1)


if __name__ == '__main__':
    s = "abc"
    print(Solution().validPalindrome(s))

