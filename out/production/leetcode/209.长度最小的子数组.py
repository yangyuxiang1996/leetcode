#
# @lc app=leetcode.cn id=209 lang=python
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        时间复杂度O(N)
        """
        n = len(nums)
        if n == 0:
            return 0
        
        left = right = 0
        sum = 0
        min_length = n + 1

        while right < n:
            sum += nums[right]
            right += 1
            while sum >= target:
                min_length = min(min_length, right - left)
                sum -= nums[left]
                left += 1
        
        return min_length if min_length <= n else 0
            

if __name__ == '__main__':
    target = 11
    nums = [1,1,1,1,1,1,1,1]
    print(Solution().minSubArrayLen(target, nums))

# @lc code=end

