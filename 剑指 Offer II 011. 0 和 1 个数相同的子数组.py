#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-26 08:54:55
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-26 11:16:08
FilePath: /leetcode/剑指 Offer II 011. 0 和 1 个数相同的子数组.py
Description: 
给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
'''
class Solution(object):
    def findMaxLength0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 超时
        n = len(nums)
        res = 0
        dp_0 = [[0] * n for _ in range(n)]
        dp_1 = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    if nums[i] == 1:
                        dp_1[i][j] = 1
                    else:
                        dp_0[i][j] = 1
                else:
                    if nums[i] & nums[j]:
                        dp_1[i][j] = dp_1[i+1][j-1] + 2
                        dp_0[i][j] = dp_0[i+1][j-1]
                    elif nums[i] | nums[j]:
                        dp_1[i][j] = dp_1[i+1][j-1] + 1
                        dp_0[i][j] = dp_0[i+1][j-1] + 1
                    else:
                        dp_0[i][j] = dp_0[i+1][j-1] + 2
                        dp_1[i][j] = dp_1[i+1][j-1]
                    if dp_1[i][j] == dp_0[i][j]:
                        res = max(res, j-i+1)
        return res

    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 使用前缀和+哈希表
        m = {0:-1}
        n = len(nums)
        tmp, res = 0, 0
        for i in range(n):
            if nums[i] == 0:
                tmp -= 1  # 碰到0: -1
            else:
                tmp += 1 # 碰到1: +1
            if tmp in m:  # 如果前缀和在哈希表中
                res = max(res, i - m[tmp])  # 取最长
            else:
                m[tmp] = i  # 否则，把前缀和存入哈希表中，对应的值为前缀和的索引
        return res





if __name__ == "__main__":
    nums = [0,1,0]
    print(Solution().findMaxLength(nums))


        