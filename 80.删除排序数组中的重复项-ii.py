#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-23 10:31:48
LastEditors: yangyuxiang
LastEditTime: 2021-05-23 15:58:01
FilePath: /leetcode/80.删除排序数组中的重复项-ii.py
'''

#
# @lc app=leetcode.cn id=80 lang=python
#
# [80] 删除排序数组中的重复项 II
#


# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n

        slow, fast = 2, 2
        while fast < n:
            if nums[slow-2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow

    def removeDuplicates1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n

        pos = 1
        for i in range(1, len(nums) - 1):
            if nums[i - 1] != nums[i + 1]:
                nums[pos] = nums[i]
                pos += 1
        nums[pos] = nums[-1]
        return pos + 1


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(Solution().removeDuplicates(nums))
    print(nums)

# @lc code=end
