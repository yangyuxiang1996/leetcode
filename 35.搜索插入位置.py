#
# @lc app=leetcode.cn id=35 lang=python
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution(object):
    def searchInsert0(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        左闭右闭
        """
        if not target:
            return 0
        
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        左闭右开
        """
        if not target:
            return 0
        
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left

 # @lc code=end

