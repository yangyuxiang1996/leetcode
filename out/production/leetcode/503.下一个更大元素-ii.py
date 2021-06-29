#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-10 18:34:03
LastEditors: yangyuxiang
LastEditTime: 2021-05-11 08:16:23
FilePath: /leetcode/503.下一个更大元素-ii.py
'''
#
# @lc app=leetcode.cn id=503 lang=python
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        
        stack = []
        res = [-1] * l
        for i in range(2*l-1, -1, -1):
            while stack != [] and stack[-1] <= nums[i%l]: 
                stack.pop()
            
            if stack:
                res[i%l] = stack[-1] 
            
            stack.append(nums[i%l])

        return res

if __name__ == "__main__":
    print(Solution().nextGreaterElements([1,2,1]))
            
     
            
# @lc code=end

