#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-20 08:37:41
LastEditors: yangyuxiang
LastEditTime: 2021-05-20 09:01:58
FilePath: /leetcode/1011.在-d-天内送达包裹的能力.py
'''
#
# @lc app=leetcode.cn id=1011 lang=python
#
# [1011] 在 D 天内送达包裹的能力
#

# @lc code=start
class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        最大一次运载量为所有包裹的总重量，
        因为不能拆开，所以最小也要一次运走包裹里重量最大的
        从max(weights)到sum(weights)二分搜索
        """
        
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            if self.isValid(mid, weights, days):
                right = mid
            else:
                left = mid + 1

        return left

    def isValid(self, k, weights, days):
        
        # sum = 0
        # c = 1
        # for i in range(len(weights)):
        #     sum += weights[i]
        #     if sum > k:
        #         sum = weights[i]
        #         c += 1

        #     if c > days:
        #         return False
        # return True
        i = 0
        for j in range(days):
            maxCap = k
            while maxCap - weights[i] >= 0:
                maxCap -= weights[i]
                i+=1
                if i == len(weights):
                    return True

        return False


if __name__ == "__main__":
    weights = [1,2,3,4,5,6,7,8,9,10]
    D = 5
    print(Solution().shipWithinDays(weights, D))



        
# @lc code=end

