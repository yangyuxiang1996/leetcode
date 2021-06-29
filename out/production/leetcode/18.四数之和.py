#
# @lc app=leetcode.cn id=18 lang=python
#
# [18] 四数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        res = []
        lo, hi = 0, len(nums)-1
        while lo < hi:
            left, right = nums[lo], nums[hi]
            if left + right < target:
                lo += 1
            elif left + right > target:
                hi -= 1
            else:
                res.append([left, right])
                while lo < hi and nums[lo] == left:
                    lo += 1
                while lo < hi and nums[hi] == right:
                    hi -= 1
        return res

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        n = len(nums)
        res = []
        i = 0
        while i < n:
            j = i+1
            while j < n:
                other = target - nums[i] - nums[j]
                tmp = self.twoSum(nums[j+1:], other)
                for l in tmp:
                    l.append(nums[i])
                    l.append(nums[j])
                    res.append(l)
                while j < n-1 and nums[j] == nums[j+1]:
                    j+=1
                j += 1
            while i < n-1 and nums[i] == nums[i+1]:
                i+=1
            i += 1
        return res


if __name__ == '__main__':
    nums = [2,2,2,2,2]
    target = 8
    print(Solution().fourSum(nums, target))
# @lc code=end

