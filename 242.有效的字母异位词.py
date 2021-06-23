#
# @lc app=leetcode.cn id=242 lang=python
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution(object):
    def isAnagram0(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
    
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # from collections import Counter
        # ss = Counter(s)
        # tt = Counter(t)
        from collections import defaultdict
        ss = defaultdict(int)
        tt = defaultdict(int)
        for i in s:
            ss[i] += 1
        for i in t:
            tt[i] += 1
        return ss == tt
# @lc code=end

