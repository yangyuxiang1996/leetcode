#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-17 07:55:13
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-17 08:47:26
FilePath: /leetcode/剑指 Offer 40. 最小的k个数.py
Description: 
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
'''
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        堆排序，大根堆，时间复杂度O(nlogk),空间复杂度O(k)
        heapq的堆顶维护的是当前堆的最小值，最后对里的元素是topk大的，所以要取相反数，取topk小的
        """
        import heapq
        queue = []
        for i in range(len(arr)):
            heapq.heappush(queue, -1*arr[i])
            if len(queue) > k:
                heapq.heappop(queue)

        ans = []
        while queue:
            ans.append(-1*heapq.heappop(queue))

        return ans
            


    def getLeastNumbers0(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        快速选择
        """
        if k >= len(arr):
            return arr
        # left, right = 0, len(arr)-1
        # mid = self.partition(arr, left, right)
        # while mid != k:
        #     if mid < k:
        #         mid = self.partition(arr, mid+1, right)
        #     elif mid > k:
        #         mid = self.partition(arr, left, mid-1)
        # return arr[:mid]
        def helper(arr, k, left, right):
            mid = self.partition(arr, left, right)  
            if mid < k:
                return helper(arr, k, mid+1, right)
            elif mid > k:
                return helper(arr, k, left, mid-1)
            elif mid == k:
                return arr[:mid]

        return helper(arr, k, 0, len(arr)-1)

    
    # 选择排序
    def partition(self, arr, left, right):
        pivot = arr[left]
        while left < right:
            while left < right and arr[right] >= pivot:
                right -= 1
            arr[left] = arr[right]
            while left < right and arr[left] <= pivot:
                left += 1
            arr[right] = arr[left]
        arr[left] = pivot
        return left
    
    def quickSort(self, arr, left, right):
        if left >= right:
            return
        mid = self.partition(arr, left, right)
        self.quickSort(arr, left, mid-1)
        self.quickSort(arr, mid+1, right)


if __name__ == '__main__':
    arr1 = [0,1,2,3,4,4,6,4,2,8,0,2,3,2,1,9,13,3,7,11,3,5,6,15,2,21,24,25]
    arr2 = [0,1,2,3,4,4,6,4,2,8,0,2,3,2,1,9,13,3,7,11,3,5,6,15,2,21,24,25]
    solution = Solution()
    print(arr1)
    solution.quickSort(arr1, 0, len(arr1)-1) 
    print(arr1)
    print(solution.getLeastNumbers(arr2, 10))
    
        


                
