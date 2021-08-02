#
# @lc app=leetcode.cn id=215 lang=python
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution(object):
    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        l = []
        for i in range(len(nums)):
            heapq.heappush(l, nums[i])
        
        for i in range(len(nums)-k):
            heapq.heappop(l)

        return heapq.heappop(l)

# @lc code=end

