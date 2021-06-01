#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-20 06:43:18
LastEditors: yangyuxiang
LastEditTime: 2021-05-20 07:57:02
FilePath: /leetcode/42.接雨水.py
'''
#
# @lc app=leetcode.cn id=42 lang=python
#
# [42] 接雨水
# 对于位置i，所能盛的雨水量res[i] = max(min(max(height[:i]),
#                                   max(height[i+1:])
#                                   ) - height[i],
#                                   0
#                                   )
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        备忘录的方法用了两个数组，
        但是发现其实每一次只需要用到第i次的值
        因此可以边计算最大值边遍历，
        考虑到左右两边，可以采用双指针
        """
        n = len(height)
        if n < 3:
            return 0

        l_max = height[0]
        r_max = height[n-1]
        left, right = 1, n-2
        res = 0

        while left <= right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])
            if l_max < r_max:
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1
        return res
                

    def trap0(self, height):
        """
        :type height: List[int]
        :rtype: int
        因为每个位置我只需要知道它之前和之后的最大值，
        所以可以用两个数组提前算好，
        再遍历取对应的元素比较计算就好
        """
        n = len(height)
        if n < 3:
            return 0

        l_max, r_max = [0] * n, [0] * n
        l_max[0], r_max[n-1] = height[0], height[n-1]

        # 计算第i个位置之前的最大值
        for i in range(1, n):
            l_max[i] = max(height[i], l_max[i-1])

        # 倒序计算第i个位置之后的最大值
        for i in range(n-2, -1, -1):
            r_max[i] = max(height[i], r_max[i+1])

        # 计算每个位置所能盛的雨水量
        res = 0
        for i in range(n):
            res += min(l_max[i], r_max[i]) - height[i]

        return res

        

    def trap1(self, height):
        """
        :type height: List[int]
        :rtype: int
        暴力解法, 超时, O(N2)
        """
        res = 0
        for i in range(1, len(height)-1):
            res += max(min(max(height[:i]), max(height[i+1:])) - height[i], 0)

        return res


if __name__ == '__main__':
    height = [4,2,0,3,2,5]
    print(Solution().trap(height))

    
            

# @lc code=end

