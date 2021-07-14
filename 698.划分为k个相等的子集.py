#
# @lc app=leetcode.cn id=698 lang=python
#
# [698] 划分为k个相等的子集
#

# @lc code=start
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        回溯+剪枝
        """
        sum_ = sum(nums)
        if sum_ % k != 0:
            return False
        
        target = sum_ // k
        used = [False] * len(nums)

        def backtrace(nums, k, target, cur, start, used):
            if k == 0:
                return True
            if cur == target:
                return backtrace(nums, k-1, target, 0, 0, used)
            
            for i in range(start, len(nums)):
                if not used[i] and cur + nums[i] <= target:
                    used[i] = True
                    if backtrace(nums, k, target, cur+nums[i], i+1, used):
                        return True
                    used[i] = False
            
            return False
        
        return backtrace(nums, k, target, 0, 0, used)


if __name__ == '__main__':
    nums = [1,1,1,1,2,2,2,2]
    k = 2
    print(Solution().canPartitionKSubsets(nums, k))
# @lc code=end

