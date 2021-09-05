#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-09-03 12:53:59
LastEditors: Yuxiang Yang
LastEditTime: 2021-09-03 13:02:16
FilePath: /leetcode/剑指 Offer II 035. 最小时间差.py
Description: 
给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。
输入：timePoints = ["23:59","00:00"]
输出：1
输入：timePoints = ["00:00","23:59","00:00"]
输出：0
'''
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        mins = []
        for time in timePoints:
            time = time.split(':')
            mins.append(int(time[0])*60+int(time[1]))
        
        mins = sorted(mins)
        ans = float('inf')
        for i in range(len(mins)-1):
            ans = min(ans, mins[i+1]-mins[i])
        
        ans = min(ans, 23*60+60-mins[-1]+mins[0])

        return ans


if __name__ == '__main__':
    timePoints = ["00:00","23:59","00:00"]
    print(Solution().findMinDifference(timePoints))

        

