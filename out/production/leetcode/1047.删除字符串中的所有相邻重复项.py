#
# @lc app=leetcode.cn id=1047 lang=python
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates0(self, s):
        """
        :type s: str
        :rtype: str
        解法：栈
        """
        n = len(s)
        if n < 2:
            return s
        
        stack = []
        for i in range(n):
            c = s[i]
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)

    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        解法：双指针
        """
        if len(s) < 2:
            return s
        c = list(s)
        fast = slow = 0
        while fast < len(s):
            c[slow] = c[fast]
            if slow > 0 and c[slow] == c[slow-1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
        return "".join(c[:slow])



# @lc code=end

