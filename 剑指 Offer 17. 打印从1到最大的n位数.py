#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-14 09:48:23
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-15 00:07:43
FilePath: /leetcode/剑指 Offer 17. 打印从1到最大的n位数.py
Description: 
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
'''

class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        全排列
        """
        def dfs(index, num, digit):
            if index == digit:
                res.append(int(''.join(num)))
                return
            for i in range(10):
                num.append(str(i))
                dfs(index + 1, num, digit)
                num.pop()

        res = []
        for digit in range(1, n + 1):
            for first in range(1, 10):
                num = [str(first)]
                dfs(1, num, digit)
        return res
        
    
    def printNumbers0(self, n):
        """
        :type n: int
        :rtype: List[int]
        队列
        """
        res = []
        queue = []
        for i in range(1, 10):
            queue.append(str(i))

        while queue:
            for i in range(len(queue)):
                val = queue.pop(0)
                res.append(int(val))
                if len(val) < n:
                    for j in range(10):
                        tmp = val + str(j)
                        queue.append(tmp)
        return res

    
if __name__ == '__main__':
    n = 3
    print(Solution().printNumbers(n))


            
            
