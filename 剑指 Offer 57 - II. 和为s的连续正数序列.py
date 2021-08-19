#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-19 07:42:00
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-19 08:25:26
FilePath: /leetcode/剑指 Offer 57 - II. 和为s的连续正数序列.py
Description: 
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
输入：target = 9
输出：[[2,3,4],[4,5]]
'''
from copy import deepcopy
class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        tmp = 0
        end = (target+1)//2+1
        for i in range(1, end):
            tmp += i
            path.append(i)
            while tmp > target:
                tmp -= path.pop(0)
            if tmp == target:
                res.append(deepcopy(path))
                
        return res

    def findContinuousSequence0(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        # 双指针
        i, j, tmp = 1, 2, 3
        res = []
        while i < j:
            j += 1
            tmp += j
            while tmp > target:
                tmp -= i
                i += 1
            if tmp == target:
                res.append(list(range(i, j+1)))

        return res

if __name__ == '__main__':
    target = 9
    print(Solution().findContinuousSequence(target))
            
