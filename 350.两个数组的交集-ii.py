#
# @lc app=leetcode.cn id=350 lang=python
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1, nums2 = sorted(nums1), sorted(nums2)
        i, j = 0, 0
        res = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res

    
    def intersect0(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        from collections import defaultdict
        query = defaultdict(int)
        for num in nums2:
            query[num] += 1
        
        res = []
        for num in nums1:
            if num in query and query[num] > 0:
                res.append(num)
                query[num] -= 1
        return res


# @lc code=end

