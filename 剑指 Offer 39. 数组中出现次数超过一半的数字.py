#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-18 00:11:04
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-18 00:19:56
FilePath: /leetcode/剑指 Offer 39. 数组中出现次数超过一半的数字.py
Description: 
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
'''
class Solution(object):
    def majorityElement0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        m = collections.defaultdict(int)
        for num in nums:
            m[num] += 1
            if m[num] > len(nums) / 2:
                return num
        return -1

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] == res:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    cnt = 1
                    res = nums[i]
        return res


if __name__ == '__main__':
    nums = [3,1,2,3,5,3,4,3]
    print(Solution().majorityElement(nums))


    
