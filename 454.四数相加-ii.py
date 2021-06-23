#
# @lc app=leetcode.cn id=454 lang=python
#
# [454] 四数相加 II
#

# @lc code=start
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        hashmap = {}
        count = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                tmp = nums1[i] + nums2[j]
                if tmp in hashmap:
                    hashmap[tmp] += 1
                else:
                    hashmap[tmp] = 1
        
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                tmp = nums3[i] + nums4[j]
                if -tmp in hashmap:
                    count += hashmap[-tmp]
        return count
# @lc code=end

