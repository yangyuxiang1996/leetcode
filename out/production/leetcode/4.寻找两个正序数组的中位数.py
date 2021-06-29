#
# @lc app=leetcode.cn id=4 lang=python
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        基本思路：在两个有序数组上寻找分割线，将两个有序数组分割成左右两部分，
        条件1：左边的元素与右边的元素个数相等或者左边元素个数比右边多一个
        条件2: 左边所有元素的值小于右边元素的值
        如果两个数组的长度和为奇数，那么左边元素的最大值就是中位数；
        如果两个数组的长度和为偶数，那么左边元素的最大值和右边元素的最小值的均值就是中位数；
        """

        # 首先固定长度较小的数组为nums1
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)

        l_size = (m+n+1) // 2  # 统一m+n为偶数和奇数的两种情况

        # 定义i为nums1的分割位置，nums1中左边元素个数为i个；定义j为nums2的分割位置，nums2中左边元素个数为j个
        # 满足i+j=l_size
        # 符合要求的分割位置：nums1[i-1] <= nums2[j] && nums1[i] >= nums2[j-1]
        left, right = 0, m
        while left < right:
            i = left + (right - left + 1) // 2
            j = l_size - i
            if nums1[i-1] > nums2[j]:
                # 下一次搜索位置: [left, i-1]
                right = i - 1
            elif nums1[i-1] <= nums2[j]:
                # 下一次搜索位置: [i, right]
                left = i

        i = left
        j = l_size - i
        nums1LeftMax = nums1[i-1] if i != 0 else float('-inf')
        nums1RightMin = nums1[i] if i != m else float('inf')
        nums2LeftMax = nums2[j-1] if j != 0 else float('-inf')
        nums2RightMin = nums2[j] if j != n else float('inf')

        if (m+n) % 2 == 1:
            return max(nums1LeftMax, nums2LeftMax)
        else:
            return (max(nums1LeftMax, nums2LeftMax) + \
                min(nums1RightMin, nums2RightMin)) / 2.



        

        
# @lc code=end

