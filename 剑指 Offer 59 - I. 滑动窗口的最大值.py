#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-23 23:33:51
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-24 00:33:21
FilePath: /leetcode/剑指 Offer 59 - I. 滑动窗口的最大值.py
Description: 
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
'''
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        stack, ans = [], []
        for i in range(k):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            stack.append(i)
        ans.append(nums[stack[0]])

        for i in range(k, len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            stack.append(i)
            if stack[0] == i-k:
                stack.pop(0)
            ans.append(nums[stack[0]])

        return ans

    
if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(Solution().maxSlidingWindow(nums, k))
            
        

