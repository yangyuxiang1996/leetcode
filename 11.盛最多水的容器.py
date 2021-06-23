#
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        ans = 0
        while left <= right:
            area = min(height[left], height[right]) * (right - left)
            ans = max(ans, area)
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return ans



# @lc code=end

