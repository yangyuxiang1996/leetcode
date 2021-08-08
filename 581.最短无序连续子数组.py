#
# @lc app=leetcode.cn id=581 lang=python
#
# [581] 最短无序连续子数组
#

# @lc code=start
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums1 = sorted(nums)
        left = 0
        right = len(nums)-1
        while left <= len(nums)-1 and nums1[left] == nums[left]:
                left += 1
        if left == len(nums):
            return 0
        
        while right >= 0 and nums1[right] == nums[right]:
                right -= 1
        return right-left+1
            

# @lc code=end

