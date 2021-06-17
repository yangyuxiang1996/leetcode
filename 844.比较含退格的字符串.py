#
# @lc app=leetcode.cn id=844 lang=python
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution(object):
    def backspaceCompare0(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        栈
        """
        def build(s):
            n = len(s)
            stack = []
            for i in range(n):
                if s[i] != '#':
                    stack.append(s[i])
                else:
                    if stack:
                        stack.pop()
            
            return "".join(stack)
        
        return build(s) == build(t)


    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        双指针
        """
        end_s = len(s)-1
        end_t = len(t)-1
        skip_s = skip_t = 0

        while end_s >= 0 or end_t >= 0:
            while end_s >= 0:
                if s[end_s] == '#':
                    skip_s +=1
                    end_s -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    end_s -= 1
                else:
                    break
            while end_t >= 0:
                if t[end_t] == '#':
                    skip_t +=1
                    end_t -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    end_t -= 1
                else:
                    break
            
            if end_s >= 0 and end_t >= 0:
                if s[end_s] != t[end_t]:
                    return False
            else:
                if end_s >= 0 or end_t >= 0:
                    return False
            
            end_s -= 1
            end_t -= 1

        return True


if __name__ == '__main__':
    s = "q"
    t = "#"
    print(Solution().backspaceCompare(s, t))

        
# @lc code=end

