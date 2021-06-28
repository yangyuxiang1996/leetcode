#
# @lc app=leetcode.cn id=150 lang=python
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution(object):
    def calc(self, x, y, f):
        if f == "+":
            return y + x
        elif f == "-":
            return y - x
        elif f == "*":
            return y * x
        else:
            return int(float(y)/x)

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0
        
        stack = []
        funcs = ['+', '-', '*', '/']
        for token in tokens:
            if token not in funcs:
                stack.append(int(token))
            else:
                res = self.calc(stack.pop(), stack.pop(), token)
                stack.append(res)

        return stack[-1]


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens))
# @lc code=end

