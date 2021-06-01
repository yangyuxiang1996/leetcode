#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-06 22:12:18
LastEditors: yangyuxiang
LastEditTime: 2021-05-06 22:20:43
FilePath: /leetcode/二分插入.py
'''
def insert(nums, val):
    left = 0
    right = len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < val and nums[mid+1] > val:
            return mid+1
        elif nums[mid] > val:
            right = mid
        else:
            left = mid + 1

print(insert([1,2,3,5,7,8], 6))
