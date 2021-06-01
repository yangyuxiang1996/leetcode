#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-23 13:50:58
LastEditors: yangyuxiang
LastEditTime: 2021-04-23 15:10:22
FilePath: /leetcode/49.字母异位词分组.py
'''
#
# @lc app=leetcode.cn id=49 lang=python
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        c = {}
        for i, s in enumerate(strs):
            s = "".join(sorted(s))
            if s not in c: 
                c[s] = [i]
            else:
                c[s].append(i)
        
        results = []
        for _, v in c.items():
            results.append([strs[k] for k in v])
        
        return results 
                        

if __name__ == '__main__':
    input = ["","b"]
    print(Solution().groupAnagrams(input))                  
            

        
# @lc code=end

