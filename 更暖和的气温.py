#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-10 18:41:34
LastEditors: yangyuxiang
LastEditTime: 2021-05-10 18:58:40
FilePath: /leetcode/更暖和的气温.py
'''
class Solution:
    def nextWarmTemperature(self, nums):
        l = len(nums)
        stack = []
        res = [0] * l
        
        for i in range(l-1, -1, -1):
            while stack != [] and nums[stack[-1]] < nums[i]:
                stack.pop()
            
            if stack:
                res[i] = stack[-1] - i
                

            stack.append(i)

        return res

if __name__ == '__main__':
    print(Solution().nextWarmTemperature([73,74,75,71,69,72,76,73]))


