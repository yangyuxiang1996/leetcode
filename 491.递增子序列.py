#
# @lc app=leetcode.cn id=491 lang=python
#
# [491] 递增子序列
#

# @lc code=start
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        result = []

        def backtrace(start, path):
            if len(path) >= 2:
                result.append(path[:])
            repeat = []
            for i in range(start, len(nums)):
                if nums[i] in repeat:
                    continue
                if not path or nums[i] >= path[-1]:
                    path.append(nums[i])
                    repeat.append(nums[i])
                    backtrace(i+1, path)
                    path.pop()
        backtrace(0, [])
        return result
# @lc code=end

