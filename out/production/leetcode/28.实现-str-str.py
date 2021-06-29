#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr0(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        n, m = len(haystack), len(needle)
        for i in range(n-m+1):
            if haystack[i:i+m] == needle:
                return i
        return -1
    
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if n == 0:
            return 0
        
        next = self.getNext(needle)
        j = 0
        for i in range(m):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j-1]
            if haystack[i] == needle[j]:
                j += 1
            if j == n:
                return i - j + 1

        return -1

    def getNext(self, needle):
        n = len(needle)
        j = 0  # 记录第i个位置的最长相等前后缀的长度
        next=[0 for i in range(n)]  # 前缀数组，用于保存第i的位置的最长相等前后缀长度，例如aa，前缀为a，后缀为a，其最长相等前后缀长度为1
        for i in range(1, n):  # 从第二个元素开始遍历，因为第一个元素的最长相等前后缀长度为0
            while j > 0 and needle[i] != needle[j]:
                j = next[j-1]  # 跳到上一个公共前缀的末尾
            if needle[i] == needle[j]:
                j += 1
            next[i] = j

        return next


if __name__ == '__main__':
    haystack = "aabaacaabaaf"
    needle = "aabaaf"
    print(Solution().strStr(haystack, needle))
        
# @lc code=end

