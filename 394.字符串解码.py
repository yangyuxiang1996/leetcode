#
# @lc app=leetcode.cn id=394 lang=python
#
# [394] 字符串解码
#

# @lc code=start
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        :解法: 栈
        :链接: https://leetcode-solution-leetcode-pp.gitbook.io/leetcode-solution/medium/394.decode-string
        """
        stack = []
        for i in range(len(s)):
            if s[i] != ']':  # 只要不是']'，就一直入栈
                stack.append(s[i])
            else:
                repeat_str = ''
                repeat_count = ''
                while stack and stack[-1] != '[':
                    repeat_str = stack.pop() + repeat_str  # 注意这里的顺序要和出栈的顺序反过来
                stack.pop()  # '['出栈
                while stack and stack[-1].isdigit():
                    repeat_count = stack.pop() + repeat_count  # 注意这里的顺序要和出栈的顺序反过来
                stack.append(repeat_str * int(repeat_count))  # 最后把重复的字符串放入栈中
        return ''.join(stack)


                

# @lc code=end

