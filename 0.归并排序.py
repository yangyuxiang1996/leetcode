#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-07-31 12:24:29
LastEditors: Yuxiang Yang
LastEditTime: 2021-07-31 12:58:01
FilePath: /leetcode/0.排序.py
Description: 排序
'''

"""
归并排序：时间复杂度O(nlogn)
"""
def merge(list_left, list_right):
    """
    入参数组都是有序的，此处将两个有序数组合并成一个大的有序数组
    """
    # 两个数组的起始下标
    l, r = 0, 0

    new_list = []
    while l < len(list_left) and r < len(list_right):
        if list_left[l] <= list_right[r]:
            new_list.append(list_left[l])
            l += 1
        else:
            new_list.append(list_right[r])
            r += 1
    new_list += list_left[l:]
    new_list += list_right[r:]
    return new_list

def merge_sort(mylist):
    """
    归并排序
    mylist: 待排序数组
    return: 新数组list
    """
    if len(mylist) <= 1:
        return mylist

    mid = len(mylist) // 2
    list_left = merge_sort(mylist[:mid])
    list_right = merge_sort(mylist[mid:])
    return merge(list_left, list_right)

if __name__ == '__main__':
    nums = [10, 8, 2, 6, 1, 0]
    nums = merge_sort(nums)
    print(nums)
