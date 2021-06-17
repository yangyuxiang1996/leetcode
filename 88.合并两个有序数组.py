#
# @lc app=leetcode.cn id=88 lang=python
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution(object):
    def find_position(self, nums, m, target):
        if not nums:
            return

        left, right = 0, m
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid+1
        return left


    def merge0(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for num in nums2:
            idx = self.find_position(nums1, m, num)
            nums1[idx+1:] = nums1[idx:-1]
            nums1[idx] = num
            m += 1

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            
        nums1[:n] = nums2[:n]



if __name__ == '__main__':
    nums1 = [1,0,0,0]
    m = 1
    nums2 = [2,2,3]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)







# @lc code=end

