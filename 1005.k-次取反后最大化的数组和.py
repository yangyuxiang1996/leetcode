#
# @lc app=leetcode.cn id=1005 lang=python
#
# [1005] K 次取反后最大化的数组和
#

# @lc code=start
class Solution(object):
    def largestSumAfterKNegations0(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(k):
            min_j = 0
            min_v = nums[0]
            for j in range(1, len(nums)):
                if nums[j] < min_v:
                    min_v = nums[j]
                    min_j = j
            nums[min_j] = -nums[min_j]

        return sum(nums)

    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums, key=abs, reverse=True)
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1

        if k%2 == 1:
            nums[-1] = -nums[i]

        return sum(nums)
# @lc code=end

