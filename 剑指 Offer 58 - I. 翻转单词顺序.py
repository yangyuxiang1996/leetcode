#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-19 08:42:47
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-19 12:57:06
FilePath: /leetcode/剑指 Offer 58 - I. 翻转单词顺序.py
Description: 
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。
'''
class Solution(object):
    def reverse(self, s, left, right):
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 先整体翻转，再逐个翻转
        # 先去除两边的空格
        left, right = 0, len(s)-1
        while left <= right and s[left] == ' ':
                left += 1
        while left <= right and s[right] == ' ':
                right -= 1
        if left > right:
            return ""
        
        # 用快慢指针去除中间的空格
        strs = list(s[left:right+1])
        slow, fast = 0, 0
        while fast < len(strs):
            while strs[fast] == ' ' and strs[fast-1] == ' ':
                fast += 1
            strs[slow] = strs[fast]
            fast += 1
            slow += 1

        strs = strs[0:slow]     
        self.reverse(strs, 0, len(strs)-1)

        start = 0
        end = 0
        while end < len(strs)-1:
            if strs[end] != ' ':
                end += 1
            else:
                self.reverse(strs, start, end-1)
                start = end+1
                end += 1
        self.reverse(strs, start, end)
        return "".join(strs)


if __name__ == '__main__':
    s = ""
    print(Solution().reverseWords(s))
                

