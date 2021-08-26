#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-25 10:29:08
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-25 14:03:19
FilePath: /leetcode/剑指 Offer II 086. 分割回文子字符串.py
Description: 
给定一个字符串 s ，请将 s 分割成一些子串，使每个子串都是 回文串 ，返回 s 所有可能的分割方案。
回文串 是正着读和反着读都一样的字符串。
输入：s = "google"
输出：[["g","o","o","g","l","e"],["g","oo","g","l","e"],["goog","l","e"]]
'''
class Solution(object):
    def isValid(self, s, left, right):
        if left == right:
            return True
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []

        def helper(s, start, path):
            if start >= len(s):
                res.append(path[:])
            
            for i in range(start, len(s)):
                if self.isValid(s, start, i):
                    path.append(s[start:i+1])
                    helper(s, i+1, path)
                    path.pop()
            
        helper(s, 0, [])
        return res


if __name__ == "__main__":
    s = "googlel"
    print(Solution().partition(s))

        
