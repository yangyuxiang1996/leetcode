#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-01 00:08:06
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-10 19:00:20
FilePath: /leetcode/0.快速排序.py
Description: 
'''
def quickSort(nums, left, right):
    if left >= right:
        return
    mid = partition0(nums, left, right)
    quickSort(nums, left, mid-1)
    quickSort(nums, mid+1, right)
    
def partition0(nums, left, right):
    pivot = nums[left]
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= pivot: # 从右往左找第一个比pivot小的
            j-=1
        while i < j and nums[i] <= pivot: # 从左往右找第一个比pivot大的
            i+=1
        # 交换
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    # 此时nums[i]一定比pivot大
    if i > left:
        nums[i], nums[left] = nums[left], nums[i]
    return i

def partition(nums, left, right):
    pivot = nums[left]  # 以最左边元素作为轴心，最后以pivot作为分界，左边元素都小于等于pivot，右边元素都大于等pivot
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= pivot: # 找第一个比pivot小的，放左边
            j-=1
        if i < j:
            nums[i] = nums[j]
        while i < j and nums[i] <= pivot: # 找第一个比pivot大的，放右边
            i+=1
        if i < j:
            nums[j] = nums[i]
        
    nums[i] = pivot  # mid位置放pivot
    return i  # 返回mid位置


def sort(nums):
    quickSort(nums, 0, len(nums)-1)

if __name__ == '__main__':
    nums = [49, 38, 65, 97, 76, 13, 27, 49]
    sort(nums)
    print(nums)

        
        

    