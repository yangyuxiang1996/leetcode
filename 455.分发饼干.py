#
# @lc app=leetcode.cn id=455 lang=python
#
# [455] 分发饼干
#

# @lc code=start
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)

        # result = 0
        # i = len(s)-1        
        # while i >= 0 :
        #     if g and s[i] >= g[-1]:
        #         result += 1
        #         i -= 1

        #     if not g:
        #         return result

        #     g.pop()

        # result = 0
        # index = len(s)-1
        # for i in range(len(g)-1, -1, -1):
        #     if index >= 0 and s[index] >= g[i]:  # 大饼干先喂大胃口
        #         result += 1
        #         index -= 1

        result = 0
        for i in range(len(s)):
            if result < len(g) and g[result] <= s[i]:  # 小饼干喂小胃口
                result += 1 

        return result
            

if __name__ == '__main__':
    g = [1,2,3]
    s = [3]
    print(Solution().findContentChildren(g,s))
            
# @lc code=end

