#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-28 10:41:33
LastEditors: yangyuxiang
LastEditTime: 2021-04-28 22:30:13
FilePath: /leetcode/650.只有两个键的键盘.py
'''
#
# @lc app=leetcode.cn id=650 lang=python
#
# [650] 只有两个键的键盘
#

# @lc code=start
class Solution:
    def minSteps(self, n):
        
        dp = [float('inf')] * (n+1)	
		## Intialize a dp array to store the solutions of sub problems i.e. number of steps needed
	
        dp[1] = 0
		## Intially first element of dp array with 0 as 'A' is already present and we haven't consumed any steps yet. 
		## As the value of n is from [1,3000] and initally 'A' is already present so we don't need to bother about the dp[0]
        
        for i in range(2, n+1):
            for j in range(1, i):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i//j)
        return dp[-1]

if __name__ == '__main__':
    print(Solution().minSteps(20))
         
        
# @lc code=end

