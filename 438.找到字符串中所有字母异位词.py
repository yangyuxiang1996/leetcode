#
# @lc app=leetcode.cn id=438 lang=python
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution(object):
    def findAnagrams0(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        暴力解法，超时
        """
        n, m = len(s), len(p)
        p = sorted(p)
        res = []
        for i in range(n):
            if s[i] in p:
                if sorted(s[i:i+m]) == p:
                    res.append(i)
        return res


    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        滑动窗口
        """
        from collections import  defaultdict
        need = defaultdict(int)
        for i in p:
            need[i] += 1
        
        window = {}
        n, m = len(s), len(p)
        left, right = 0, 0
        valid = 0
        res = []

        while right < n:
            c = s[right]
            right += 1
            if c in need:
                if c not in window:
                    window[c] = 1
                else:
                    window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while right-left == m:  # 缩小滑动窗口
                if valid == len(need):
                    res.append(left)
                c = s[left]
                if c in window:
                    if c in need and need[c] == window[c]:
                        valid -= 1
                    window[c] -= 1
                left += 1
        
        return res


if __name__ == '__main__':
    s = 'ababc'
    p = 'ab'
    print(Solution().findAnagrams(s, p))


# @lc code=end

