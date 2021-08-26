#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-25 23:07:45
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-25 23:21:15
FilePath: /leetcode/剑指 Offer II 088. 爬楼梯的最少成本.py
Description: 
数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。
每当爬上一个阶梯都要花费对应的体力值，一旦支付了相应的体力值，就可以选择向上爬一个阶梯或者爬两个阶梯。
请找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。
输入：cost = [10, 15, 20]
输出：15
解释：最低花费是从 cost[1] 开始，然后走两步即可到阶梯顶，一共花费 15 。
'''
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # 动态规划
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])

        dp = [0] * (len(cost)+1)
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[-1]


if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(Solution().minCostClimbingStairs(cost))
