#
# @lc app=leetcode.cn id=151 lang=python
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution(object):
    def reverseWords0(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(reversed(s.split()))

    def removeBlank(self, s):
        # 去除两端空格
        left, right = 0, len(s)-1
        while left < right and s[left] == ' ':
            left += 1
        while left < right and s[right] == ' ':
            right -= 1

        # 去除中间的空格
        output = list(s[left:right+1])
        lo, hi = 0, 0
        while hi < len(output):
            if output[hi] == ' ' and output[hi+1] == ' ':
                hi += 1
            else:
                output[lo] = output[hi]
                lo += 1
                hi += 1
        
        return output[:lo]

    def reverse_str(self, s):
        if isinstance(s, str):
            s = list(s)
        left, right = 0, len(s)-1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

    def reverse_words(self, s):
        start, end = 0, 0
        n = len(s)
        while start < n:
            while end < n and s[end] != ' ':
                end += 1
            s[start:end] = self.reverse_str(s[start:end])
            start = end+1
            end += 1
        return s

    def reverseWords(self, s):
        s = self.removeBlank(s)
        s = self.reverse_str(s)
        s = self.reverse_words(s)
        return "".join(s)


if __name__ == '__main__':
    s = "  hello nihao   w   orld!  "
    s = Solution().reverseWords(s)
    print(s)    
# @lc code=end

