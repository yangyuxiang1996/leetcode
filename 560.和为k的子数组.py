#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-18 09:48:11
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-26 08:44:12
FilePath: /leetcode/560.和为k的子数组.py
'''
#
# @lc app=leetcode.cn id=560 lang=python
#
# [560] 和为K的子数组
#

# @lc code=start
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = {0:1}
        res = 0
        sum_i = 0
        for i in range(0, len(nums)):
            sum_i = sum_i + nums[i]
            
            sum_j = sum_i - k
            if sum_j in sum:
                res += sum[sum_j]
            
            if sum_i not in sum:
                sum[sum_i] = 1
            else:
                sum[sum_i] += 1


                    
        return res

if __name__ == '__main__':
    nums = [1]
    k=0
    print(Solution().subarraySum(nums, k))
                

            
        
# @lc code=end

