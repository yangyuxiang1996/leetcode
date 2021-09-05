#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-09-04 10:57:51
LastEditors: Yuxiang Yang
LastEditTime: 2021-09-04 11:05:44
FilePath: /leetcode/剑指 Offer II 038. 每日温度.py
Description: 
请根据每日 气温 列表 temperatures ，重新生成一个列表，要求其对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
'''
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # 下一个更大的数
        # 单调栈
        stack = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                ans[index] = i - index
            stack.append(i)

        return ans

if __name__ == '__main__':
    temperatures = [73,74,75,71,69,72,76,73]
    print(Solution().dailyTemperatures(temperatures))



