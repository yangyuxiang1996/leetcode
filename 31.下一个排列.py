#
# @lc app=leetcode.cn id=31 lang=python
#
# [31] 下一个排列
#

# @lc code=start
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        
        # 从后向前查找第一个相邻升序的元素对 (i,j)，nums[i] < nums[j]
        i = len(nums)-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        j = i + 1
        
        # 然后在 [j,end) 从后向前查找第一个大于 A[i] 的值 A[k]
        for k in range(len(nums)-1, j-1, -1):
            if i >= 0 and nums[i] < nums[k]:
                nums[i], nums[k] = nums[k], nums[i]
                break
        
        # 这时 [j,end) 必然是降序，逆置 [j,end)，使其升序
        left, right = j, len(nums)-1
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        return


if __name__ == '__main__':
    nums = [5,1,1]
    Solution().nextPermutation(nums)
    print(nums)
        
        


        

        
# @lc code=end

