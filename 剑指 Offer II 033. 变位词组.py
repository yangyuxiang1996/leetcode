#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-09-03 00:49:34
LastEditors: Yuxiang Yang
LastEditTime: 2021-09-03 00:59:10
FilePath: /leetcode/剑指 Offer II 033. 变位词组.py
Description: 
给定一个字符串数组 strs ，将 变位词 组合在一起。 可以按任意顺序返回结果列表。
注意：若两个字符串中每个字符出现的次数都相同，则称它们互为变位词。
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # hashmap
        if len(strs) == 1:
            return [strs]
        
        m = {}
        for s in strs:
            ss = "".join(sorted(s))
            if ss in m:
                m[ss].append(s)
            else:
                m[ss] = [s]
        
        return list(m.values())

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))


