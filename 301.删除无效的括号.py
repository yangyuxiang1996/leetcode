#
# @lc app=leetcode.cn id=301 lang=python
#
# [301] 删除无效的括号
#

# @lc code=start
class Solution(object):
    def __init__(self):
        self.res = set()
        self.n = 0

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # 首先要遍历字符串，统计需要删除的左括号和右括号的数量
        left_remove = right_remove = 0
        self.n = len(s)
        for i in range(self.n):
            if s[i] == '(':
                left_remove += 1
            elif s[i] == ')':
                if left_remove == 0:
                    right_remove += 1
                elif left_remove > 0:
                    left_remove -= 1

        self.backtrace(s, 0, 0, 0, left_remove, right_remove, [])
        return list(self.res)
        
        

    def backtrace(self, s, index, left_count, right_count, left_remove, right_remove, path):
        """
        :param index: 字符串id
        :param leftcount: 保留的左括号数量
        :param rightcount: 保留的右括号数量
        :param leftremove: 需要移除的左括号数量
        :param rightremove: 需要移除的右括号数量
        :param st: 保留下来的字符串
        :return:
        """
        if index == len(s):
            if left_remove == 0 and right_remove == 0:
                self.res.add(''.join(path))
            return
        
        # 选择1:删除
        if s[index] == '(' and left_remove > 0:
            # 由于 leftRemove > 0，并且当前遇到的是左括号，因此可以尝试删除当前遇到的左括号
            self.backtrace(s, index+1, left_count, right_count, left_remove-1, right_remove, path)
        if s[index] == ')' and right_remove > 0:
            # 由于 rightRemove > 0，并且当前遇到的是右括号，因此可以尝试删除当前遇到的右括号
            self.backtrace(s, index+1, left_count, right_count, left_remove, right_remove-1, path)

        # 选择2:保留
        path.append(s[index])
        if s[index] != ')' and s[index] != '(':
            # 如果不是括号，继续深度优先遍历
            self.backtrace(s, index+1, left_count, right_count, left_remove, right_remove, path)
        elif s[index] == '(':
            self.backtrace(s, index+1, left_count+1, right_count, left_remove, right_remove, path)
        elif right_count < left_count:
            self.backtrace(s, index+1, left_count, right_count+1, left_remove, right_remove, path)
        path.pop()



# @lc code=end

