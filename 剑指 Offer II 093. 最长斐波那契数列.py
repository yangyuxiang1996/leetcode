#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-09-01 08:33:35
LastEditors: Yuxiang Yang
LastEditTime: 2021-09-01 09:07:01
FilePath: /leetcode/剑指 Offer II 093. 最长斐波那契数列.py
Description: 
如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的：
n >= 3
对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2}
给定一个严格递增的正整数数组形成序列 arr ，找到 arr 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。
（回想一下，子序列是从原序列  arr 中派生出来的，它从 arr 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。例如， [3, 5, 8] 是 [3, 4, 5, 6, 7, 8] 的一个子序列）
'''
class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        m = {}
        for i in arr:
            m[i] = 0
        
        ans = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                x, y = arr[j], arr[i] + arr[j]
                count = 2
                while y in m:
                    x, y = y, x + y
                    count += 1
                ans = max(ans, count)
        return ans if ans >= 3 else 0


if __name__ == '__main__':
    arr = [1, 10, 11]
    print(Solution().lenLongestFibSubseq(arr))

