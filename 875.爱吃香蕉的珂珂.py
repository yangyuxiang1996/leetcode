#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-20 07:59:42
LastEditors: yangyuxiang
LastEditTime: 2021-05-20 08:24:03
FilePath: /leetcode/875.爱吃香蕉的珂珂.py
'''
#
# @lc app=leetcode.cn id=875 lang=python
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
class Solution(object):
    def isValid(self, k, piles, h):
        count = 0
        for i in range(len(piles)):
            count += piles[i] // k
            if piles[i] % k != 0:
                count += 1
            
            if count > h:
                return False
        
        return True
        
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        因为一个小时最多只能吃一堆，所以最大速度就是max(piles)，最小值指定是1
        那么直接从最小值到最大值线性搜索，找到满足条件的最小k即可
        因为有序，所以可以用二分搜索查找左侧边界
        """
        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2
            if self.isValid(mid, piles, h):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    piles = [3,6,7,11]
    h=8
    print(Solution().minEatingSpeed(piles, h))
# @lc code=end

