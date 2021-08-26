#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-25 08:01:56
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-25 08:09:07
FilePath: /leetcode/剑指 Offer II 085. 生成匹配的括号.py
Description: 
正整数 n 代表生成括号的对数，请设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def helper(path, tmp_left, tmp_right):
            if tmp_left > n or tmp_right > n or tmp_left < tmp_right:
                return
            if tmp_left == n and tmp_right == n:
                res.append(path)
                return
            helper(path+"(", tmp_left+1, tmp_right)
            helper(path+")", tmp_left, tmp_right+1)
                
        res = []
        helper("", 0, 0)

        return res


if __name__ == '__main__':
    n = 1
    print(Solution().generateParenthesis(n))
