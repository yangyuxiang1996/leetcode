#
# @lc app=leetcode.cn id=383 lang=python
#
# [383] 赎金信
#

# @lc code=start
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if not ransomNote:
            return True
        if not magazine:
            return False
        
        from collections import defaultdict
        # d1 = defaultdict(int)
        # d2 = defaultdict(int)
        # for i in ransomNote:
        #     d1[i] += 1
        # for i in magazine:
        #     d2[i] += 1

        # for i in ransomNote:
        #     if i not in d2 or d1[i] > d2[i]:
        #         return False
        # return True

        d = defaultdict(int)
        for i in magazine:
            d[i] += 1
        for i in ransomNote:
            if i not in d or d[i] <= 0:
                return False
            else:
                d[i] -= 1
        return True
# @lc code=end

