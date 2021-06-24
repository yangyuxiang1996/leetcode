#
# @lc app=leetcode.cn id=541 lang=python
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        n = len(s)
        for i in range(0, n, 2*k):
            left = i
            right = i + k - 1 if i + k - 1 <= n-1 else n-1
            while left <= right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)


if __name__ == '__main__':
    s="abcdefg"
    k=2
    print(Solution().reverseStr(s, k))

# @lc code=end

