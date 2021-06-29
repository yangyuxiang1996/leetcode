#!/usr/bin/env python
# coding=utf-8
'''
Description
Author: yangyuxiang
Date: 2021-05-18 08:05:03
LastEditors: yangyuxiang
LastEditTime: 2021-05-18 08:42:39
FilePath: /leetcode/969.煎饼排序.py
'''
#
# @lc app=leetcode.cn id=969 lang=python
#
# [969] 煎饼排序
#

# @lc code=start
class Solution(object):          
        
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = []

        def reverse(arr, i, j):
            while i < j:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
                i += 1
                j -= 1  
        
        def helper(arr, n):
            if n == 1:
                return
            
            max_v = arr[0]
            max_i = 0
            for i in range(n):
                if arr[i] > max_v:
                    max_v = arr[i]
                    max_i = i
            reverse(arr, 0, max_i)
            res.append(max_i+1)
            reverse(arr, 0, n-1)
            res.append(n)

            helper(arr, n-1)

        
        helper(arr, len(arr))
        return res


if __name__ == '__main__':
    arr = [1,2,3]
    print(Solution().pancakeSort(arr))
   

# @lc code=end

