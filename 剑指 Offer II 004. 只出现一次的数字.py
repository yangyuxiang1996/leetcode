#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-24 22:42:24
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-24 23:00:39
FilePath: /leetcode/剑指 Offer II 004. 只出现一次的数字.py
Description: 
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
输入：nums = [2,2,3,2]
输出：3
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # hashmap
        import collections
        count = collections.defaultdict(int)
        for num in nums:
            count[num] += 1
        for num in nums:
            if count[num] == 1:
                return num
        return -1

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 不使用额外空间
        # 0~31位，统计每一位上1的数量，如果恰好比3的倍数多一个，说明这一位在所求的数字上
        res = 0
        is_neg = 0
        for i in range(32):
            count = 0
            for num in nums:
                if (num >> i) & 1:
                    count += 1
            if count % 3 == 1:
                res += 2**i
                if i == 31:
                    is_neg = True
                
        return res if not is_neg else res - 2**32


if __name__ == "__main__":
    nums = [1,1,1,2,3,3,3]
    print(Solution().singleNumber(nums))



        