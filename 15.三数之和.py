#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-15 09:31:13
LastEditors: yangyuxiang
LastEditTime: 2021-06-23 22:25:59
FilePath: /leetcode/15.三数之和.py
'''
#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
class Solution(object):
    def threeSum0(self, nums):
        """
        双指针法
        """
        nums = sorted(nums)
        n = len(nums)
        res = []
        i = 0
        for i in range(n):
            if nums[i] > 0:
                break # 因为是有序的，所以后面不可能存在三元组使得和为0
        
            if nums[i] == nums[i-1] and i >= 1:
                continue
            
            lo, hi = i+1, n-1
            while lo < hi:
                left, right = nums[lo], nums[hi]
                target = 0 - nums[i]
                if left + right < target:
                    lo += 1
                elif left + right > target:
                    hi -= 1
                else:
                    res.append([nums[i], left, right])
                    while lo < hi and nums[lo] == left:
                        lo += 1
                    while lo < hi and nums[hi] == right:
                        hi -= 1
                    
        return res


    def twoSum(self, nums, target):
        lo, hi = 0, len(nums)-1
        res = []
        while lo < hi:
            sum = nums[lo]+nums[hi]
            left, right = nums[lo], nums[hi]
            if sum < target:
                lo += 1
            elif sum > target:
                hi -= 1
            else:
                res.append([left, right])
                while lo < hi and nums[lo] == left:
                    lo += 1
                while lo < hi and nums[hi] == right:
                    hi -= 1
        return res
                
        
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        res = []

        i = 0
        while i < len(nums) :
            if nums[i] > 0:
                break
            other = 0 - nums[i]
            tmp = self.twoSum(nums[i+1:], other)
            for l in tmp:
                l.append(nums[i])
                res.append(l)
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1

            i+=1

        return res
                

if __name__ == "__main__":
    nums = [0,0,0] 
    print(Solution().threeSum(nums))       


# @lc code=end

