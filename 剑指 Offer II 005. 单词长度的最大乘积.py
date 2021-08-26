#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-24 23:01:47
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-24 23:13:07
FilePath: /leetcode/剑指 Offer II 005. 单词长度的最大乘积.py
Description: 
给定一个字符串数组 words，请计算当两个字符串 words[i] 和 words[j] 不包含相同字符时，它们长度的乘积的最大值。
假设字符串中只包含英语的小写字母。如果没有不包含相同字符的一对字符串，返回 0。
'''
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # 二维数组，判断是否有重复单词
        flags = [[0] * 26 for _ in range(len(words))]
        ans = 0
        for i in range(len(words)):
            for c in words[i]:
                flags[i][ord(c) - ord('a')] = 1
        for i in range(0, len(words)):
            for j in range(i+1, len(words)):
                k = 0
                while k < 26:
                    if flags[i][k] and flags[j][k]:
                        break
                    k += 1
                if k == 26:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans


if __name__ == '__main__':
    words = ["abcw","baz","foo","bar","fxyz","abcdef"]
    print(Solution().maxProduct(words))



