#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-09-04 09:43:53
LastEditors: Yuxiang Yang
LastEditTime: 2021-09-04 10:44:50
FilePath: /leetcode/剑指 Offer II 037. 小行星碰撞.py
Description: 
给定一个整数数组 asteroids，表示在同一行的小行星。

对于数组中的每一个元素，其绝对值表示小行星的大小，正负表示小行星的移动方向（正表示向右移动，负表示向左移动）。每一颗小行星以相同的速度移动。

找出碰撞后剩下的所有小行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。
'''
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        n = len(asteroids)
        if n <= 1:
            return asteroids
        
        stack = []
        for i in range(n):
            while stack and asteroids[i] < 0 < stack[-1]:
                if stack[-1] < -asteroids[i]:
                    stack.pop()
                    continue
                if stack[-1] == -asteroids[i]:
                    stack.pop()
                break
            else:
                stack.append(asteroids[i])

        return stack


if __name__ == '__main__':
    asteroids = [-2,1,1,-1]
    print(Solution().asteroidCollision(asteroids))
                
