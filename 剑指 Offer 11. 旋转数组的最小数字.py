#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-11 22:35:16
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-11 23:22:12
FilePath: /leetcode/剑指 Offer 11. 旋转数组的最小数字.py
Description: 
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  
'''

class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        if not numbers:
            return 0
        if numbers[0] < numbers[-1]:
            return numbers[0]
        left, right = 0, len(numbers)-1
        while left <= right:
            mid = left + (right - left) // 2
            if numbers[mid] < numbers[right]:
                # [left, right] -> [left, mid]
                right = mid
            elif numbers[mid] > numbers[right]:
                # [left, right] -> [mid+1, right]
                left = mid + 1
            else:
                # [left, right] -> [left, right-1]
                right -= 1
        return numbers[left]


if __name__ == '__main__':
    nums = [1]
    print(Solution().minArray(nums))
        

