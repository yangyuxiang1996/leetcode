#
# @lc app=leetcode.cn id=27 lang=python
#
# [27] 移除元素
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        快慢指针
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow



    def removeElement1(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        双指针
        """
        start, end = 0, len(nums)-1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            else:
                start += 1

        return start


    def removeElement0(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return
        
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                pre = i
                while pre < n and nums[pre] == val:
                    pre += 1
                if pre == n:
                    break
                nums[pre], nums[i] = nums[i], nums[pre]
            else:
                i += 1
        
        return i

            


if __name__ == '__main__':
    nums = [1,2,3,2,4]
    val = 2
    print(Solution().removeElement(nums, val))

# @lc code=end

