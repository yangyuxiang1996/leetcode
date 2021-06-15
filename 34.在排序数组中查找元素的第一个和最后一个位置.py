#
# @lc app=leetcode.cn id=34 lang=python
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        lb, rb = -1, -1
        
        # 搜寻左边界
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1  
        if left >= len(nums) or nums[left] != target:
            lb = -1
        else:
            lb = left

        # 搜寻右边界
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        if right < 0 or nums[right] != target:
            rb = -1
        else:
            rb = right


        return [lb, rb]


if __name__ == "__main__":
    nums = [0,0,0,1,2,3]
    target = 0
    print(Solution().searchRange(nums, target))


 # @lc code=end

