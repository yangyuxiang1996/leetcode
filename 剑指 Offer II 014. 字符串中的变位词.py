#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-27 10:01:30
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-27 10:32:03
FilePath: /leetcode/剑指 Offer II 014. 字符串中的变位词.py
Description: 
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的某个变位词。
换句话说，第一个字符串的排列之一是第二个字符串的 子串 。
'''
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # 滑动窗口
        import collections
        need = collections.defaultdict(int)
        window = collections.defaultdict(int)
        for c in s1:
            need[c] += 1
        left, right = 0, 0
        valid = 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):
                if right - left == len(s1):
                    return True
                c = s2[left]
                left += 1
                if c in window:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1

        return False


if __name__ == "__main__":
    s1 = "adc"
    s2 = "dcda"
    print(Solution().checkInclusion(s1, s2))



        

