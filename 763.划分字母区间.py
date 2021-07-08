#
# @lc app=leetcode.cn id=763 lang=python
#
# [763] 划分字母区间
#

# @lc code=start
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        import collections
        hash = {}
        for i in range(len(s)):
            hash[s[i]] = i

        res = []
        left = right = 0
        for i in range(len(s)):
            right = max(right, hash[s[i]])
            if i == right:
                res.append(right - left + 1)
                left = i + 1
        return res
        
# @lc code=end

