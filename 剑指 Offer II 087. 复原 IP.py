#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-25 22:03:02
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-25 22:39:53
FilePath: /leetcode/剑指 Offer II 087. 复原 IP.py
Description: 
给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。
有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
'''
class Solution(object):
    def isValid(self, s):
        if len(s) > 3:
            return False
        if len(s) > 1 and s[0] == '0':
            return False
        if int(s) > 255:
            return False
        return True

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []

        def helper(s, start, path):
            if len(path) == 4:
                if start >= len(s):
                    res.append(path[:])
                return
            
            for i in range(start, len(s)):
                if self.isValid(s[start:i+1]):
                    path.append(s[start:i+1])
                    helper(s, i+1, path)
                    path.pop()
        helper(s, 0, [])
        return [".".join(ip) for ip in res]


if __name__ == '__main__':
    s = "1111"
    print(Solution().restoreIpAddresses(s))
