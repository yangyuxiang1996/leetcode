#!/usr/bin/env python
# coding=utf-8
'''
Author: yangyuxiang
Date: 2021-07-13 11:03:32
LastEditors: yangyuxiang
LastEditTime: 2021-07-15 08:55:50
FilePath: /leetcode/0.01背包.py
Description: 
'''

'''
01背包问题：有N件物品和一个最多能被重量为W 的背包。第i件物品的重量是weight[i]，得到的价值是value[i] 。每件物品只能用一次，求解将哪些物品装入背包里物品价值总和最大。
测试数据：
weights: [1,3,4]
values: [15,20,30]
maxWeight: 4
expected answer: 35
'''

class Solution:
    def findMaxValue0(self, weights, values, maxWeight):
        '''
        动态规划，定义一个二维dp数组，dp[i][j]表示当前背包容量为j时，在前i个物品中能够取得的最大价值
        对于第i个物品，无非两种选择，放或不放：不放时，dp[i][j] = dp[i-1][j]；放时，需要保证当前剩余容量大于当前物品的重量，所以需要倒推到j-weights[i]的位置，才能保证放下物品i
        状态转移方程：dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]]+values[i])
        时间复杂度：O(NM), 空间复杂度O(NM)
        '''
        # 定义dp数组
        dp = [[0] * (maxWeight + 1) for _ in range(len(weights)+1)]
        # 初始化dp数组
        # for i in range(len(weights)):
        #     dp[i][0] = 0  # 背包容量为0时，最大价值为0、
        # for j in range(weights[0], maxWeight+1):
        #     dp[0][j] = values[0]  # 只有当当前背包容量大于第0个物品的重量时，背包才能放下东西

        # 递推
        for i in range(1, len(weights)+1):
            for j in range(0, maxWeight+1):
                if j - weights[i-1] >= 0:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]]+values[i-1])
                else:
                    dp[i][j] = dp[i-1][j]

            print(dp[i-1])
        print(dp[i-1])    
        return dp[-1][-1]

    def findMaxValue1(self, weights, values, maxWeight):
        '''
        动态规划，从上面的解法可以看出，对于i，在每一层遍历时只用到了上一层的元素，因此这里可以将二维dp数组压缩成一维dp数组，降低空间复杂度
        
        '''
        dp = [0] * (maxWeight+1)
                # 递推
        for i in range(0, len(weights)):
            for j in range(maxWeight, 0, -1):  # 注意这里只能从后向前遍历，因为如果从前向后遍历的话，前面的值会被修改，但是后面需要的是修改前的值
                if j - weights[i] >= 0:
                    dp[j] = max(dp[j], dp[j-weights[i]]+values[i])
                else:
                    dp[j] = dp[j]
            print(dp)
        
        return dp[-1]
        




if __name__ == '__main__':
    weights = [1,3,4]
    values = [15,20,30]
    maxWeight = 4
    print(Solution().findMaxValue0(weights, values, maxWeight))
    
                
