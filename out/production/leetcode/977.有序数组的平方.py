#
# @lc app=leetcode.cn id=977 lang=python
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        双指针
        """
        n = len(nums)
        res = [0] * n
        i, j, pos = 0, n-1, n-1
        while i <= j:
            if nums[i]**2 > nums[j]**2:
                res[pos] = nums[i]**2
                i += 1
            else:
                res[pos] = nums[j]**2
                j -= 1
            pos -= 1
        return res


    def sortedSquares0(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp1 = []
        tmp = [0] * len(nums)
        j = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                tmp1.append(nums[i]**2)
            else:
                tmp[j] = nums[i]**2
                j += 1
        tmp1 = tmp1[::-1]

        # tmp = []
        def merge(nums1, m, nums2, n):
            while m > 0 and n > 0:
                if nums1[m-1] > nums2[n-1]:
                    nums1[m+n-1] = nums1[m-1]
                    m -= 1
                else:
                    nums1[m+n-1] = nums2[n-1]
                    n -= 1
            nums1[:n] = nums2[:n]

        merge(tmp, j, tmp1, len(tmp1))
        
        return tmp


if __name__ == '__main__':
    nums = [-4,-1,0,3,10]
    print(Solution().sortedSquares(nums))
                
# @lc code=end

