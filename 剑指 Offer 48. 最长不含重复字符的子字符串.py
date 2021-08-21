#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-21 23:07:38
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-21 23:42:45
FilePath: /leetcode/剑指 Offer 48. 最长不含重复字符的子字符串.py
Description: 
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
'''
class Solution(object):
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 1:
            return n
        
        left, right = 0, 0
        window = {}
        ans = 0
        while right < n:
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1
                while left < right and window[s[right]] != 1:
                    window[s[left]] -= 1
                    left += 1
            right += 1
            ans = max(ans, right-left)

        return ans

    def lengthOfLongestSubstring0(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 1:
            return n
        
        left, right = 0, 0
        window = {}
        ans = 0
        while right < n:
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1
            while window[s[right]] != 1:
                window[s[left]] -= 1
                left += 1
            right += 1
            ans = max(ans, right-left)
        return ans

    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic, res ,i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(i, dic[s[j]]) # i 为s[j]上一次出现的索引
            dic[s[j]] = j # 更新最后出现的索引
            res = max(res, j-i)

        return res


if __name__ == '__main__':
    s = "au"
    print(Solution().lengthOfLongestSubstring(s))




