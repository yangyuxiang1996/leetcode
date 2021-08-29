#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File:       剑指 Offer II 015. 字符串中的所有变位词.py
@Time:       2021/08/27 10:47:31
@Author:     Yuxiang Yang
@Version:    1.0
@Describe:   
给定两个字符串 s 和 p，找到 s 中所有 p 的 变位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
变位词 指字母相同，但排列不同的字符串。
'''
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        import collections
        need = collections.defaultdict(int)
        window = collections.defaultdict(int)
        res = []
        for c in p:
            need[c] += 1
        
        left, right, valid = 0, 0, 0
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):
                if right - left == len(p):
                    res.append(left)
                c = s[left]
                left += 1
                if c in window:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        return res


if __name__ == '__main__':
    s = "abab"
    p = "ab"
    print(Solution().findAnagrams(s, p))



